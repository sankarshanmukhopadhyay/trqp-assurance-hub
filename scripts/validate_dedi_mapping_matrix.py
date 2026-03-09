#!/usr/bin/env python3
"""Validate DeDi mapping matrix (experimental) for internal consistency.

This checks:
- YAML parses and contains required keys
- Each row references a CTS check id that exists in profiles/dedi_experimental.yaml
- Each row references a schema file that exists in this repo
- Expected evidence is non-empty

This is intentionally light-weight and does not attempt to validate semantics beyond wiring correctness.
"""

import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))

def load_profile_checks(profile_path: Path):
    doc = load_yaml(profile_path)
    checks = doc.get("checks", []) or []
    ids = set()
    for c in checks:
        cid = c.get("id")
        if cid:
            ids.add(cid)
    return ids

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", default="docs/reference/dedi-mapping-matrix.yaml",
                    help="Path to dedi-mapping-matrix.yaml (default: repo doc path)")
    ap.add_argument("--profile", default="profiles/dedi_experimental.yaml",
                    help="Path to DeDi experimental profile yaml (default: repo profile path)")
    args = ap.parse_args()

    matrix_path = (ROOT / args.matrix).resolve()
    profile_path = (ROOT / args.profile).resolve()

    if not matrix_path.exists():
        raise SystemExit(f"Matrix not found: {matrix_path}")
    if not profile_path.exists():
        raise SystemExit(f"Profile not found: {profile_path}")

    matrix = load_yaml(matrix_path)
    required_top = ["id","status","snapshot_date","rows"]
    for k in required_top:
        if k not in matrix:
            raise SystemExit(f"Missing top-level key: {k}")

    check_ids = load_profile_checks(profile_path)
    if not check_ids:
        raise SystemExit("No checks found in dedi_experimental profile")

    rows = matrix.get("rows", []) or []
    if not rows:
        raise SystemExit("Matrix has no rows")

    errors = []
    for i, row in enumerate(rows, start=1):
        for k in ["dedi_artifact","hub_control_objective","cts_check_id","expected_evidence","cts_schema_path"]:
            if k not in row or row[k] in [None,"",[]]:
                errors.append(f"Row {i}: missing/empty '{k}'")
        cid = row.get("cts_check_id")
        if cid and cid not in check_ids:
            errors.append(f"Row {i}: cts_check_id '{cid}' not present in {profile_path.relative_to(ROOT)}")
        sp = row.get("cts_schema_path")
        if sp:
            schema_file = ROOT / sp
            if not schema_file.exists():
                errors.append(f"Row {i}: schema path not found: {sp}")

    if errors:
        for e in errors:
            print("[ERR]", e)
        raise SystemExit(2)

    print("[OK] DeDi mapping matrix wiring is consistent.")
    print(f"Rows: {len(rows)}; Profile checks: {len(check_ids)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
