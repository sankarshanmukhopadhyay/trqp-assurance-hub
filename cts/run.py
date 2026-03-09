"""CTS runner entrypoint.

This module executes TRQP Conformance Suite profiles against a target SUT and emits
machine-readable evidence artifacts (reports, manifests, bundles).

Operator notes:
- Prefer deterministic mode for CI and audit-grade runs.
- Outputs are written under the configured output directory with stable naming.

This docstring exists to make the runner easier to maintain and safer to adapt.
"""

import argparse, json, time, hashlib, zipfile, uuid
from pathlib import Path
from datetime import datetime, timezone
import yaml
import requests
from jsonschema import validate as js_validate
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder

ROOT = Path(__file__).resolve().parent.parent

def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())


def guess_media_type(p: Path) -> str | None:
    suf = p.suffix.lower()
    if suf == ".json":
        return "application/json"
    if suf == ".zip":
        return "application/zip"
    if suf in [".txt", ".log"]:
        return "text/plain"
    if suf in [".yaml", ".yml"]:
        return "text/yaml"
    return None


def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def json_path_get(doc, path: str):
    """
    Minimal JSONPath-like accessor.

    Supports:
      - $.a.b.c
      - $.a[0].b
      - $["key.with.dots"].a
      - wildcard array iteration: $.items[*].id  (returns list of matches)
    """
    if not path.startswith("$"):
        raise ValueError("Only supports paths starting with $")

    # Tokenize
    i = 1  # skip $
    tokens = []
    while i < len(path):
        if path[i] == ".":
            i += 1
            # read identifier until . or [ or end
            j = i
            while j < len(path) and path[j] not in ".[":
                j += 1
            tokens.append(("key", path[i:j]))
            i = j
        elif path[i] == "[":
            # index, wildcard, or quoted key
            j = path.find("]", i)
            if j == -1:
                raise ValueError(f"Unclosed [ in path: {path}")
            inner = path[i+1:j]
            if inner == "*":
                tokens.append(("wildcard", None))
            elif (inner.startswith('"') and inner.endswith('"')) or (inner.startswith("'") and inner.endswith("'")):
                tokens.append(("key", inner[1:-1]))
            else:
                # assume integer index
                tokens.append(("index", int(inner)))
            i = j + 1
        else:
            raise ValueError(f"Unexpected character in path at {i}: {path[i]} ({path})")

    def step(cur, tok):
        kind, val = tok
        if kind == "key":
            return cur.get(val) if isinstance(cur, dict) else None
        if kind == "index":
            if isinstance(cur, list) and 0 <= val < len(cur):
                return cur[val]
            return None
        if kind == "wildcard":
            if isinstance(cur, list):
                return cur[:]  # list of items to expand
            return None
        raise ValueError("unknown token")

    cur = doc
    for idx, tok in enumerate(tokens):
        if tok[0] == "wildcard":
            # Expand wildcard: apply remaining tokens to each element
            remainder = tokens[idx + 1:]
            arr = step(cur, tok)
            if arr is None:
                return None
            out = []
            for item in arr:
                c = item
                for rt in remainder:
                    c = step(c, rt)
                    if c is None:
                        break
                if c is not None:
                    out.append(c)
            return out
        else:
            cur = step(cur, tok)
            if cur is None:
                return None
    return cur

