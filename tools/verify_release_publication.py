#!/usr/bin/env python3
"""Verify GitHub eligibility evidence and human publication decision before release.

The gate registry is independent of each release instance. This verifier proves
the recorded GitHub run actually executed and completed the required named steps.
It does not claim independent certification or authenticate a live deployment.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def verify(manifest: dict, run: dict, jobs: dict, comment: dict, registry: dict) -> list[str]:
    errors = []
    coord = manifest.get("coordinator", {})
    evidence = manifest.get("eligibility_evidence", {})
    expected_run = evidence.get("workflow_run_id")
    expected_commit = coord.get("validated_main_commit")
    expected_path = ".github/workflows/stack-release-eligibility.yml"
    if run.get("id") != expected_run:
        errors.append("eligibility run id does not match immutable manifest")
    if run.get("head_sha") != expected_commit:
        errors.append("eligibility run SHA does not match validated main commit")
    if run.get("path") != expected_path or evidence.get("workflow") != "stack-release-eligibility":
        errors.append("eligibility workflow path is not authoritative")
    if run.get("head_branch") != "main" or run.get("conclusion") != "success":
        errors.append("eligibility run was not successful on main")
    if evidence.get("workflow_conclusion") != "success":
        errors.append("manifest does not record a successful eligibility result")

    expected_comment_id = coord.get("human_release_judgment_comment_id")
    if comment.get("id") != expected_comment_id:
        errors.append("human judgment comment id mismatch")
    owner = coord.get("repository", "").split("/")[0]
    if comment.get("user", {}).get("login") != owner:
        errors.append("human judgment author does not match designated repository owner")
    if not comment.get("created_at") or comment.get("updated_at") != comment.get("created_at"):
        errors.append("human judgment has no immutable captured version or was edited")
    body = comment.get("body") or ""
    for required in ("Human release judgment: ACCEPT", str(expected_run),
                     str(expected_commit), str(evidence.get("artifact_digest")),
                     str(manifest.get("stack", {}).get("id"))):
        if required not in body:
            errors.append("human judgment does not bind accepted release evidence: " + required)

    decisive = [job for job in jobs.get("jobs", [])
                if job.get("name") == "decisive-test" and job.get("conclusion") == "success"]
    if len(decisive) != 1:
        errors.append("exactly one successful decisive-test job is required")
    else:
        step_status = {step.get("name"): step.get("conclusion")
                       for step in decisive[0].get("steps", [])}
        for gate in manifest.get("release_gates", []):
            mapping = registry.get("gates", {}).get(gate)
            if not mapping:
                errors.append("unmapped release gate: " + gate)
                continue
            step = mapping["check_step"]
            if step_status.get(step) != "success":
                errors.append(f"gate {gate} has no successful execution step: {step}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    for arg in ("manifest", "run", "jobs", "comment"):
        parser.add_argument("--" + arg, type=Path, required=True)
    parser.add_argument("--registry", type=Path,
                        default=Path("stack/schema/release-gates.json"))
    args = parser.parse_args()
    load = lambda p: json.loads(p.read_text(encoding="utf-8"))
    errors = verify(load(args.manifest), load(args.run), load(args.jobs),
                    load(args.comment), load(args.registry))
    if errors:
        for item in errors:
            print("fail-closed:", item)
        return 1
    print("Release provenance: immutable eligibility run, executed gates and human judgment verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
