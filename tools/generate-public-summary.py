#!/usr/bin/env python3
"""Generate a public assurance summary from a Combined Assurance Manifest."""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def norm_status(value):
    value = str(value or "unknown").lower()
    return value if value in {"pass", "warn", "fail", "unknown"} else "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--valid-days", type=int, default=30)
    ap.add_argument("--concerns", default="mailto:trust-ops@example.org")
    args = ap.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    build = manifest.get("build", {})
    summary = manifest.get("summary", {})
    tools = manifest.get("tools", {})
    generated_at = manifest.get("generated_at") or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    try:
        dt = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError:
        dt = datetime.now(timezone.utc).replace(microsecond=0)
    valid_until = (dt + timedelta(days=args.valid_days)).isoformat().replace("+00:00", "Z")

    out = {
        "summary_version": "0.1.0",
        "target_id": build.get("target_id", "unknown-target"),
        "target": build.get("target", "unknown"),
        "assurance_level": summary.get("assurance_tier") or tools.get("trqp_tspp", {}).get("assurance_level", "AL1"),
        "overall_status": norm_status(summary.get("overall_status")),
        "conformance_status": norm_status(summary.get("conformance_status")),
        "posture_status": norm_status(summary.get("tspp_status") or summary.get("posture_status")),
        "generated_at": generated_at,
        "valid_until": valid_until,
        "evidence_manifest": Path(args.manifest).name,
        "limitations": ["This summary does not replace legal, financial, or ecosystem-specific due diligence."],
        "consumer_relevance": {
            "plain_language_summary": "The registry has machine-verifiable evidence for protocol conformance and security posture. Relying parties should check freshness and limitations before use.",
            "what_was_checked": ["protocol behavior", "security posture", "freshness expectations", "evidence integrity"],
            "what_was_not_checked": ["legal liability", "business solvency", "all ecosystem-specific governance rules"],
            "where_to_raise_concerns": args.concerns
        }
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