def ensure_dirs(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    (out/"cases").mkdir(exist_ok=True)

def http_request(base_url: str, tc: dict, headers: dict, body):
    url = base_url.rstrip("/") + tc["path"]
    method = tc.get("method", "POST").upper()
    return requests.request(method, url, headers=headers, json=body, timeout=20)

def add_ha_headers(headers: dict, sut: dict, nonce: str, ts: str):
    # Demo HA control plane (example SUT expects these)
    headers["X-Auth-Mode"] = "high_assurance"
    api_key = sut.get("api_key")
    if not api_key:
        raise SystemExit("High assurance profile requires sut.api_key (refusing to default to demo-secret)")
    headers["X-API-Key"] = api_key
    headers["X-Nonce"] = nonce
    headers["X-Timestamp"] = ts


def resolve_identifiers(sut: dict) -> dict:
    """Return identifier overrides from sut config, with defaults."""
    defaults = {
        "authority_id": "did:example:transport-ministry",
        "entity_id": "did:example:logistics-sp-123",
        "subject_authority_id": "did:example:foreign-authority-xyz",
        "action": "issue-transport-credential",
    }
    overrides = sut.get("identifiers", {}) or {}
    return {**defaults, **overrides}


def apply_identifier_overrides(body: dict | None, identifiers: dict) -> dict | None:
    """Replace placeholder identifier values in a request body with SUT-specific overrides."""
    if body is None:
        return body
    result = dict(body)
    for field in ("authority_id", "entity_id", "subject_authority_id", "action"):
        if field in result:
            result[field] = identifiers[field]
    return result


def list_tests(tests: list, profile: dict) -> None:
    """Print test IDs and names applicable to the given profile."""
    profile_id = profile.get("id")
    print(f"Tests applicable to profile '{profile_id}':\n")
    for tc in tests:
        applicable_profiles = tc.get("profiles")
        if applicable_profiles and profile_id not in applicable_profiles:
            status = "NOT_APPLICABLE"
        else:
            status = "applicable"
        print(f"  [{status}] {tc['id']}: {tc.get('name', '')}")
    print()


def main():
    ap = argparse.ArgumentParser(description="TRQP Conformance Suite runner")
    ap.add_argument("--profile", required=True, help="Path to profile YAML")
    ap.add_argument("--sut", required=True, help="Path to SUT config YAML")
    ap.add_argument("--out", required=True, help="Output directory for evidence artifacts")
    ap.add_argument("--dry-run", action="store_true",
                    help="Validate inputs and list applicable tests without executing any HTTP requests")
    ap.add_argument("--list-tests", action="store_true",
                    help="Print tests applicable to the selected profile and exit")
    args = ap.parse_args()

    profile = load_yaml(Path(args.profile))
    sut = load_yaml(Path(args.sut))
    out = Path(args.out)

    tests = load_yaml(ROOT/"tests/core_tests.yaml")["tests"]
    identifiers = resolve_identifiers(sut)

    if args.list_tests:
        list_tests(tests, profile)
        return

    if args.dry_run:
        print(f"Dry run: profile='{profile.get('id')}', sut base_url='{sut.get('base_url')}'")
        list_tests(tests, profile)
        print("Dry run complete — no HTTP requests were made.")
        return

    ensure_dirs(out)

    if profile.get("gates", {}).get("require_state_reference") and not sut.get("state_reference"):
        raise SystemExit("Gate failed: sut.state_reference required for this profile.")

    run_id = str(uuid.uuid4())
    run = {
        "test_run_id": run_id,
        "profile_id": profile["id"],
        "out_dir_label": out.name,
        "sut": {k:v for k,v in sut.items() if k != "signing_key_b64"},
        "started_at": now_iso(),
        "tool": {"name": "trqp-cts", "version": "0.1.0"},
    }

    base_url = sut["base_url"]
    verdicts = []

    for tc in tests:
        _verdict_override = None
        tc_id = tc["id"]

        # Profile gating: tests may declare 'profiles: [..]' to indicate applicability.
        applicable_profiles = tc.get("profiles")
        if applicable_profiles and profile.get("id") not in applicable_profiles:
            case = {
                "test_case_id": tc_id,
                "name": tc.get("name"),
                "request": {"method": tc.get("method","POST"), "path": tc["path"], "headers": {}, "body": None},
                "response": {"status": None, "headers": {}, "text": ""},
                "elapsed_ms": 0,
                "assertions": [{"type": "profile_gate", "profiles": applicable_profiles, "profile_id": profile.get("id"), "pass": True}],
                "skipped": True
            }
            case_path = out/"cases"/f"{tc_id}.json"
            case_path.write_text(json.dumps(case, indent=2), encoding="utf-8")
            verdicts.append({"test_case_id": tc_id, "result": "NOT_APPLICABLE", "reason": f"not applicable to profile {profile.get('id')}", "elapsed_ms": 0})
            continue
        try:
            headers = dict(sut.get("default_headers", {}))
            headers.update(tc.get("request", {}).get("headers", {}) or {})
            body = tc.get("request", {}).get("body", None)
            body = apply_identifier_overrides(body, identifiers)

            # If profile is HA, add HA headers for tests except TC-SEC-001 (which asserts unauth)
            if profile["id"] == "high_assurance" and tc_id != "TC-SEC-001":
                nonce = "nonce-" + str(uuid.uuid4())
                ts = now_iso()
                add_ha_headers(headers, sut, nonce, ts)

            started = time.time()
            resp = http_request(base_url, tc, headers, body)
            elapsed_ms = int((time.time() - started) * 1000)

            case = {
                "id": tc_id,
                "name": tc.get("name"),
                "request": {"method": tc.get("method","POST"), "path": tc["path"], "headers": headers, "body": body},
                "response": {"status": resp.status_code, "headers": dict(resp.headers), "text": resp.text},
                "elapsed_ms": elapsed_ms,
                "assertions": []
            }

            ok = True
            exp = tc.get("expect", {})

            if "status" in exp and "status_in" in exp:
                ok = False
                case["assertions"].append({"type":"expect_config","error":"expect.status and expect.status_in are mutually exclusive","pass":False})
            
            if "status" in exp:
                passed = resp.status_code == exp["status"]
                ok &= passed
                case["assertions"].append({"type":"status", "expected":exp["status"], "actual":resp.status_code, "pass":passed})

            if "status_in" in exp:
                passed = resp.status_code in exp["status_in"]
                ok &= passed
                case["assertions"].append({"type":"status_in", "expected":exp["status_in"], "actual":resp.status_code, "pass":passed})

            resp_json = None
            needs_json = any(k in exp for k in ["schema","json_path_exists","json_path_equals"]) or exp.get("response_json")
            if needs_json:
                try:
                    resp_json = resp.json()
                    case["response"]["json"] = resp_json
                    case["assertions"].append({"type":"json_parse","pass":True})
                except Exception:
                    ok = False
                    case["assertions"].append({"type":"json_parse","pass":False})

            if "response_header_contains" in exp:
                for k,v in exp["response_header_contains"].items():
                    actual = resp.headers.get(k)
                    passed = (actual is not None and v in actual) if k.lower()=="content-type" else (actual == v)
                    ok &= passed
                    case["assertions"].append({"type":"header_contains","header":k,"expected":v,"actual":actual,"pass":passed})

            if exp.get("schema") and resp_json is not None:
                schema = load_json(ROOT/exp["schema"])
                try:
                    js_validate(instance=resp_json, schema=schema)
                    case["assertions"].append({"type":"schema","schema":exp["schema"],"pass":True})
                except Exception as e:
                    ok = False
                    case["assertions"].append({"type":"schema","schema":exp["schema"],"pass":False,"error":str(e)})

            if exp.get("json_path_exists") and resp_json is not None:
                for p in exp["json_path_exists"]:
                    v = json_path_get(resp_json, p)
                    passed = (v is not None) and (v != [])
                    ok &= passed
                    case["assertions"].append({"type":"json_path_exists","path":p,"pass":passed})

            if exp.get("json_path_equals") and resp_json is not None:
                for p, expected in exp["json_path_equals"]:
                    actual = json_path_get(resp_json, p)
                    passed = (actual == expected)
                    ok &= passed
                    case["assertions"].append({"type":"json_path_equals","path":p,"expected":expected,"actual":actual,"pass":passed})

            if exp.get("json_path_in") and resp_json is not None:
                for p, allowed in exp["json_path_in"]:
                    actual = json_path_get(resp_json, p)
                    passed = actual in allowed
                    ok &= passed
                    case["assertions"].append({"type":"json_path_in","path":p,"allowed":allowed,"actual":actual,"pass":passed})

            # Special replay test for HA: send the same nonce twice to trigger 409
            if tc_id == "TC-SEC-002" and profile["id"] == "high_assurance":
                # Reuse the same nonce/timestamp headers
                resp2 = http_request(base_url, tc, headers, body)
                passed = resp2.status_code == exp["status"]
                ok &= passed
                case["assertions"].append({"type":"replay","expected":exp["status"],"actual":resp2.status_code,"pass":passed})

        except Exception as e:
            # Record as ERROR to keep reports deterministic and audit-friendly
            elapsed_ms = int((time.time() - started) * 1000) if 'started' in locals() else 0
            case = {
                "id": tc_id,
                "name": tc.get("name"),
                "request": {"method": tc.get("method","POST"), "path": tc.get("path"), "headers": headers if 'headers' in locals() else {}, "body": body if 'body' in locals() else None},
                "response": {"status": None, "headers": {}, "text": ""},
                "elapsed_ms": elapsed_ms,
                "assertions": [{"type": "exception", "pass": False, "error": str(e)}],
            }
            ok = False
            _verdict_override = "ERROR"
        case_path = out/"cases"/f"{tc_id}.json"
        case_path.write_text(json.dumps(case, indent=2), encoding="utf-8")

        verdicts.append({"test_case_id": tc_id, "result": (_verdict_override if _verdict_override else ("PASS" if ok else "FAIL")), "elapsed_ms": elapsed_ms})

    run["ended_at"] = now_iso()
    (out/"run.json").write_text(json.dumps(run, indent=2), encoding="utf-8")
    (out/"verdicts.json").write_text(json.dumps(verdicts, indent=2), encoding="utf-8")

    manifest = {"generated_at": now_iso(), "hashes": {}}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name not in ["bundle.zip","manifest.sig"]:
            manifest["hashes"][str(p.relative_to(out))] = sha256_file(p)

    manifest_path = out/"manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    if profile.get("evidence", {}).get("sign_manifest"):
        key_b64 = sut.get("signing_key_b64")
        if not key_b64:
            raise SystemExit("sign_manifest enabled but sut.signing_key_b64 missing")
        sk = SigningKey(key_b64.encode("utf-8"), encoder=Base64Encoder)
        sig = sk.sign(manifest_path.read_bytes()).signature
        (out/"manifest.sig").write_bytes(sig)

    if profile.get("evidence", {}).get("bundle", True):
        bundle = out/"bundle.zip"
        with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(out.rglob("*")):
                if p.is_file() and p.name != "bundle.zip":
                    z.write(p, arcname=str(p.relative_to(out)))

    # Bundle descriptor (machine-readable index of key artifacts)
    descriptor = {
        "bundle_version": "0.1.0",
        "run": run,
        "artifacts": {
            "run_json": "run.json",
            "verdicts": "verdicts.json",
            "manifest": "manifest.json",
            "cases_dir": "cases"
        }
    }
    if (out/"manifest.sig").exists():
        descriptor["artifacts"]["signature"] = "manifest.sig"

    # Normalized artifact index (canonical kinds where applicable)
    artifact_index = []

    # Hub-aligned artifact_kind values (stable semantic labels)
    ARTIFACT_KIND_MAP = {
        "cts_run_json": "conformance_run_metadata",
        "cts_verdicts": "conformance_verdicts",
        "cts_manifest": "conformance_manifest",
        "cts_manifest_sig": "conformance_manifest_signature",
        "cts_case_file": "conformance_case_artifact",
        "cts_bundle_zip": "conformance_evidence_bundle_zip",
        "cts_bundle_descriptor": "conformance_evidence_bundle_descriptor",
        "cts_checksums": "evidence_bundle_checksums",
    }


    def add_idx(kind: str, rel_path: str, notes: str | None = None):
        p = out/rel_path
        entry = {
            "kind": kind,
            "artifact_kind": ARTIFACT_KIND_MAP.get(kind),
            "path": rel_path,
            "produced_by": "trqp-cts",
        }
        if p.exists() and p.is_file():
            entry["sha256"] = sha256_file(p)
            mt = guess_media_type(p)
            if mt:
                entry["media_type"] = mt
        if notes:
            entry["notes"] = notes
        artifact_index.append(entry)

    add_idx("cts_run_json", "run.json")
    add_idx("cts_verdicts", "verdicts.json")
    add_idx("cts_manifest", "manifest.json")
    if (out/"manifest.sig").exists():
        add_idx("cts_manifest_sig", "manifest.sig", notes="Signature over manifest.json (high-assurance profiles).")

    # Case-level artifacts
    cases_dir = out/"cases"
    if cases_dir.exists():
        for p in sorted(cases_dir.glob("*.json")):
            add_idx("cts_case_file", str(p.relative_to(out)))

    # Bundle zip is optional; add after creation if present
    if (out/"bundle.zip").exists():
        descriptor["artifacts"]["bundle_zip"] = "bundle.zip"
        add_idx("cts_bundle_zip", "bundle.zip")

    descriptor["artifact_index"] = artifact_index
    (out/"bundle_descriptor.json").write_text(json.dumps(descriptor, indent=2), encoding="utf-8")

    # Add the bundle descriptor itself to the artifact index (and checksum it)
    add_idx("cts_bundle_descriptor", "bundle_descriptor.json")

    # Checksums (machine-readable integrity metadata over key artifacts)
    checksums = []
    for a in artifact_index:
        if a.get("sha256") and a.get("path"):
            checksums.append({"path": a["path"], "sha256": a["sha256"]})
    checksums_obj = {
        "checksums_version": "0.1.0",
        "algorithm": "sha256",
        "generated_by": "trqp-cts",
        "generated_at": now_iso(),
        "entries": sorted(checksums, key=lambda e: e["path"]),
    }
    (out/"checksums.json").write_text(json.dumps(checksums_obj, indent=2), encoding="utf-8")
    add_idx("cts_checksums", "checksums.json")


    print(f"OK: evidence written to {out}")

if __name__ == "__main__":
    main()
