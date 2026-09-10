from tools.consume_cts_profile_evidence import consume


def evidence(result="PASS", *, version="2.0", binding="https-json", state="CURRENT"):
    return {
        "producer": "trqp-conformance-suite",
        "protocol": {"id": "trqp", "version": version, "binding": binding},
        "reassessment": {"state": state},
        "results": [
            {"test_case_id": "TC-AUTHZ-001", "result": result, "evidence_ref": "cts://run-1/TC-AUTHZ-001"},
            {"test_case_id": "TC-RECOG-001", "result": "PASS", "evidence_ref": "cts://run-1/TC-RECOG-001"},
        ],
    }


def test_ayra_authorization_consumes_cts_owned_result():
    result = consume(evidence(), expected_protocol_version="2.0", expected_binding="https-json", proposition_ids=["PROP-AYRA-CORE-001"])
    proposition = result["propositions"][0]
    assert proposition["result"] == "PASS"
    assert proposition["source_authority"] == "trqp-conformance-suite"
    assert proposition["source_test_case_id"] == "TC-AUTHZ-001"


def test_cts_fail_cannot_be_overridden_by_hub():
    result = consume(evidence("FAIL"), expected_protocol_version="2.0", expected_binding="https-json", proposition_ids=["PROP-AYRA-CORE-001"])
    assert result["propositions"][0]["result"] == "FAIL"


def test_wrong_protocol_version_is_indeterminate():
    result = consume(evidence(version="3.0"), expected_protocol_version="2.0", expected_binding="https-json")
    assert result["state"] == "INDETERMINATE"
    assert result["propositions"] == []


def test_wrong_binding_is_indeterminate():
    result = consume(evidence(binding="didcomm"), expected_protocol_version="2.0", expected_binding="https-json")
    assert result["state"] == "INDETERMINATE"


def test_stale_cts_evidence_is_not_consumed_as_current():
    result = consume(evidence(state="REASSESS_REQUIRED"), expected_protocol_version="2.0", expected_binding="https-json")
    assert result["state"] == "INDETERMINATE"
    assert result["propositions"] == []


def test_missing_test_evidence_is_indeterminate_not_pass():
    doc = evidence()
    doc["results"] = []
    result = consume(doc, expected_protocol_version="2.0", expected_binding="https-json", proposition_ids=["PROP-AYRA-CORE-001"])
    assert result["propositions"][0]["result"] == "INDETERMINATE"


def test_not_applicable_remains_distinct():
    result = consume(evidence("NOT_APPLICABLE"), expected_protocol_version="2.0", expected_binding="https-json", proposition_ids=["PROP-AYRA-CORE-001"])
    assert result["propositions"][0]["result"] == "NOT_APPLICABLE"
