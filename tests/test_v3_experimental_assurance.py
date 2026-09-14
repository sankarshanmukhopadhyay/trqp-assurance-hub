from tools.validate_v3_experimental_assurance import (
    AUTHORITY,
    CANDIDATE_SHA,
    reconcile,
    validate,
)


def test_complete_pinned_reconciliation():
    report = validate()
    assert report["candidate_commit"] == CANDIDATE_SHA
    assert report["authority_status"] == AUTHORITY
    assert report["requirements"] == 32
    assert report["supported"] == 32
    assert report["not_supported"] == 0
    assert report["indeterminate"] == 0


def test_missing_evidence_never_becomes_supported():
    assert reconcile("PASS", "NOT_TESTED") == "INDETERMINATE"
    assert reconcile("NOT_TESTED", "PASS") == "INDETERMINATE"
    assert reconcile("INDETERMINATE", "PASS") == "INDETERMINATE"


def test_failure_is_not_supported():
    assert reconcile("FAIL", "PASS") == "NOT_SUPPORTED"
    assert reconcile("PASS", "FAIL") == "NOT_SUPPORTED"


def test_only_two_passes_support_claim():
    assert reconcile("PASS", "PASS") == "SUPPORTED"
