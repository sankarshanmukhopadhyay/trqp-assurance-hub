import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from tools.build_ayra_assurance_bundle import ROOT, build, render_report

FIXTURES = Path(__file__).parent / "fixtures" / "ayra"
OBSERVED_AT = "2026-09-10T15:30:00Z"
RUN_ID = "ayra-fixture-001"


def load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def build_fixture():
    return build(
        fixture=load("conformant.json"),
        authority_observation=load("authority-success.json"),
        run_id=RUN_ID,
        observed_at=OBSERVED_AT,
    )


def test_bundle_is_deterministic_for_same_inputs():
    first_bundle, first_payloads = build_fixture()
    second_bundle, second_payloads = build_fixture()
    assert first_bundle == second_bundle
    assert first_payloads == second_payloads


def test_bundle_contains_explicit_profile_and_target_provenance():
    bundle, _ = build_fixture()
    assert bundle["profile"]["id"] == "ayra-trqp"
    assert bundle["profile"]["version"] == "0.6.0-draft"
    assert bundle["profile"]["source_revision"] == "ec7768572592b50ba3f4102c026c2449148b5e11"
    assert bundle["target"]["registry_id"] == "did:web:registry.example.org"
    assert bundle["run"] == {"run_id": RUN_ID, "observed_at": OBSERVED_AT}


def test_sensitive_fields_are_removed_before_persistence():
    fixture = load("conformant.json")
    fixture["headers"] = {"Authorization": "Bearer secret", "Cookie": "session=x", "X-Trace": "safe"}
    bundle, payloads = build(
        fixture=fixture,
        authority_observation=load("authority-success.json"),
        run_id=RUN_ID,
        observed_at=OBSERVED_AT,
    )
    endpoint = payloads["endpoint-evidence.json"].decode("utf-8")
    assert "Bearer secret" not in endpoint
    assert "session=x" not in endpoint
    assert "X-Trace" in endpoint
    assert "headers.Authorization" in bundle["redaction"]["removed_fields"]
    assert "headers.Cookie" in bundle["redaction"]["removed_fields"]


def test_artifact_hashes_bind_machine_evidence():
    bundle, payloads = build_fixture()
    for artifact in bundle["artifacts"]:
        assert artifact["path"] in payloads
        import hashlib
        assert hashlib.sha256(payloads[artifact["path"]]).hexdigest() == artifact["sha256"]


def test_report_is_derived_from_machine_results():
    bundle, _ = build_fixture()
    report = render_report(bundle)
    for dimension, item in bundle["results"]["profile"]["dimensions"].items():
        assert f"`{dimension}`: **{item['result']}**" in report
    for key in ("identifier_syntax", "did_method", "resolution", "service_discovery", "governance_discovery", "control_evidence", "governance_legitimacy"):
        assert f"`{key}`: **{bundle['results']['authority'][key]}**" in report


def test_missing_required_provenance_is_schema_invalid():
    bundle, _ = build_fixture()
    broken = json.loads(json.dumps(bundle))
    del broken["profile"]["source_revision"]
    schema = json.loads((ROOT / "schemas" / "ayra-assurance-bundle.schema.json").read_text(encoding="utf-8"))
    with pytest.raises(ValidationError):
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(broken)


def test_report_preserves_legitimacy_boundary():
    bundle, _ = build_fixture()
    assert bundle["results"]["authority"]["governance_legitimacy"] == "INDETERMINATE"
    report = render_report(bundle)
    assert "do not establish governance legitimacy" in report
