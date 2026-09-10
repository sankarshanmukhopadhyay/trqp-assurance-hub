import json
from pathlib import Path

from tools.ayra_authority_evidence import assess_authority, is_safe_https_url

FIXTURES = Path(__file__).parent / "fixtures" / "ayra"


def load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_successful_bounded_discovery_does_not_claim_legitimacy():
    result = assess_authority(load("authority-success.json"))
    assert result["identifier_syntax"] == "PASS"
    assert result["did_method"] == "PASS"
    assert result["resolution"] == "PASS"
    assert result["service_discovery"] == "PASS"
    assert result["governance_discovery"] == "PASS"
    assert result["control_evidence"] == "INDETERMINATE"
    assert result["governance_legitimacy"] == "INDETERMINATE"


def test_malformed_did_fails_syntax_without_inventing_resolution():
    result = assess_authority({"registry_did": "registry-123"})
    assert result["identifier_syntax"] == "FAIL"
    assert result["did_method"] == "INDETERMINATE"
    assert result["resolution"] == "FAIL"


def test_unsupported_did_method_is_visible_failure():
    result = assess_authority({"registry_did": "did:key:z6Mk...", "supported_did_methods": ["web"], "did_resolved": True})
    assert result["identifier_syntax"] == "PASS"
    assert result["did_method"] == "FAIL"


def test_endpoint_mismatch_fails_discovery():
    result = assess_authority({
        "registry_did": "did:web:registry.example.org",
        "did_resolved": True,
        "trqp_service_endpoint": "https://other.example.org/trqp",
        "expected_trqp_endpoint": "https://registry.example.org/trqp",
    })
    assert result["service_discovery"] == "FAIL"


def test_missing_governance_evidence_does_not_pass():
    result = assess_authority({"registry_did": "did:web:registry.example.org", "did_resolved": True})
    assert result["governance_discovery"] == "FAIL"
    assert result["governance_legitimacy"] == "INDETERMINATE"


def test_contradictory_governance_data_fails_discovery():
    result = assess_authority({
        "registry_did": "did:web:registry.example.org",
        "did_resolved": True,
        "authority_id": "did:web:authority.example.org",
        "governance_framework": {"authority_id": "did:web:other.example.org", "discoverable": True},
    })
    assert result["governance_discovery"] == "FAIL"


def test_ssrf_unsafe_urls_are_rejected():
    assert not is_safe_https_url("http://registry.example.org/trqp")
    assert not is_safe_https_url("https://localhost/trqp")
    assert not is_safe_https_url("https://127.0.0.1/trqp")
    assert not is_safe_https_url("https://169.254.169.254/latest/meta-data")
    assert is_safe_https_url("https://registry.example.org/trqp")
