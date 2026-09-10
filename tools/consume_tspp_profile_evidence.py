#!/usr/bin/env python3
"""Project TSPP producer-owned posture evidence into profile assurance propositions.

TSPP remains authoritative for control/posture semantics. The Hub validates
applicability and lifecycle state and does not reinterpret producer conclusions.
"""
from __future__ import annotations

TSPP_TO_AYRA = {
    "PROP-AYRA-SIGN-001": "TSPP-AL2-01",
}


def _control_index(evidence: dict) -> dict[str, dict]:
    return {
        item["control_id"]: item
        for item in evidence.get("posture", {}).get("controls", [])
    }


def consume(
    evidence: dict,
    *,
    expected_target_id: str,
    expected_run_id: str,
    proposition_ids: list[str] | None = None,
) -> dict:
    if evidence.get("producer") != "TRQP-TSPP":
        raise ValueError("unexpected TSPP evidence producer")

    if evidence.get("target", {}).get("id") != expected_target_id:
        return {"state": "INDETERMINATE", "reason": "tspp-target-mismatch", "propositions": []}
    if evidence.get("run", {}).get("id") != expected_run_id:
        return {"state": "INDETERMINATE", "reason": "tspp-run-mismatch", "propositions": []}

    reassessment = evidence.get("reassessment", {}).get("state")
    if reassessment != "CURRENT":
        return {
            "state": "INDETERMINATE",
            "reason": f"tspp-evidence-{str(reassessment).lower()}",
            "propositions": [],
        }

    control_set = evidence.get("control_set", {})
    if not control_set.get("id") or not control_set.get("revision"):
        return {"state": "INDETERMINATE", "reason": "tspp-control-set-unbound", "propositions": []}

    selected = proposition_ids or list(TSPP_TO_AYRA)
    index = _control_index(evidence)
    propositions = []
    for proposition_id in selected:
        control_id = TSPP_TO_AYRA[proposition_id]
        observation = index.get(control_id)
        if observation is None:
            result = "INDETERMINATE"
            reason = "tspp-control-evidence-missing"
            refs = []
        else:
            result = observation["result"]
            if result not in {"PASS", "FAIL", "INDETERMINATE", "NOT_APPLICABLE"}:
                raise ValueError(f"unsupported TSPP consumer result: {result}")
            reason = f"TSPP:{control_id}"
            refs = [{"kind": "external", "reference": observation.get("evidence_ref", reason)}]

        propositions.append({
            "proposition_id": proposition_id,
            "requirement_id": "AYRA-SIGN-001",
            "dimension": "security",
            "normative_strength": "SHOULD",
            "applicability": "APPLICABLE",
            "source_authority": "TRQP-TSPP",
            "source_control_id": control_id,
            "result": result,
            "reason": reason,
            "evidence": refs,
        })

    return {"state": "CURRENT", "propositions": propositions}
