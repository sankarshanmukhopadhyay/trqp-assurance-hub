#!/usr/bin/env python3
"""Compose producer-owned evidence into profile assessment without changing ownership."""
from __future__ import annotations

from copy import deepcopy

from tools.consume_cts_profile_evidence import consume as consume_cts
from tools.consume_tspp_profile_evidence import consume as consume_tspp
from tools.profile_assurance_model import aggregate


def compose_cts_core(assessment: dict, cts_evidence: dict, *, protocol_version: str = "2.0", binding: str = "https-json") -> dict:
    """Replace only CTS-owned Ayra core proposition observations."""
    result = deepcopy(assessment)
    mapped_ids = ["PROP-AYRA-CORE-001", "PROP-AYRA-CORE-002"]
    consumed = consume_cts(
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
    result.setdefault("producer_evidence", {})["cts"] = {
        "state": consumed["state"],
        "suite_version": cts_evidence.get("suite_version"),
        "test_set": cts_evidence.get("test_set"),
        "run": cts_evidence.get("run"),
        "target": cts_evidence.get("target"),
        "reassessment": cts_evidence.get("reassessment"),
    }
    return result


def compose_tspp_security(assessment: dict, tspp_evidence: dict, *, target_id: str, run_id: str) -> dict:
    """Add/replace only TSPP-owned security posture propositions."""
    result = deepcopy(assessment)
    mapped_ids = ["PROP-AYRA-SIGN-001"]
    consumed = consume_tspp(
        tspp_evidence,
        expected_target_id=target_id,
        expected_run_id=run_id,
        proposition_ids=mapped_ids,
    )
    by_id = {item["proposition_id"]: item for item in consumed.get("propositions", [])}
    propositions = result.setdefault("propositions", [])
    existing = {item.get("proposition_id"): item for item in propositions}

    for pid in mapped_ids:
        source = by_id.get(pid)
        if source is None:
            replacement = {
                "proposition_id": pid,
                "requirement_id": "AYRA-SIGN-001",
                "dimension": "security",
                "normative_strength": "SHOULD",
                "applicability": "APPLICABLE",
                "result": "INDETERMINATE",
                "evidence": [],
                "reason": consumed.get("reason", "tspp-evidence-unavailable"),
                "evidence_authority": "TRQP-TSPP",
            }
        else:
            replacement = dict(source)
            replacement["evidence_authority"] = source["source_authority"]

        if pid in existing:
            existing[pid].clear()
            existing[pid].update(replacement)
        else:
            propositions.append(replacement)

    result.update(aggregate(propositions))
    result.setdefault("producer_evidence", {})["tspp"] = {
        "state": consumed["state"],
        "tspp_version": tspp_evidence.get("tspp_version"),
        "assurance_level": tspp_evidence.get("assurance_level"),
        "control_set": tspp_evidence.get("control_set"),
        "run": tspp_evidence.get("run"),
        "target": tspp_evidence.get("target"),
        "reassessment": tspp_evidence.get("reassessment"),
    }
    return result


def compose_profile_producers(
    assessment: dict,
    *,
    cts_evidence: dict,
    tspp_evidence: dict,
    target_id: str,
    run_id: str,
    protocol_version: str = "2.0",
    binding: str = "https-json",
) -> dict:
    """Compose both producer authorities while preserving producer-owned semantics."""
    result = compose_cts_core(
        assessment,
        cts_evidence,
        protocol_version=protocol_version,
        binding=binding,
    )
    return compose_tspp_security(result, tspp_evidence, target_id=target_id, run_id=run_id)
