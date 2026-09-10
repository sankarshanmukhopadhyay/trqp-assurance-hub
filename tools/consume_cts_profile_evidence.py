#!/usr/bin/env python3
"""Map CTS profile-consumable evidence into Hub-owned assurance propositions.

CTS remains authoritative for the underlying core/binding conformance result. The
Hub only validates applicability/provenance and projects the result into the
profile proposition model.
"""
from __future__ import annotations

CTS_TO_AYRA = {
    "PROP-AYRA-CORE-001": "TC-AUTHZ-001",
    "PROP-AYRA-CORE-002": "TC-RECOG-001",
}


def _result_index(cts_evidence: dict) -> dict[str, dict]:
    return {item["test_case_id"]: item for item in cts_evidence.get("results", [])}


def consume(cts_evidence: dict, *, expected_protocol_version: str, expected_binding: str,
            proposition_ids: list[str] | None = None) -> dict:
    if cts_evidence.get("producer") != "trqp-conformance-suite":
        raise ValueError("unexpected CTS evidence producer")

    protocol = cts_evidence.get("protocol", {})
    if protocol.get("id") != "trqp" or protocol.get("version") != expected_protocol_version or protocol.get("binding") != expected_binding:
        return {"state": "INDETERMINATE", "reason": "cts-protocol-binding-mismatch", "propositions": []}

    reassessment = cts_evidence.get("reassessment", {}).get("state")
    if reassessment != "CURRENT":
        return {"state": "INDETERMINATE", "reason": f"cts-evidence-{str(reassessment).lower()}", "propositions": []}

    selected = proposition_ids or list(CTS_TO_AYRA)
    index = _result_index(cts_evidence)
    propositions = []
    for proposition_id in selected:
        test_case_id = CTS_TO_AYRA[proposition_id]
        observation = index.get(test_case_id)
        if observation is None:
            result = "INDETERMINATE"
            reason = "cts-test-evidence-missing"
            evidence = []
        else:
            result = observation["result"]
            if result not in {"PASS", "FAIL", "INDETERMINATE", "NOT_APPLICABLE"}:
                raise ValueError(f"unsupported CTS consumer result: {result}")
            reason = f"CTS:{test_case_id}"
            evidence = [{"kind": "external", "reference": observation.get("evidence_ref", reason)}]

        propositions.append({
            "proposition_id": proposition_id,
            "source_authority": "trqp-conformance-suite",
            "source_test_case_id": test_case_id,
            "result": result,
            "reason": reason,
            "evidence": evidence,
        })

    return {"state": "CURRENT", "propositions": propositions}
