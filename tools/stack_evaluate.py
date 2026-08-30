#!/usr/bin/env python3
"""Execute the declared TRQP component validation surfaces from a clean-room workspace."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run_make(path: Path, target: str) -> dict:
    proc = subprocess.run(["make", target], cwd=path, text=True, capture_output=True)
    return {
        "target": target,
        "returncode": proc.returncode,
        "stdout_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr.encode()).hexdigest(),
        "stdout_tail": proc.stdout.splitlines()[-20:] if proc.returncode else [],
        "stderr_tail": proc.stderr.splitlines()[-20:] if proc.returncode else [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".stack-work")
    parser.add_argument("--output", default="artifacts/stack-candidate/run-manifest.json")
    args = parser.parse_args()
    workspace = Path(args.workspace)
    manifest = json.loads((workspace / "bootstrap-manifest.json").read_text(encoding="utf-8"))

    results = {}
    for name in ("tspp", "cts", "assurance_hub"):
        results[name] = run_make(workspace / name, "assurance-check")

    passed = all(result["returncode"] == 0 for result in results.values())
    record = {
        "stack_id": manifest["stack"]["id"],
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "components": manifest["components"],
        "results": results,
        "eligible_component_execution": passed,
        "note": "This run record is candidate evidence and is not a coordinated release declaration."
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    for name, result in results.items():
        status = 'PASS' if result['returncode'] == 0 else 'FAIL'
        print(f"[{status}] {name} assurance-check")
        if result['returncode']:
            for line in result['stdout_tail']:
                print(f"[{name}:stdout] {line}")
            for line in result['stderr_tail']:
                print(f"[{name}:stderr] {line}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
