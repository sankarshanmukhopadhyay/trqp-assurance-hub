#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "stack" / "candidates" / "2026.2" / "lifecycle-eligibility.json"
REQUIRED_GATES = {
    "change-event-valid",
    "material-change-detected",
    "non-material-change-bounded",
    "stale-assurance-not-reused",
    "authority-drift-detected",
    "unknown-impact-fails-safe",
    "reassessment-plan-valid",
    "bounded-reassessment-valid",
    "supersession-lineage-complete",
    "post-change-assurance-recomposed",
}


def main():
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    assert data["stack_release"] == "trqp-stack-2026.2"
    assert set(data["gates"]) == REQUIRED_GATES, "release-gate set drifted from Hub #42"

    pending = []
    for name, gate in data["gates"].items():
        status = gate.get("status")
        assert status in {"proven", "pending"}, f"unsupported gate status: {name}={status}"
        if status == "proven":
            assert gate.get("evidence"), f"proven gate lacks evidence: {name}"
            for ref in gate["evidence"]:
                if ref.startswith("artifacts/") or ref.startswith("scripts/") or ref.startswith("tools/"):
                    assert (ROOT / ref).exists(), f"missing local gate evidence: {name}: {ref}"
        else:
            pending.append(name)
            assert gate.get("reason"), f"pending gate lacks reason: {name}"

    frozen = data["candidate_tuple"].get("frozen") is True
    expected_eligible = frozen and not pending
    assert data["release_eligible"] is expected_eligible, "release_eligible contradicts evidence/freeze state"
    assert data["judgment"]["workflow_green_is_release_green"] is False

    if expected_eligible:
        assert data["judgment"]["current"] == "RELEASE_ELIGIBLE"
    else:
        assert data["judgment"]["current"] == "NOT_RELEASE_ELIGIBLE"

    print(f"TRQP Stack 2026.2 lifecycle eligibility ledger: PASS; pending={','.join(pending) or 'none'}; tuple_frozen={frozen}; release_eligible={expected_eligible}")


if __name__ == "__main__":
    main()
