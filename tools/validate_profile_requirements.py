#!/usr/bin/env python3
"""Validate a profile requirement catalogue and repository-local invariants."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "trqp-profile-requirements.schema.json"


def validate(path: Path) -> dict:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(document)
    ids = [item["id"] for item in document["requirements"]]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        raise ValueError(f"duplicate requirement ids: {', '.join(duplicates)}")
    for item in document["requirements"]:
        if item["strength"] == "MAY" and item.get("applicability") is None:
            raise ValueError(f"optional requirement lacks applicability: {item['id']}")
    return document


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalogue", nargs="?", default=str(ROOT / "profiles" / "ayra" / "requirements.yaml"))
    args = parser.parse_args()
    document = validate(Path(args.catalogue))
    print(f"valid: {args.catalogue} ({len(document['requirements'])} requirements)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
