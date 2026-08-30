#!/usr/bin/env python3
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "artifacts" / "lifecycle"


def load(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def validate_authority_drift(record):
    compatibility = record["authority_compatibility"]
    assert compatibility["drift_detected"] is True
    assert compatibility["compatible"] is False
    assert compatibility["expected_semantic_authority"]
    assert compatibility["observed_semantic_authority"]
    assert compatibility["expected_semantic_authority"] != compatibility["observed_semantic_authority"]
    assert record["current_validity"] in {"INDETERMINATE", "STALE", "REASSESSMENT_REQUIRED"}
    assert record["current_validity"] != "CURRENT"
    assert record["reassessment"]["required"] is True
    assert record["reassessment"]["full_rerun_required"] is True
    assert "tsmm" in record["authority"] and "tis" in record["authority"] and "hub" in record["authority"]
    assert len(record["rationale"]) >= 20


def validate_supersession(record):
    previous = record["previous_assurance"]
    reassessment = record["reassessment"]
    supersession = record["supersession"]
    current = record["current_assurance"]

    assert previous["ref"]
    assert previous["validity"] == "SUPERSEDED"
    assert record["trigger"]["impact"] == "material"
    assert record["trigger"]["lifecycle_event_ref"]
    assert reassessment["plan_ref"]
    assert reassessment["completed"] is True
    assert reassessment["evidence_current"] is True
    assert reassessment["scope_completed"]
    assert supersession["lineage_complete"] is True
    assert supersession["history_rewritten"] is False
    assert supersession["superseded_ref"] == previous["ref"]
    assert supersession["superseding_ref"]
    assert current["validity"] == "CURRENT"
    assert current["basis"]
    assert set(record["authority"]) == {"tspp", "cts", "hub"}
    assert len(record["rationale"]) >= 20


def expect_rejected(label, validator, record):
    try:
        validator(record)
    except (AssertionError, KeyError):
        return
    raise AssertionError(f"negative pressure test unexpectedly accepted: {label}")


def main():
    drift = load("authority-drift-recomposition.json")
    supersession = load("supersession-recomposition.json")
    validate_authority_drift(drift)
    validate_supersession(supersession)

    candidate = copy.deepcopy(drift)
    candidate["current_validity"] = "CURRENT"
    expect_rejected("authority-drift-current", validate_authority_drift, candidate)

    candidate = copy.deepcopy(drift)
    candidate["authority_compatibility"]["drift_detected"] = False
    expect_rejected("authority-drift-not-detected", validate_authority_drift, candidate)

    candidate = copy.deepcopy(drift)
    candidate["reassessment"]["full_rerun_required"] = False
    expect_rejected("authority-drift-bounded-without-compatibility", validate_authority_drift, candidate)

    candidate = copy.deepcopy(supersession)
    candidate["reassessment"]["completed"] = False
    expect_rejected("supersession-before-reassessment-complete", validate_supersession, candidate)

    candidate = copy.deepcopy(supersession)
    candidate["supersession"]["lineage_complete"] = False
    expect_rejected("supersession-without-lineage", validate_supersession, candidate)

    candidate = copy.deepcopy(supersession)
    candidate["supersession"]["history_rewritten"] = True
    expect_rejected("supersession-rewrites-history", validate_supersession, candidate)

    candidate = copy.deepcopy(supersession)
    candidate["reassessment"]["evidence_current"] = False
    expect_rejected("supersession-from-stale-reassessment", validate_supersession, candidate)

    print("Authority drift and supersession boundaries satisfied")


if __name__ == "__main__":
    main()
