from copy import deepcopy
import json
from pathlib import Path

from tools.compose_profile_producer_evidence import compose_profile_producers, compose_tspp_security
from tools.consume_tspp_profile_evidence import consume
from tools.run_ayra_profile import assess_fixture

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "ayra"


def load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def current_tspp() -> dict:
    return load("tspp-profile-current.json")


def base_assessment() -> dict:
    return assess_fixture(load("conformant.json"))


def test_current_tspp_pass_is_attributed_to_tspp():
    result = consume(current_tspp(), expected_target_id="ayra-registry-fixture", expected_run_id="ayra-profile-run-001")
    proposition = result["propositions"][0]
    assert proposition["result"] == "PASS"
    assert proposition["source_authority"] == "TRQP-TSPP"
    assert proposition["source_control_id"] == "TSPP-AL2-01"


def test_tspp_fail_cannot_be_overridden_by_local_state():
    evidence = current_tspp()
    evidence["posture"]["result"] = "FAIL"
    evidence["posture"]["controls"][0]["result"] = "FAIL"
    result = compose_tspp_security(base_assessment(), evidence, target_id="ayra-registry-fixture", run_id="ayra-profile-run-001")
    proposition = next(p for p in result["propositions"] if p["proposition_id"] == "PROP-AYRA-SIGN-001")
    assert proposition["result"] == "FAIL"
    assert proposition["evidence_authority"] == "TRQP-TSPP"


def test_reassessment_required_is_indeterminate_for_current_assurance():
    evidence = current_tspp()
    evidence["reassessment"] = {"state": "REASSESS_REQUIRED"}
    result = compose_tspp_security(base_assessment(), evidence, target_id="ayra-registry-fixture", run_id="ayra-profile-run-001")
    proposition = next(p for p in result["propositions"] if p["proposition_id"] == "PROP-AYRA-SIGN-001")
    assert proposition["result"] == "INDETERMINATE"
    assert result["producer_evidence"]["tspp"]["state"] == "INDETERMINATE"


def test_wrong_target_and_run_fail_safe():
    evidence = current_tspp()
    assert consume(evidence, expected_target_id="other", expected_run_id="ayra-profile-run-001")["state"] == "INDETERMINATE"
    assert consume(evidence, expected_target_id="ayra-registry-fixture", expected_run_id="other")["state"] == "INDETERMINATE"


def test_missing_control_evidence_is_indeterminate():
    evidence = current_tspp()
    evidence["posture"]["controls"] = []
    result = consume(evidence, expected_target_id="ayra-registry-fixture", expected_run_id="ayra-profile-run-001")
    assert result["propositions"][0]["result"] == "INDETERMINATE"


def test_unbound_control_set_is_not_current():
    evidence = current_tspp()
    evidence["control_set"]["revision"] = ""
    result = consume(evidence, expected_target_id="ayra-registry-fixture", expected_run_id="ayra-profile-run-001")
    assert result == {"state": "INDETERMINATE", "reason": "tspp-control-set-unbound", "propositions": []}


def test_cross_source_composition_preserves_independent_authorities():
    assessment = base_assessment()
    cts = load("cts-profile-current.json")
    tspp = current_tspp()
    # A CTS failure must remain visible while TSPP remains independently positive.
    cts["results"][0]["result"] = "FAIL"
    result = compose_profile_producers(
        assessment,
        cts_evidence=cts,
        tspp_evidence=tspp,
        target_id="ayra-registry-fixture",
        run_id="ayra-profile-run-001",
    )
    by_id = {p["proposition_id"]: p for p in result["propositions"]}
    assert by_id["PROP-AYRA-CORE-001"]["result"] == "FAIL"
    assert by_id["PROP-AYRA-CORE-001"]["evidence_authority"] == "trqp-conformance-suite"
    assert by_id["PROP-AYRA-SIGN-001"]["result"] == "PASS"
    assert by_id["PROP-AYRA-SIGN-001"]["evidence_authority"] == "TRQP-TSPP"
    assert result["producer_evidence"]["cts"]["state"] == "CURRENT"
    assert result["producer_evidence"]["tspp"]["state"] == "CURRENT"
    assert "compliant" not in result


def test_tspp_composition_does_not_modify_non_security_profile_propositions():
    assessment = base_assessment()
    before = {
        p["proposition_id"]: deepcopy(p)
        for p in assessment["propositions"]
        if p["dimension"] != "security"
    }
    result = compose_tspp_security(assessment, current_tspp(), target_id="ayra-registry-fixture", run_id="ayra-profile-run-001")
    after = {p["proposition_id"]: p for p in result["propositions"]}
    for pid, proposition in before.items():
        assert after[pid] == proposition
