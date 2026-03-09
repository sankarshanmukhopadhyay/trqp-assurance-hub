#!/usr/bin/env python3
"""Validate Decentralized Directory Protocol (DeDi) artifacts (experimental).

This tool validates DeDi JSON documents against vendored JSON Schemas that ship with the CTS.

Notes:
- Schemas are vendored as a **non-normative snapshot** of the upstream DeDi repo.
- This script provides structural validation only; cryptographic verification remains an operator/auditor concern.
"""

import argparse
import json
from pathlib import Path

from jsonschema import validate as js_validate

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "dedi"

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def validate_json(doc, schema_path: Path):
    schema = load_json(schema_path)
    js_validate(instance=doc, schema=schema)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--public-key", dest="public_key", help="Path to a DeDi public_key JSON document")
    ap.add_argument("--revoke", help="Path to a DeDi revoke JSON document")
    ap.add_argument("--membership", help="Path to a DeDi membership JSON document")
    ap.add_argument("--subscriber", help="Path to a DeDi Beckn_subscriber JSON document")
    args = ap.parse_args()

    if not any([args.public_key, args.revoke, args.membership, args.subscriber]):
        raise SystemExit("Provide at least one of --public-key, --revoke, --membership, --subscriber")

    if args.public_key:
        doc = load_json(Path(args.public_key))
        validate_json(doc, SCHEMAS / "public_key.schema.json")
        print("[OK] DeDi schema: public_key")

    if args.revoke:
        doc = load_json(Path(args.revoke))
        validate_json(doc, SCHEMAS / "revoke.schema.json")
        print("[OK] DeDi schema: revoke")

    if args.membership:
        doc = load_json(Path(args.membership))
        validate_json(doc, SCHEMAS / "membership.schema.json")
        print("[OK] DeDi schema: membership")

    if args.subscriber:
        doc = load_json(Path(args.subscriber))
        validate_json(doc, SCHEMAS / "Beckn_subscriber.schema.json")
        print("[OK] DeDi schema: Beckn_subscriber")

    print("DeDi artifact validation PASSED (experimental).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
