#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "artifacts" / "lifecycle"


def load(name):
    with (FIXTURES / name).open(encoding="utf-8") as f:
        return json.load(f)


def validate(record):
    required = {"record_id", "historical_assurance", "lifecycle_event_ref", "cts_reassessment_ref", "impact", "reassessment", "current_validity", "authority", "rationale"}
    missing = required - record.keys()
    assert not missing, f"missing fields: {sorted(missing)}"
    assert record["historical_assurance"]["result"] in {"PASS", "FAIL", "INDETERMINATE"}
    assert record["historical_assurance"]["ref"], "historical assurance must remain attributable"
    assert record["lifecycle_event_ref"], "TSPP lifecycle evidence must remain attributable"
    assert record["cts_reassessment_ref"], "CTS reassessment evidence must remain attributable"
    assert set(record["authority"]) == {"tspp", "cts", "hub"}, "authority boundaries must remain explicit"
    assert len(record["rationale"]) >= 10

    impact = record["impact"]
    state = record["current_validity"]
    reassessment = record["reassessment"]

    if impact == "material":
        assert state != "CURRENT", "material change cannot preserve CURRENT assurance"
        assert reassessment["required"] is True
    if impact == "unknown":
        assert state in {"INDETERMINATE", "REASSESSMENT_REQUIRED", "STALE"}
        assert reassessment["required"] is True
        assert reassessment["full_rerun_required"] is True
    if impact == "non_material" and state == "CURRENT":
        assert reassessment["required"] is False
        assert reassessment["full_rerun_required"] is False


def main():
    names = [
        "material-recomposition.json",
        "unknown-recomposition.json",
        "non-material-recomposition.json",
    ]
    for name in names:
        validate(load(name))

    probes = []
    material = load(names[0]); material["current_validity"] = "CURRENT"; probes.append(("material-current", material))
    unknown = load(names[1]); unknown["current_validity"] = "CURRENT"; probes.append(("unknown-current", unknown))
    unknown_no_full = load(names[1]); unknown_no_full["reassessment"]["full_rerun_required"] = False; probes.append(("unknown-no-full-rerun", unknown_no_full))
    no_cts = load(names[0]); no_cts["cts_reassessment_ref"] = ""; probes.append(("missing-cts-lineage", no_cts))

    for label, candidate in probes:
        try:
            validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(f"negative pressure test unexpectedly accepted: {label}")

    print("Assurance lifecycle recomposition boundaries satisfied")


if __name__ == "__main__":
    main()
