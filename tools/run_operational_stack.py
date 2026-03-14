#!/usr/bin/env python3
"""Create a portable Operational Stack artifact set from CTS and TSPP reports."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def copy_into(src: Path, dst: Path) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return str(dst)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build an Operational Stack artifact directory.")
    p.add_argument("--cts-report", required=True)
    p.add_argument("--tspp-report", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--build-id", required=True)
    p.add_argument("--target-id", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--out", default="artifacts/operational-stack")
    args = p.parse_args(argv)

    repo_root = Path(__file__).resolve().parent.parent
    out = (repo_root / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    cts_src = Path(args.cts_report).resolve()
    tspp_src = Path(args.tspp_report).resolve()

    cts_dst = out / "conformance" / "cts-report.json"
    tspp_dst = out / "posture" / "tspp-report.json"
    copy_into(cts_src, cts_dst)
    copy_into(tspp_src, tspp_dst)

    metadata = {
        "run_id": args.run_id,
        "target_id": args.target_id,
        "target": args.target,
        "build_id": args.build_id,
        "artifacts": {
            "cts_report": str(cts_dst.relative_to(out)),
            "tspp_report": str(tspp_dst.relative_to(out)),
        },
    }
    metadata_path = out / "metadata" / "stack-run.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    manifest_path = out / "combined-assurance-manifest.json"
    cmd = [
        sys.executable,
        str(repo_root / "tools" / "generate-manifest.py"),
        "--build-id", args.build_id,
        "--target", args.target,
        "--run-id", args.run_id,
        "--target-id", args.target_id,
        "--cts-report", str(cts_dst),
        "--tspp-report", str(tspp_dst),
        "--artifact", "conformance_report:conformance/cts-report.json:trqp_conformance_suite:application/json:cts-report-v0",
        "--artifact", "posture_report:posture/tspp-report.json:trqp_tspp:application/json:tspp-report-v0",
        "--artifact", "stack_run_metadata:metadata/stack-run.json:trqp_assurance_hub:application/json:operational-stack-run-v0",
        "--base-dir", str(out),
        "--schema", str(repo_root / "schemas" / "combined-assurance-manifest.schema.json"),
        "--out", str(manifest_path),
    ]
    subprocess.check_call(cmd)
    print(f"Operational Stack artifacts written to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
