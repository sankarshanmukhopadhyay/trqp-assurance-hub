#!/usr/bin/env python3
"""Validate required fields in a TRQP Public Assurance Summary."""
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ["summary_version", "target_id", "target", "assurance_level", "overall_status", "conformance_status", "posture_status", "generated_at", "valid_until", "evidence_manifest", "consumer_relevance"]
VALID_STATUS = {"pass", "warn", "fail", "unknown"}
VALID_AL = {"AL1", "AL2", "AL3", "AL4"}

def parse_dt(v):
    return datetime.fromisoformat(v.replace("Z", "+00:00"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", required=True)
    args = ap.parse_args()
    data = json.loads(Path(args.summary).read_text())
    errors = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"missing required field: {key}")
    if data.get("assurance_level") not in VALID_AL:
        errors.append("assurance_level must be AL1, AL2, AL3, or AL4")
    for key in ["overall_status", "conformance_status", "posture_status"]:
        if str(data.get(key, "")).lower() not in VALID_STATUS:
            errors.append(f"{key} has invalid status")
    try:
        if parse_dt(data["valid_until"]) <= parse_dt(data["generated_at"]):
            errors.append("valid_until must be later than generated_at")
    except Exception as exc:
        errors.append(f"invalid generated_at/valid_until timestamp: {exc}")
    cr = data.get("consumer_relevance", {})
    for key in ["plain_language_summary", "what_was_checked", "what_was_not_checked"]:
        if key not in cr:
            errors.append(f"consumer_relevance missing {key}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print("public assurance summary: ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
