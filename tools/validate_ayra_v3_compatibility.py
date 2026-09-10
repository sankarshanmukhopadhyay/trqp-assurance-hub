#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "ayra-v3-compatibility.schema.json"
DEFAULT_MATRIX = ROOT / "profiles" / "ayra" / "v3-compatibility.yaml"


def load_and_validate(path: Path) -> dict:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(document)
    seen = set()
    for mapping in document["mappings"]:
        rid = mapping["ayra_requirement"]
        if rid in seen:
            raise ValueError(f"duplicate mapping: {rid}")
        seen.add(rid)
        if mapping["classification"] == "evidence_gap" and not mapping.get("evidence_gap"):
            raise ValueError(f"evidence gap lacks explanation: {rid}")
    return document


def status_for_revisions(document: dict, *, ayra_revision: str, candidate_revision: str) -> str:
    current = document["current_authority"]["source_revision"]
    candidate = document["candidate_source"]["revision"]
    return "CURRENT" if ayra_revision == current and candidate_revision == candidate else "REASSESSMENT_REQUIRED"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", nargs="?", type=Path, default=DEFAULT_MATRIX)
    args = parser.parse_args()
    document = load_and_validate(args.matrix)
    print(f"valid: {args.matrix} ({len(document['mappings'])} mappings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
