#!/usr/bin/env python3
"""Validate a machine-readable assurance profile against its JSON Schema."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate machine-readable assurance profile")
    ap.add_argument("profile", help="Path to YAML assurance profile")
    ap.add_argument(
        "--schema",
        default=str(Path(__file__).resolve().parent.parent / "schemas" / "machine-readable-assurance-profile.schema.json"),
        help="Path to schema file",
    )
    args = ap.parse_args()

    profile = yaml.safe_load(Path(args.profile).read_text(encoding="utf-8"))
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(profile)
    print(f"valid: {args.profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
