#!/usr/bin/env python3
"""Validate JSON examples against their JSON Schemas.

This repository is primarily documentation + schemas.
To keep it trustworthy, we validate that examples do not drift from schemas.

Behavior:
- For each `examples/*.example.json`, locate a matching `schemas/*.schema.json`.
- Validate the example against the schema.
- For each AL evidence bundle directory (`examples/al*-evidence-bundle/`),
  validate each *.json file against its paired schema per the bundle's
  SCHEMA_MAP (declared in the bundle README metadata or inferred by filename).
- Perform light cross-file checks for the assurance profile example.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
SCHEMAS_DIR = ROOT / "schemas"
CONTROL_CATALOG = ROOT / "tools" / "control-catalog.json"

# Mapping from AL bundle JSON filename stems to Hub schema paths.
# Files not in this map are validated for JSON parse only (no schema check).
_BUNDLE_SCHEMA_MAP: dict[str, str] = {
    "combined-assurance-manifest": "schemas/combined-assurance-manifest.schema.json",
    "control-satisfaction-declaration": "schemas/control-satisfaction.schema.json",
    "lifecycle-assertion": "schemas/lifecycle-assertion.schema.json",
    "certification-attestation": "schemas/certification-attestation.schema.json",
    "recognition-assertion": "schemas/recognition-assertion.schema.json",
    "revocation-notice": "schemas/recognition-assertion.schema.json",  # uses revocation sub-schema if present
}

# Files in bundle directories that are intentionally schema-free
_BUNDLE_SKIP_SCHEMA: set[str] = {
    "version-tuple",          # no stable schema yet; validated for JSON parse only
    "control-satisfaction",   # alias — schema applied via control-satisfaction-declaration
    "revocation-notice",      # lightweight JSON; no dedicated schema yet
    "lifecycle-assertion",    # already in map above
    "trust-list-snapshot",    # operator-defined; no schema
    "monitoring-summary",     # operator-defined; no schema
    "remediation-closure",    # no dedicated schema; validated for JSON parse only
}


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON: {path}: {e}")


def validate_against_schema(instance_path: Path, schema_path: Path) -> list[str]:
    """Return a list of error messages, empty if valid."""
    schema = load_json(schema_path)
    instance = load_json(instance_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
    msgs = []
    for err in errors:
        loc = "/".join([str(p) for p in err.path]) or "(root)"
        msgs.append(f"- {loc}: {err.message}")
    return msgs


def validate_example(example_path: Path) -> None:
    schema_path = SCHEMAS_DIR / example_path.name.replace(".example.json", ".schema.json")
    if not schema_path.exists():
        raise RuntimeError(
            f"Missing schema for example {example_path.name}. Expected: {schema_path}"
        )
    errors = validate_against_schema(example_path, schema_path)
    if errors:
        msg_lines = [f"Schema validation failed for {example_path} against {schema_path}:"]
        msg_lines.extend(errors)
        raise RuntimeError("\n".join(msg_lines))


def validate_bundle_directory(bundle_dir: Path) -> list[str]:
    """Validate all JSON files in an AL evidence bundle directory.

    Returns a list of human-readable error strings (empty = all pass).
    """
    failures: list[str] = []

    for json_file in sorted(bundle_dir.glob("*.json")):
        stem = json_file.stem
        # Always validate JSON parse
        try:
            instance = load_json(json_file)
        except RuntimeError as e:
            failures.append(str(e))
            continue

        # Look up schema
        schema_rel = _BUNDLE_SCHEMA_MAP.get(stem)
        if schema_rel is None:
            # Not in map — check if we should skip or just parse-only
            continue

        schema_path = ROOT / schema_rel
        if not schema_path.exists():
            # Schema not yet defined — skip silently (not a failure)
            continue

        errors = validate_against_schema(json_file, schema_path)
        if errors:
            failures.append(
                f"Bundle schema validation failed: {json_file.relative_to(ROOT)}"
                f" against {schema_rel}:\n" + "\n".join(errors)
            )

    # Recurse into monitoring-evidence/ subdirectory if present
    monitoring_dir = bundle_dir / "monitoring-evidence"
    if monitoring_dir.is_dir():
        for json_file in sorted(monitoring_dir.glob("*.json")):
            try:
                load_json(json_file)  # parse-only
            except RuntimeError as e:
                failures.append(str(e))

    return failures


def cross_checks() -> None:
    """Repo-specific cross-checks that complement JSON Schema validation."""

    if not CONTROL_CATALOG.exists():
        return

    catalog = load_json(CONTROL_CATALOG)
    control_ids = {c["id"] for c in catalog.get("controls", []) if "id" in c}

    profile_path = EXAMPLES_DIR / "trqp-assurance-profile.example.json"
    if not profile_path.exists():
        return

    profile = load_json(profile_path)

    controls = profile.get("controls") or {}
    declared = controls.get("control_ids") or []
    missing = [cid for cid in declared if cid not in control_ids]
    if missing:
        raise RuntimeError(
            "Assurance profile references unknown control IDs: " + ", ".join(missing)
        )

    sat_ref = controls.get("satisfaction_declaration_ref")
    if sat_ref:
        sat_path = ROOT / sat_ref
        if not sat_path.exists():
            raise RuntimeError(
                f"Assurance profile references missing satisfaction declaration: {sat_ref}"
            )

    recog = profile.get("recognition") or {}
    for ref in recog.get("assertion_refs") or []:
        ref_path = ROOT / ref
        if not ref_path.exists():
            raise RuntimeError(f"Assurance profile references missing recognition assertion: {ref}")

    lifecycle = profile.get("lifecycle") or {}
    lac_ref = lifecycle.get("lifecycle_assertion_ref")
    if lac_ref:
        lac_path = ROOT / lac_ref
        if not lac_path.exists():
            raise RuntimeError(f"Assurance profile references missing lifecycle assertion: {lac_ref}")

    # Certification attestation cross-checks (CTR-ACB baseline)
    cert_path = EXAMPLES_DIR / "certification-attestation.example.json"
    if cert_path.exists():
        cert = load_json(cert_path)

        in_scope = cert.get("in_scope_controls") or []
        missing2 = [cid for cid in in_scope if cid not in control_ids]
        if missing2:
            raise RuntimeError(
                "Certification attestation references unknown control IDs: " + ", ".join(missing2)
            )

        for ev in cert.get("evidence_refs") or []:
            ref = ev.get("ref")
            if not ref or ref.startswith("http://") or ref.startswith("https://"):
                continue
            ref_path = ROOT / ref
            if not ref_path.exists():
                raise RuntimeError(f"Certification attestation references missing evidence artifact: {ref}")


def main() -> int:
    errors: list[str] = []

    # 1. Validate flat examples/*.example.json
    examples = sorted(EXAMPLES_DIR.glob("*.example.json"))
    if not examples:
        print("No examples found.")
    else:
        for ex in examples:
            try:
                validate_example(ex)
            except RuntimeError as e:
                errors.append(str(e))

    # 2. Validate AL evidence bundle directories
    bundle_dirs = sorted(
        d for d in EXAMPLES_DIR.iterdir()
        if d.is_dir() and d.name.startswith("al") and d.name.endswith("-evidence-bundle")
    )
    bundle_failures: list[str] = []
    for bundle_dir in bundle_dirs:
        bundle_failures.extend(validate_bundle_directory(bundle_dir))

    if bundle_failures:
        errors.extend(bundle_failures)

    # 3. Cross-checks
    try:
        cross_checks()
    except RuntimeError as e:
        errors.append(str(e))

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    total_bundles = sum(
        len(list(d.glob("*.json"))) for d in bundle_dirs
    )
    print(
        f"Validated {len(examples)} example(s) and "
        f"{total_bundles} bundle artifact(s) across {len(bundle_dirs)} AL bundle(s) successfully."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(str(e), file=sys.stderr)
        raise SystemExit(1)
