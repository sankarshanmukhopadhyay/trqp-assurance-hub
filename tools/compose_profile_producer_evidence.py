#!/usr/bin/env python3
"""Compose producer-owned evidence into a profile assessment without changing ownership."""
from __future__ import annotations

from copy import deepcopy

from tools.consume_cts_profile_evidence import consume
from tools.profile_assurance_model import aggregate


def compose_cts_core(assessment: dict, cts_evidence: dict, *, protocol_version: str = "2.0", binding: str = "https-json") -> dict:
    """Replace only CTS-owned Ayra core proposition observations.

    Profile/extension/operational/authority propositions remain untouched. If CTS
    evidence is stale or incompatible, the mapped core propositions become
    INDETERMINATE rather than falling back to duplicate local observations.
    """
    result = deepcopy(assessment)
    mapped_ids = ["PROP-AYRA-CORE-001", "PROP-AYRA-CORE-002"]
    consumed = consume(
        cts_evidence,
        expected_protocol_version=protocol_version,
        expected_binding=binding,
        proposition_ids=mapped_ids,
    )

    by_id = {item["proposition_id"]: item for item in consumed.get("propositions", [])}
    for proposition in result.get("propositions", []):
        pid = proposition.get("proposition_id")
        if pid not in mapped_ids:
            continue
        source = by_id.get(pid)
        if source is None:
            proposition["result"] = "INDETERMINATE"
            proposition["evidence"] = []
            proposition["reason"] = consumed.get("reason", "cts-evidence-unavailable")
            proposition["evidence_authority"] = "trqp-conformance-suite"
            continue
        proposition["result"] = source["result"]
        proposition["evidence"] = source["evidence"]
        proposition["reason"] = source["reason"]
        proposition["evidence_authority"] = source["source_authority"]
        proposition["source_test_case_id"] = source["source_test_case_id"]

    result.update(aggregate(result.get("propositions", [])))
    result["producer_evidence"] = {
        "cts": {
            "state": consumed["state"],
            "suite_version": cts_evidence.get("suite_version"),
            "test_set": cts_evidence.get("test_set"),
            "run": cts_evidence.get("run"),
            "target": cts_evidence.get("target"),
            "reassessment": cts_evidence.get("reassessment"),
        }
    }
    return result
