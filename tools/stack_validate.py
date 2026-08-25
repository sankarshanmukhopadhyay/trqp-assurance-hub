#!/usr/bin/env python3
"""Validate a coordinated TRQP stack candidate manifest and release eligibility evidence."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

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
    if not REQUIRED_AUTHORITIES.issubset(doc.get("authorities", {})): errors.append("tsmm and tis authorities are required")
    gates = set(doc.get("release_gates", []))
    missing = REQUIRED_GATES - gates
    if missing: errors.append("missing release gates: " + ", ".join(sorted(missing)))
    return errors


def verify_remote_refs(doc: dict) -> list[str]:
    errors: list[str] = []
    for name, component in doc["components"].items():
        url = f"https://github.com/{component['repository']}.git"
        ref = f"refs/tags/{component['ref']}^{{}}"
        fallback = f"refs/tags/{component['ref']}"
        proc = subprocess.run(["git", "ls-remote", url, ref, fallback], capture_output=True, text=True)
        if proc.returncode != 0 or not proc.stdout.strip():
            errors.append(f"{name}: unable to resolve {component['ref']}")
            continue
        resolved = [line.split()[0] for line in proc.stdout.splitlines() if line.strip()]
        if component["commit"] not in resolved:
            errors.append(f"{name}: tag does not resolve to declared commit")
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
    if args.check_remote: print("[PASS] tagged component commits match manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
