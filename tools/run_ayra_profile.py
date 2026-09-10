#!/usr/bin/env python3
"""Execute bounded Ayra TRQP profile assurance against a deterministic fixture.

This adapter consumes observed endpoint behaviour and maps it to the proposition
state model established by #60. It does not redefine TRQP or Ayra semantics.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from tools.ayra_assurance_guards import profile_binding_state, signing_state
from tools.profile_assurance_model import aggregate, evaluate

DID_PREFIX = "did:"


def _is_did(value: object) -> bool:
    return isinstance(value, str) and value.startswith(DID_PREFIX) and len(value) > len(DID_PREFIX)


def _evidence(ref: str) -> list[dict]:
    return [{"kind": "test", "reference": ref}]


def assess_fixture(document: dict) -> dict:
    binding = profile_binding_state(document)
    if binding != "PASS":
        return {
            "profile_binding": binding,
            "signing": signing_state(document),
            "propositions": [],
            "dimensions": {},
        }

    endpoints = document.get("endpoints", {})
    propositions: list[dict] = []

    def add(pid: str, rid: str, dimension: str, strength: str, *, applicability: str = "APPLICABLE", implemented: bool | None, evidence_present: bool, satisfied: bool | None, reason: str) -> None:
        propositions.append({
            "proposition_id": pid,
            "requirement_id": rid,
            "dimension": dimension,
            "normative_strength": strength,
            "applicability": applicability,
            "evidence": _evidence(reason) if evidence_present else [],
            "result": evaluate(
                strength=strength,
                applicability=applicability,
                implemented=implemented,
                evidence_present=evidence_present,
                satisfied=satisfied,
            ),
            "reason": reason,
        })

    for name, pid, rid in (
        ("authorization", "PROP-AYRA-CORE-001", "AYRA-CORE-001"),
        ("recognition", "PROP-AYRA-CORE-002", "AYRA-CORE-002"),
    ):
        endpoint = endpoints.get(name)
        implemented = endpoint is not None
        satisfied = bool(endpoint and endpoint.get("method") == "POST" and endpoint.get("status") == 200)
        add(pid, rid, "core_profile", "MUST", implemented=implemented, evidence_present=implemented, satisfied=satisfied if implemented else None, reason=f"fixture:endpoints.{name}")

    ids = document.get("ids")
    id_values = list(ids.values()) if isinstance(ids, dict) else []
    add(
        "PROP-AYRA-ID-001", "AYRA-ID-001", "core_profile", "MUST",
        implemented=bool(id_values), evidence_present=bool(id_values),
        satisfied=all(_is_did(value) for value in id_values) if id_values else None,
        reason="fixture:ids",
    )

    error = document.get("error_response")
    problem_ok = bool(
        error
        and error.get("content_type") == "application/problem+json"
        and isinstance(error.get("body"), dict)
        and error["body"].get("status") == error.get("status")
    )
    add(
        "PROP-AYRA-ERR-001", "AYRA-ERR-001", "operational", "MUST",
        implemented=error is not None, evidence_present=error is not None,
        satisfied=problem_ok if error is not None else None,
        reason="fixture:error_response",
    )

    operational_negative = bool(error and error.get("interpreted_as_trust_negative", False))
    add(
        "PROP-AYRA-ERR-002", "AYRA-ERR-002", "operational", "MUST_NOT",
        implemented=error is not None, evidence_present=error is not None,
        satisfied=(not operational_negative) if error is not None else None,
        reason="fixture:error_response.interpreted_as_trust_negative",
    )

    rate_applicability = document.get("rate_limiting", "UNKNOWN")
    if rate_applicability is True:
        rate_state = "APPLICABLE"
    elif rate_applicability is False:
        rate_state = "NOT_APPLICABLE"
    else:
        rate_state = "UNKNOWN"
    rate = document.get("rate_limit_response")
    rate_ok = bool(
        rate
        and rate.get("status") == 429
        and rate.get("content_type") == "application/problem+json"
        and isinstance(rate.get("body"), dict)
        and rate["body"].get("status") in (None, 429)
        and not rate.get("interpreted_as_trust_negative", False)
    )
    add(
        "PROP-AYRA-RATE-001", "AYRA-RATE-001", "operational", "MUST",
        applicability=rate_state, implemented=rate is not None,
        evidence_present=rate is not None or rate_state == "NOT_APPLICABLE",
        satisfied=rate_ok if rate is not None else None,
        reason="fixture:rate_limit_response",
    )

    extension_applicability = document.get("unsupported_extension", "UNKNOWN")
    if extension_applicability is True:
        extension_state = "APPLICABLE"
    elif extension_applicability is False:
        extension_state = "NOT_APPLICABLE"
    else:
        extension_state = "UNKNOWN"
    extension = document.get("unsupported_extension_response")
    extension_ok = bool(
        extension
        and extension.get("status") == 501
        and extension.get("content_type") == "application/problem+json"
    )
    add(
        "PROP-AYRA-EXT-002", "AYRA-EXT-002", "extension", "MUST",
        applicability=extension_state, implemented=extension is not None,
        evidence_present=extension is not None or extension_state == "NOT_APPLICABLE",
        satisfied=extension_ok if extension is not None else None,
        reason="fixture:unsupported_extension_response",
    )

    registry_id = document.get("registry_id")
    add(
        "PROP-AYRA-DID-001", "AYRA-DID-001", "authority", "MUST",
        implemented=registry_id is not None, evidence_present=registry_id is not None,
        satisfied=_is_did(registry_id) if registry_id is not None else None,
        reason="fixture:registry_id",
    )

    return {
        "profile_binding": binding,
        "signing": signing_state(document),
        "propositions": propositions,
        **aggregate(propositions),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    document = json.loads(args.fixture.read_text(encoding="utf-8"))
    result = assess_fixture(document)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
