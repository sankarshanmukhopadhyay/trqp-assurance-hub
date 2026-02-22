#!/usr/bin/env python3
"""Validate JSON examples against their JSON Schemas.

This repository is primarily documentation + schemas.
To keep it trustworthy, we validate that examples do not drift from schemas.

Behavior:
- For each `examples/*.example.json`, locate a matching `schemas/*.schema.json`.
- Validate the example against the schema.
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


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON: {path}: {e}")


def validate_example(example_path: Path) -> None:
    schema_path = SCHEMAS_DIR / example_path.name.replace(".example.json", ".schema.json")
    if not schema_path.exists():
        raise RuntimeError(
            f"Missing schema for example {example_path.name}. Expected: {schema_path}"
        )

    schema = load_json(schema_path)
    instance = load_json(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
    if errors:
        msg_lines = [f"Schema validation failed for {example_path} against {schema_path}:"]
        for err in errors:
            loc = "/".join([str(p) for p in err.path]) or "(root)"
            msg_lines.append(f"- {loc}: {err.message}")
        raise RuntimeError("\n".join(msg_lines))


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


def main() -> int:
    examples = sorted(EXAMPLES_DIR.glob("*.example.json"))
    if not examples:
        print("No examples found.")
        return 0

    for ex in examples:
        validate_example(ex)

    cross_checks()

    print(f"Validated {len(examples)} example(s) successfully.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(str(e), file=sys.stderr)
        raise SystemExit(1)
