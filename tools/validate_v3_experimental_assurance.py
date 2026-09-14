#!/usr/bin/env python3
"""Validate the pinned experimental TRQP v3 assurance reconciliation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = ROOT / "experimental" / "trqp-v3" / "source-pin.json"
PRODUCERS = ROOT / "experimental" / "trqp-v3" / "producer-pins.json"
EVIDENCE = ROOT / "experimental" / "trqp-v3" / "assurance-evidence.json"

CANDIDATE_SHA = "532a570ed8b7b468b7a317030077577b9859c14f"
AUTHORITY = "DOWNSTREAM_EXPERIMENTAL_NOT_ADOPTED"
CTS_COMMIT = "33465ca0edb27a11fb801baaad348cf6ec159c87"
TSPP_COMMIT = "fc7f15fb81f2bcaaa4d79fd4ac1df09d25572c89"

REQUIRED = {
    "TRQP3-PROP-001", "TRQP3-PROP-002", "TRQP3-MAT-001", "TRQP3-MAT-002",
    "TRQP3-MAT-003", "TRQP3-CTX-001", "TRQP3-LIFE-001", "TRQP3-LIFE-002",
    "TRQP3-LIFE-003", "TRQP3-EVID-001", "TRQP3-EVID-002", "TRQP3-EVID-003",
    "TRQP3-DEC-001", "TRQP3-DEC-002", "TRQP3-REQ-001", "TRQP3-EVAL-001",
    "TRQP3-RESP-001", "TRQP3-NEG-001", "TRQP3-NEG-002", "TRQP3-BIND-001",
    "TRQP3-DISC-001", "TRQP3-DISC-002", "TRQP3-PROF-001", "TRQP3-PROF-002",
    "TRQP3-REC-001", "TRQP3-REC-002", "TRQP3-ERR-001", "TRQP3-SEC-001",
    "TRQP3-SEC-002", "TRQP3-PRIV-001", "TRQP3-AUD-001", "TRQP3-COMP-001",
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def reconcile(cts: str, tspp: str) -> str:
    """Return an assurance state without converting missing/conflicting evidence to PASS."""
    if cts == "PASS" and tspp == "PASS":
        return "SUPPORTED"
    if cts == "FAIL" or tspp == "FAIL":
        return "NOT_SUPPORTED"
    return "INDETERMINATE"


def validate() -> dict:
    pin = load(PIN)
    producers = load(PRODUCERS)
    evidence = load(EVIDENCE)

    if pin.get("commit") != CANDIDATE_SHA or pin.get("authority_status") != AUTHORITY:
        raise AssertionError("candidate source/authority pin changed without reassessment")
    if producers.get("candidate_commit") != CANDIDATE_SHA:
        raise AssertionError("producer evidence is bound to a different candidate")
    if producers.get("authority_status") != AUTHORITY:
        raise AssertionError("producer authority boundary is invalid")

    producer_map = {row["name"]: row for row in producers.get("producers", [])}
    if set(producer_map) != {"cts", "tspp"}:
        raise AssertionError("both CTS and TSPP producer pins are required")
    if producer_map["cts"].get("commit") != CTS_COMMIT:
        raise AssertionError("CTS producer moved; reconciliation is stale")
    if producer_map["tspp"].get("commit") != TSPP_COMMIT:
        raise AssertionError("TSPP producer moved; reconciliation is stale")

    if evidence.get("candidate_commit") != CANDIDATE_SHA:
        raise AssertionError("assurance evidence is not bound to candidate pin")
    if evidence.get("authority_status") != AUTHORITY:
        raise AssertionError("assurance evidence authority boundary is invalid")

    rows = evidence.get("requirements")
    if not isinstance(rows, list) or not rows:
        raise AssertionError("requirement evidence must be a non-empty list")
    ids = {row.get("id") for row in rows}
    if ids != REQUIRED:
        raise AssertionError(
            f"requirement reconciliation drift: missing={sorted(REQUIRED - ids)}, extra={sorted(ids - REQUIRED)}"
        )

    for row in rows:
        expected = reconcile(row.get("cts"), row.get("tspp"))
        if row.get("assurance") != expected:
            raise AssertionError(
                f"{row.get('id')}: assurance {row.get('assurance')} contradicts producer evidence; expected {expected}"
            )

    if not evidence.get("residual_risk"):
        raise AssertionError("experimental assurance must retain residual risk")

    return {
        "candidate_commit": CANDIDATE_SHA,
        "authority_status": AUTHORITY,
        "requirements": len(rows),
        "supported": sum(row["assurance"] == "SUPPORTED" for row in rows),
        "not_supported": sum(row["assurance"] == "NOT_SUPPORTED" for row in rows),
        "indeterminate": sum(row["assurance"] == "INDETERMINATE" for row in rows),
        "status": "PASS",
    }


def main() -> int:
    print(json.dumps(validate(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
