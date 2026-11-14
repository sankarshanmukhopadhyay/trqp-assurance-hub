#!/usr/bin/env python3
"""Validate a coordinated TRQP stack candidate manifest and release eligibility evidence."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_SCHEMA = ROOT / "stack/schema/release-manifest.schema.json"
GATE_REGISTRY = ROOT / "stack/schema/release-gates.json"

def _gate_registry() -> dict:
    return json.loads(GATE_REGISTRY.read_text(encoding="utf-8"))

REQUIRED_COMPONENTS = {"tspp", "cts", "assurance_hub"}
REQUIRED_AUTHORITIES = {"tsmm", "tis"}
REQUIRED_GATES = {
    "release-tuple-resolves", "tagged-commits-match", "clean-bootstrap",
    "canonical-evaluation", "tspp-evidence-valid", "cts-evidence-valid",
    "cts-replay-deterministic", "combined-assurance-valid", "run-target-correlation",
    "provenance-complete", "artifact-integrity-valid", "negative-cases-fail-closed",
    "full-stack-replay-equivalent", "walkthrough-executable"
}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
VERSION = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_structure(doc: dict) -> list[str]:
    errors: list[str] = []
    if doc.get("schema_version") != "1.0": errors.append("schema_version must be 1.0")
    stack = doc.get("stack", {})
    if stack.get("status") not in {"candidate", "validated", "revoked", "superseded"}: errors.append("invalid stack status")
    components = doc.get("components", {})
    if set(components) != REQUIRED_COMPONENTS: errors.append("components must be exactly tspp, cts, assurance_hub")
    for name, component in components.items():
        if not component.get("repository"): errors.append(f"{name}: repository missing")
        if not str(component.get("ref", "")).startswith("v"): errors.append(f"{name}: immutable version tag required")
        if not SHA40.match(str(component.get("commit", ""))): errors.append(f"{name}: 40-character commit SHA required")

    authorities = doc.get("authorities", {})
    if not REQUIRED_AUTHORITIES.issubset(authorities):
        errors.append("tsmm and tis authorities are required")
    else:
        for name in sorted(REQUIRED_AUTHORITIES):
            authority = authorities[name]
            if not authority.get("repository"): errors.append(f"{name}: authority repository missing")
            historical_without_strict_pins = stack.get("id") in {
                "trqp-stack-2026.1", "trqp-stack-2026.2"
            }
            if not historical_without_strict_pins or authority.get("version"):
                if not VERSION.match(str(authority.get("version", ""))):
                    errors.append(f"{name}: semantic version required")
            if not historical_without_strict_pins or authority.get("commit"):
                if not SHA40.match(str(authority.get("commit", ""))):
                    errors.append(f"{name}: 40-character authority commit SHA required")

    for issue in Draft202012Validator(load(MANIFEST_SCHEMA)).iter_errors(doc):
        errors.append("release manifest schema: " + issue.message)
    registry = _gate_registry()
    gates = set(doc.get("release_gates", []))
    required = REQUIRED_GATES.copy()
    if stack.get("status") == "validated":
        required = set(registry["release_minimums"].get(stack.get("id"), []))
        if not required:
            errors.append("validated release has no independently registered gate baseline")
    missing = required - gates
    if missing: errors.append("missing release gates: " + ", ".join(sorted(missing)))
    unknown = gates - set(registry["gates"])
    if unknown: errors.append("unmapped release gates: " + ", ".join(sorted(unknown)))
    for gate in gates & set(registry["gates"]):
        entry = registry["gates"][gate]
        if not entry.get("check_step") or not entry.get("evidence_source"):
            errors.append(f"gate {gate} lacks executable/evidence mapping")
    return errors


def _remote_tag(repository: str, ref: str) -> list[str]:
    url = f"https://github.com/{repository}.git"
    proc = subprocess.run(
        ["git", "ls-remote", url, f"refs/tags/{ref}^{{}}", f"refs/tags/{ref}"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return []
    return [line.split()[0] for line in proc.stdout.splitlines() if line.strip()]


def _commit_exists(repository: str, commit: str) -> bool:
    """Prove a public repository can fetch the exact declared authority commit."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        init = subprocess.run(["git", "init", "--quiet", tmp], capture_output=True, text=True)
        if init.returncode != 0:
            return False
        remote = subprocess.run(
            ["git", "-C", tmp, "remote", "add", "origin", f"https://github.com/{repository}.git"],
            capture_output=True,
            text=True,
        )
        if remote.returncode != 0:
            return False
        fetch = subprocess.run(
            ["git", "-C", tmp, "fetch", "--quiet", "--depth", "1", "origin", commit],
            capture_output=True,
            text=True,
        )
        if fetch.returncode != 0:
            return False
        actual = subprocess.run(
            ["git", "-C", tmp, "rev-parse", "FETCH_HEAD"],
            capture_output=True,
            text=True,
        )
        return actual.returncode == 0 and actual.stdout.strip() == commit


def verify_remote_refs(doc: dict) -> list[str]:
    errors: list[str] = []
    for name, component in doc["components"].items():
        resolved = _remote_tag(component["repository"], component["ref"])
        if not resolved:
            errors.append(f"{name}: unable to resolve {component['ref']}")
        elif component["commit"] not in resolved:
            errors.append(f"{name}: tag does not resolve to declared commit")

    for name, authority in doc["authorities"].items():
        commit = authority.get("commit")
        if not commit:
            continue
        if not _commit_exists(authority["repository"], commit):
            errors.append(f"{name}: declared authority commit is not fetchable")
            continue
        ref = authority.get("ref")
        if ref:
            resolved = _remote_tag(authority["repository"], ref)
            if not resolved:
                errors.append(f"{name}: unable to resolve authority ref {ref}")
            elif commit not in resolved:
                errors.append(f"{name}: authority ref does not resolve to declared commit")
        version = authority.get("version")
        if version:
            import urllib.request
            raw = f"https://raw.githubusercontent.com/{authority['repository']}/{commit}/VERSION"
            try:
                with urllib.request.urlopen(raw, timeout=15) as response:
                    observed = response.read(256).decode("utf-8").strip()
            except Exception:
                errors.append(f"{name}: declared VERSION at authority commit is unavailable")
            else:
                if observed != version:
                    errors.append(f"{name}: declared VERSION {version!r} differs from pinned source {observed!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", default="stack/releases/candidate/manifest.json")
    parser.add_argument("--check-remote", action="store_true")
    args = parser.parse_args()
    doc = load(Path(args.manifest))
    errors = validate_structure(doc)
    if args.check_remote and not errors:
        errors.extend(verify_remote_refs(doc))
    if errors:
        for error in errors: print(f"[FAIL] {error}")
        return 1
    print("[PASS] coordinated stack manifest is structurally valid")
    if args.check_remote: print("[PASS] tagged components and authority version commits match manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
