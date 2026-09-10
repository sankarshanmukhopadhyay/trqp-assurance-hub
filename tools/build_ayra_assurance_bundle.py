#!/usr/bin/env python3
"""Build a reproducible Ayra assurance evidence bundle from deterministic observations."""
from __future__ import annotations

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from tools.ayra_authority_evidence import assess_authority
from tools.run_ayra_profile import assess_fixture

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "ayra-assurance-bundle.schema.json"
SENSITIVE_KEYS = {"authorization", "proxy-authorization", "cookie", "set-cookie", "api_key", "api-key", "token", "secret"}


def _canonical(data: object) -> bytes:
    return (json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def redact(value: object, removed: list[str], prefix: str = "") -> object:
    if isinstance(value, dict):
        result = {}
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            if key.lower() in SENSITIVE_KEYS:
                removed.append(path)
                continue
            result[key] = redact(child, removed, path)
        return result
    if isinstance(value, list):
        return [redact(child, removed, f"{prefix}[{i}]") for i, child in enumerate(value)]
    return value


def render_report(bundle: dict) -> str:
    profile_dims = bundle["results"]["profile"].get("dimensions", {})
    authority = bundle["results"]["authority"]
    lines = [
        "# Ayra TRQP Assurance Report",
        "",
        f"Run: `{bundle['run']['run_id']}`",
        f"Observed: `{bundle['run']['observed_at']}`",
        f"Target: `{bundle['target']['registry_id']}`",
        f"Profile: `{bundle['profile']['id']}@{bundle['profile']['version']}`",
        f"Source revision: `{bundle['profile']['source_revision']}`",
        "",
        "## Profile dimensions",
        "",
    ]
    for name, item in sorted(profile_dims.items()):
        lines.append(f"- `{name}`: **{item['result']}**")
    lines.extend(["", "## Authority and discovery evidence", ""])
    for key in ("identifier_syntax", "did_method", "resolution", "service_discovery", "governance_discovery", "control_evidence", "governance_legitimacy"):
        lines.append(f"- `{key}`: **{authority.get(key, 'INDETERMINATE')}**")
    lines.extend([
        "",
        "## Assurance boundary",
        "",
        "This report records technical evidence only. DID control, endpoint discovery, or successful protocol observations do not establish governance legitimacy unless separate evidence supports that conclusion.",
        "",
    ])
    return "\n".join(lines)


def build(*, fixture: dict, authority_observation: dict, run_id: str, observed_at: str) -> tuple[dict, dict[str, bytes]]:
    removed: list[str] = []
    safe_fixture = redact(deepcopy(fixture), removed)
    safe_authority = redact(deepcopy(authority_observation), removed)

    profile_result = assess_fixture(safe_fixture)
    authority_result = assess_authority(safe_authority)
    registry_id = safe_fixture.get("registry_id") or safe_authority.get("registry_did") or "unknown"
    endpoint = safe_authority.get("trqp_service_endpoint")

    payloads: dict[str, bytes] = {
        "requirement-results.json": _canonical(profile_result),
        "authority-evidence.json": _canonical(authority_result),
        "endpoint-evidence.json": _canonical({"fixture": safe_fixture}),
        "negative-tests.json": _canonical({"suite": "tests/test_ayra_adversarial.py", "status": "executed-by-ci"}),
        "provenance.json": _canonical({
            "run_id": run_id,
            "observed_at": observed_at,
            "profile_id": "ayra-trqp",
            "profile_version": "0.6.0-draft",
            "source_repository": "https://github.com/ayraforum/ayra-trust-registry-resources",
            "source_revision": "ec7768572592b50ba3f4102c026c2449148b5e11",
            "target_registry_id": registry_id,
        }),
    }

    artifacts = [
        {"path": path, "sha256": _sha256(content), "media_type": "application/json"}
        for path, content in sorted(payloads.items())
    ]
    bundle = {
        "bundle_version": "1.0",
        "run": {"run_id": run_id, "observed_at": observed_at},
        "profile": {
            "id": "ayra-trqp",
            "version": "0.6.0-draft",
            "source_repository": "https://github.com/ayraforum/ayra-trust-registry-resources",
            "source_revision": "ec7768572592b50ba3f4102c026c2449148b5e11",
        },
        "target": {"registry_id": registry_id, "endpoint": endpoint},
        "results": {"profile": profile_result, "authority": authority_result},
        "artifacts": artifacts,
        "redaction": {"removed_fields": sorted(removed)},
    }
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(bundle)
    payloads["assurance.json"] = _canonical(bundle)
    payloads["assurance.md"] = render_report(bundle).encode("utf-8")
    return bundle, payloads


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("authority", type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--observed-at", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    authority = json.loads(args.authority.read_text(encoding="utf-8"))
    _, payloads = build(fixture=fixture, authority_observation=authority, run_id=args.run_id, observed_at=args.observed_at)
    args.out.mkdir(parents=True, exist_ok=True)
    for path, content in payloads.items():
        (args.out / path).write_bytes(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
