from tools.profile_assurance_model import aggregate, evaluate


def test_missing_evidence_never_passes():
    assert evaluate(strength="MUST", applicability="APPLICABLE", implemented=True, evidence_present=False, satisfied=True) == "INDETERMINATE"


def test_unknown_applicability_is_indeterminate():
    assert evaluate(strength="MUST", applicability="UNKNOWN", implemented=True, evidence_present=True, satisfied=True) == "INDETERMINATE"


def test_not_applicable_is_explicit():
    assert evaluate(strength="MUST", applicability="NOT_APPLICABLE", implemented=False, evidence_present=False, satisfied=None) == "NOT_APPLICABLE"


def test_optional_extension_absence_is_not_failure():
    assert evaluate(strength="MAY", applicability="APPLICABLE", implemented=False, evidence_present=False, satisfied=None) == "NOT_IMPLEMENTED"


def test_missing_must_capability_fails():
    assert evaluate(strength="MUST", applicability="APPLICABLE", implemented=False, evidence_present=False, satisfied=None) == "FAIL"


def test_unmet_should_is_visible_failure_but_not_promoted_to_must_semantics():
    assert evaluate(strength="SHOULD", applicability="APPLICABLE", implemented=True, evidence_present=True, satisfied=False) == "FAIL"


def test_dimension_aggregation_preserves_indeterminacy():
    result = aggregate([
        {"dimension": "core_profile", "result": "PASS"},
        {"dimension": "authority", "result": "INDETERMINATE"},
    ])
    assert result == {"dimensions": {
        "authority": {"result": "INDETERMINATE", "proposition_results": ["INDETERMINATE"]},
        "core_profile": {"result": "PASS", "proposition_results": ["PASS"]},
    }}
    assert "compliant" not in result


def test_failure_dominates_only_its_dimension():
    result = aggregate([
        {"dimension": "core_profile", "result": "PASS"},
        {"dimension": "security", "result": "FAIL"},
        {"dimension": "extension", "result": "NOT_IMPLEMENTED"},
    ])
    assert result["dimensions"]["core_profile"]["result"] == "PASS"
    assert result["dimensions"]["security"]["result"] == "FAIL"
    assert result["dimensions"]["extension"]["result"] == "INDETERMINATE"
