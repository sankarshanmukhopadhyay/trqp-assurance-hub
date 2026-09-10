import json
from pathlib import Path

from tools.compose_profile_producer_evidence import compose_cts_core
from tools.run_ayra_profile import assess_fixture

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def proposition(result, pid):
    return next(item for item in result["propositions"] if item["proposition_id"] == pid)


def test_cts_evidence_replaces_duplicate_local_core_observation():
    fixture = load("tests/fixtures/ayra/conformant.json")
    local = assess_fixture(fixture)
    cts = load("tests/fixtures/ayra/cts-profile-evidence.json")
    composed = compose_cts_core(local, cts)
    authz = proposition(composed, "PROP-AYRA-CORE-001")
    assert authz["result"] == "PASS"
    assert authz["evidence_authority"] == "trqp-conformance-suite"
    assert authz["source_test_case_id"] == "TC-AUTHZ-001"
    assert authz["evidence"][0]["kind"] == "external"


def test_cts_failure_overrides_local_pass_for_cts_owned_core_proposition():
    fixture = load("tests/fixtures/ayra/conformant.json")
    local = assess_fixture(fixture)
    cts = load("tests/fixtures/ayra/cts-profile-evidence.json")
    cts["results"][0]["result"] = "FAIL"
    composed = compose_cts_core(local, cts)
    assert proposition(composed, "PROP-AYRA-CORE-001")["result"] == "FAIL"
    assert composed["dimensions"]["core_profile"]["result"] == "FAIL"


def test_stale_cts_evidence_makes_core_indeterminate_without_local_fallback():
    fixture = load("tests/fixtures/ayra/conformant.json")
    local = assess_fixture(fixture)
    cts = load("tests/fixtures/ayra/cts-profile-evidence.json")
    cts["reassessment"]["state"] = "REASSESS_REQUIRED"
    composed = compose_cts_core(local, cts)
    assert proposition(composed, "PROP-AYRA-CORE-001")["result"] == "INDETERMINATE"
    assert proposition(composed, "PROP-AYRA-CORE-002")["result"] == "INDETERMINATE"


def test_profile_owned_non_core_propositions_are_unchanged():
    fixture = load("tests/fixtures/ayra/conformant.json")
    local = assess_fixture(fixture)
    cts = load("tests/fixtures/ayra/cts-profile-evidence.json")
    composed = compose_cts_core(local, cts)
    for pid in ("PROP-AYRA-ID-001", "PROP-AYRA-EXT-002", "PROP-AYRA-DID-001"):
        before = proposition(local, pid)
        after = proposition(composed, pid)
        assert after["result"] == before["result"]
        assert after["reason"] == before["reason"]


def test_protocol_mismatch_does_not_reuse_local_core_evidence():
    fixture = load("tests/fixtures/ayra/conformant.json")
    local = assess_fixture(fixture)
    cts = load("tests/fixtures/ayra/cts-profile-evidence.json")
    cts["protocol"]["version"] = "3.0"
    composed = compose_cts_core(local, cts)
    assert proposition(composed, "PROP-AYRA-CORE-001")["result"] == "INDETERMINATE"
    assert composed["producer_evidence"]["cts"]["state"] == "INDETERMINATE"
