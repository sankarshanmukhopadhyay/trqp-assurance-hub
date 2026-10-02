#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from cts_determinism import DeterminismEvidenceError, assurance_projection, load_and_validate


def load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def producer_status(report: dict) -> str:
    summary = report.get("summary", {})
    fails = int(summary.get("FAIL", 0) or 0)
    passes = int(summary.get("PASS", 0) or 0)
    if fails > 0:
        return "fail"
    if passes > 0:
        return "pass"
    return "indeterminate"


def require_verified_state(report: dict, producer: str) -> dict:
    state = report.get("target_state")
    if not isinstance(state, dict):
        raise SystemExit(f"fail-closed: {producer} target_state missing")
    if state.get("status") != "verified":
        raise SystemExit(f"fail-closed: {producer} target_state not verified")
    if state.get("algorithm") != "sha256":
        raise SystemExit(f"fail-closed: {producer} target_state algorithm unsupported")
    digest = state.get("digest")
    identity = state.get("identity")
    if not isinstance(digest, str) or len(digest) != 64:
        raise SystemExit(f"fail-closed: {producer} target_state digest invalid")
    if identity != f"sha256:{digest}":
        raise SystemExit(f"fail-closed: {producer} target_state identity inconsistent")
    return state


def report_version(report: dict, producer: str) -> str | None:
    if producer == "cts":
        tool = report.get("tool")
        if isinstance(tool, dict) and tool.get("version"):
            return str(tool["version"])
        return report.get("suite_version")
    return report.get("tool_version")


def require_state_pair(cts: dict, tspp: dict) -> dict:
    cts_state = require_state_pair(cts, tspp)
    return cts_state


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cts-report", required=True)
    ap.add_argument("--cts-determinism-report", required=True)
    ap.add_argument("--tspp-report", required=True)
    ap.add_argument("--component-tuple", default="state-bound-2026-10")
    ap.add_argument("--out", default="artifacts/state-bound-assurance")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    registry = yaml.safe_load((root / "data/component-compatibility.yaml").read_text(encoding="utf-8"))
    component = next(
        (
            item
            for item in registry.get("component_tuples", [])
            if item.get("id") == args.component_tuple and item.get("status") == "supported-development"
        ),
        None,
    )
    if component is None:
        raise SystemExit("fail-closed: unsupported development component tuple")
    if not component.get("requires", {}).get("target_state_identity"):
        raise SystemExit("fail-closed: component tuple does not require target-state identity")

    cts_path = Path(args.cts_report)
    tspp_path = Path(args.tspp_report)
    det_path = Path(args.cts_determinism_report)
    cts = load_json(args.cts_report)
    tspp = load_json(args.tspp_report)

    if cts.get("run_id") != tspp.get("run_id"):
        raise SystemExit("fail-closed: run_id mismatch")
    if cts.get("target_id") != tspp.get("target_id"):
        raise SystemExit("fail-closed: target_id mismatch")

    cts_version = report_version(cts, "cts")
    tspp_version = report_version(tspp, "tspp")
    if cts_version != component.get("conformance_suite"):
        raise SystemExit(
            f"fail-closed: CTS version {cts_version!r} does not match tuple {component.get('conformance_suite')!r}"
        )
    if tspp_version != component.get("tspp"):
        raise SystemExit(
            f"fail-closed: TSPP version {tspp_version!r} does not match tuple {component.get('tspp')!r}"
        )

    cts_state = require_verified_state(cts, "CTS")
    tspp_state = require_verified_state(tspp, "TSPP")
    if cts_state["digest"] != tspp_state["digest"]:
        raise SystemExit(
            f"fail-closed: target_state.digest mismatch: {cts_state['digest']!r} != {tspp_state['digest']!r}"
        )

    try:
        det_raw = load_and_validate(args.cts_determinism_report)
    except DeterminismEvidenceError as exc:
        raise SystemExit(f"fail-closed: {exc}") from exc
    det = assurance_projection(det_raw)

    source_state = det_raw.get("source", {}).get("target_state")
    replay_state = det_raw.get("replay", {}).get("target_state")
    if not isinstance(source_state, dict) or not isinstance(replay_state, dict):
        raise SystemExit("fail-closed: CTS replay determinism target-state evidence missing")
    if source_state.get("digest") != cts_state["digest"] or replay_state.get("digest") != cts_state["digest"]:
        raise SystemExit("fail-closed: CTS replay target state does not match conformance target state")

    cs = producer_status(cts)
    ts = producer_status(tspp)
    outcome = "fail" if "fail" in (cs, ts) else ("pass" if cs == ts == "pass" else "indeterminate")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    artifacts = [
        {"role": "cts", "path": str(cts_path), "sha256": file_sha256(cts_path)},
        {"role": "tspp", "path": str(tspp_path), "sha256": file_sha256(tspp_path)},
        {"role": "cts_replay_determinism", "path": str(det_path), "sha256": file_sha256(det_path)},
    ]

    manifest = {
        "schema_version": "1.0",
        "component_tuple": component,
        "run_id": cts["run_id"],
        "target_id": cts["target_id"],
        "target_state": cts_state,
        "producer_results": {"cts": cs, "tspp": ts, "cts_replay_determinism": "pass"},
        "cts_replay_determinism": det,
        "artifacts": artifacts,
    }

    decision = {
        "schema_version": "1.0",
        "decision_id": f"state-bound:{cts['run_id']}",
        "outcome": outcome,
        "scope": "State-bound TRQP conformance, replay reproducibility, and TSPP posture composition",
        "target": cts["target_id"],
        "target_state": cts_state["identity"],
        "evidence_considered": artifacts,
        "conditions": ["CTS and TSPP evidence are bound to the same verified SHA-256 target state."],
        "limitations": [
            "This is a supported component-development tuple, not a coordinated TRQP Stack release.",
            "Self-generated repository evidence is not external certification.",
        ],
        "findings": [],
        "issued_at": "2026-10-02T00:00:00Z",
        "expires_at": None,
        "supersedes": None,
        "revoked": False,
        "revocation_reason": None,
    }

    Draft202012Validator(
        json.loads((root / "schemas/assurance-decision.schema.json").read_text(encoding="utf-8"))
    ).validate(decision)

    trace = {
        "run_id": cts["run_id"],
        "target_id": cts["target_id"],
        "target_state": cts_state,
        "chain": [
            "CTS conformance evidence",
            "CTS target-state identity",
            "CTS replay determinism",
            "TSPP posture evidence",
            "TSPP target-state identity",
            "Hub state-bound composition",
        ],
        "authority": {
            "conformance_and_replay": "trqp-conformance-suite",
            "posture_and_reassessment": "TRQP-TSPP",
            "cross_producer_composition": "trqp-assurance-hub",
        },
    }

    (out / "state-bound-assurance-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (out / "assurance-decision.json").write_text(json.dumps(decision, indent=2) + "\n")
    (out / "traceability-report.json").write_text(json.dumps(trace, indent=2) + "\n")
    print(f"state-bound assurance: {outcome}; target_state={cts_state['identity']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
