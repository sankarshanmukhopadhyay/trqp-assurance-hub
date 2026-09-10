#!/usr/bin/env python3
"""Profile assurance state semantics and dimension-preserving aggregation."""
from __future__ import annotations

from collections import defaultdict

RESULTS = {"PASS", "FAIL", "INDETERMINATE", "NOT_APPLICABLE", "NOT_IMPLEMENTED"}


def evaluate(*, strength: str, applicability: str, implemented: bool | None, evidence_present: bool, satisfied: bool | None) -> str:
    if applicability == "NOT_APPLICABLE":
        return "NOT_APPLICABLE"
    if applicability != "APPLICABLE":
        return "INDETERMINATE"
    if implemented is False:
        if strength == "MAY":
            return "NOT_IMPLEMENTED"
        return "FAIL" if strength in {"MUST", "MUST_NOT"} else "NOT_IMPLEMENTED"
    if not evidence_present or satisfied is None:
        return "INDETERMINATE"
    return "PASS" if satisfied else "FAIL"


def aggregate(propositions: list[dict]) -> dict:
    """Return independent dimension summaries; deliberately no global compliant boolean."""
    dimensions: dict[str, list[str]] = defaultdict(list)
    for proposition in propositions:
        result = proposition["result"]
        if result not in RESULTS:
            raise ValueError(f"unknown result: {result}")
        dimensions[proposition["dimension"]].append(result)

    summary = {}
    for dimension, results in sorted(dimensions.items()):
        material = [r for r in results if r not in {"NOT_APPLICABLE", "NOT_IMPLEMENTED"}]
        if "FAIL" in material:
            state = "FAIL"
        elif "INDETERMINATE" in material or not material:
            state = "INDETERMINATE"
        else:
            state = "PASS"
        summary[dimension] = {"result": state, "proposition_results": results}
    return {"dimensions": summary}
