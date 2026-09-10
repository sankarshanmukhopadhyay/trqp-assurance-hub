import copy
import json
from pathlib import Path

from tools.ayra_assurance_guards import signing_state
from tools.ayra_authority_evidence import assess_authority, is_safe_https_url
from tools.run_ayra_profile import assess_fixture

FIXTURES = Path(__file__).parent / "fixtures" / "ayra"


def load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def by_requirement(result: dict) -> dict:
    return {item["requirement_id"]: item for item in result["propositions"]}


def test_unknown_profile_revision_blocks_assurance_execution():
    fixture = load("conformant.json")
    fixture["profile_binding"]["source_revision"] = "deadbeef"
    result = assess_fixture(fixture)
    assert result["profile_binding"] == "INDETERMINATE"
    assert result["propositions"] == []
    assert result["dimensions"] == {}


def test_cross_profile_binding_cannot_reuse_ayra_semantics():
    fixture = load("conformant.json")
    fixture["profile_binding"]["profile_id"] = "other-profile"
    result = assess_fixture(fixture)
    assert result["profile_binding"] == "INDETERMINATE"
    assert result["propositions"] == []


def test_schema_shaped_but_semantically_wrong_error_is_rejected():
    fixture = load("conformant.json")
    fixture["error_response"]["body"]["status"] = 404
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-ERR-001"]["result"] == "FAIL"


def test_operational_error_cannot_become_negative_trust_answer():
    fixture = load("conformant.json")
    fixture["error_response"]["interpreted_as_trust_negative"] = True
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-ERR-002"]["result"] == "FAIL"


def test_malformed_problem_details_fails():
    fixture = load("conformant.json")
    fixture["error_response"]["content_type"] = "application/json"
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-ERR-001"]["result"] == "FAIL"


def test_bad_rate_limit_response_fails_when_applicable():
    fixture = load("conformant.json")
    fixture["rate_limit_response"]["status"] = 503
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-RATE-001"]["result"] == "FAIL"


def test_optional_extension_501_boundary_is_enforced():
    fixture = load("conformant.json")
    fixture["unsupported_extension_response"]["status"] = 404
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-EXT-002"]["result"] == "FAIL"


def test_signing_should_absence_is_indeterminate_not_universal_failure():
    assert signing_state({"signing_applicable": True}) == "INDETERMINATE"
    assert signing_state({"signing_applicable": False}) == "NOT_APPLICABLE"
    assert signing_state({"signing_applicable": True, "signature_valid": False}) == "FAIL"


def test_unsafe_discovered_urls_are_rejected():
    for value in (
        "http://registry.example.org/trqp",
        "https://localhost/trqp",
        "https://127.0.0.1/trqp",
        "https://10.0.0.1/trqp",
        "https://169.254.169.254/latest/meta-data",
    ):
        assert not is_safe_https_url(value)


def test_stale_and_contradictory_authority_evidence_never_passes():
    observation = {
        "registry_did": "did:web:registry.example.org",
        "supported_did_methods": ["web"],
        "did_resolved": True,
        "trqp_service_endpoint": "https://registry.example.org/trqp",
        "expected_trqp_endpoint": "https://registry.example.org/trqp",
        "authority_id": "did:web:authority.example.org",
        "governance_framework": {
            "authority_id": "did:web:other.example.org",
            "discoverable": True,
            "fresh": False,
        },
    }
    result = assess_authority(observation)
    assert result["governance_discovery"] != "PASS"
    assert result["governance_legitimacy"] == "INDETERMINATE"


def test_foreign_fields_do_not_mutate_ayra_result_surface():
    baseline = assess_fixture(load("conformant.json"))
    fixture = copy.deepcopy(load("conformant.json"))
    fixture["foreign_profile"] = {"compliant": True, "override": "PASS"}
    result = assess_fixture(fixture)
    assert result["dimensions"] == baseline["dimensions"]
    assert result["profile_binding"] == "PASS"
