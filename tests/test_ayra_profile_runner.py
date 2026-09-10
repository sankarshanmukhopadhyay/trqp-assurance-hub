import json
from pathlib import Path

from tools.run_ayra_profile import assess_fixture

FIXTURES = Path(__file__).parent / "fixtures" / "ayra"


def load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def by_requirement(result: dict) -> dict:
    return {item["requirement_id"]: item for item in result["propositions"]}


def test_conformant_fixture_passes_tested_dimensions():
    result = assess_fixture(load("conformant.json"))
    requirements = by_requirement(result)
    assert requirements["AYRA-CORE-001"]["result"] == "PASS"
    assert requirements["AYRA-CORE-002"]["result"] == "PASS"
    assert requirements["AYRA-ID-001"]["result"] == "PASS"
    assert requirements["AYRA-ERR-001"]["result"] == "PASS"
    assert requirements["AYRA-ERR-002"]["result"] == "PASS"
    assert requirements["AYRA-RATE-001"]["result"] == "PASS"
    assert requirements["AYRA-EXT-002"]["result"] == "PASS"
    assert requirements["AYRA-DID-001"]["result"] == "PASS"
    assert result["dimensions"]["core_profile"]["result"] == "PASS"
    assert result["dimensions"]["operational"]["result"] == "PASS"


def test_nonconformant_fixture_fails_without_false_negative_trust_semantics():
    result = assess_fixture(load("nonconformant.json"))
    requirements = by_requirement(result)
    assert requirements["AYRA-CORE-001"]["result"] == "FAIL"
    assert requirements["AYRA-CORE-002"]["result"] == "FAIL"
    assert requirements["AYRA-ID-001"]["result"] == "FAIL"
    assert requirements["AYRA-ERR-001"]["result"] == "FAIL"
    assert requirements["AYRA-ERR-002"]["result"] == "FAIL"
    assert requirements["AYRA-RATE-001"]["result"] == "FAIL"
    assert requirements["AYRA-EXT-002"]["result"] == "FAIL"
    assert requirements["AYRA-DID-001"]["result"] == "FAIL"
    assert result["dimensions"]["operational"]["result"] == "FAIL"


def test_missing_mandatory_observation_does_not_pass():
    result = assess_fixture({})
    requirements = by_requirement(result)
    assert requirements["AYRA-CORE-001"]["result"] == "FAIL"
    assert requirements["AYRA-CORE-002"]["result"] == "FAIL"
    assert requirements["AYRA-ID-001"]["result"] == "FAIL"
    assert requirements["AYRA-ERR-001"]["result"] == "FAIL"
    assert requirements["AYRA-RATE-001"]["result"] == "INDETERMINATE"
    assert requirements["AYRA-EXT-002"]["result"] == "INDETERMINATE"


def test_conditional_capabilities_can_be_explicitly_not_applicable():
    fixture = load("conformant.json")
    fixture["rate_limiting"] = False
    fixture.pop("rate_limit_response")
    fixture["unsupported_extension"] = False
    fixture.pop("unsupported_extension_response")
    requirements = by_requirement(assess_fixture(fixture))
    assert requirements["AYRA-RATE-001"]["result"] == "NOT_APPLICABLE"
    assert requirements["AYRA-EXT-002"]["result"] == "NOT_APPLICABLE"


def test_adapter_emits_no_global_compliance_boolean():
    result = assess_fixture(load("conformant.json"))
    assert "compliant" not in result
    assert "ayra_compliant" not in result
