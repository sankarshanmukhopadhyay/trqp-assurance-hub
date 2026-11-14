"""Adversarial reduction and state-contract checks for the operational Hub path."""
import pytest
from tools.run_state_bound_assurance import producer_status, require_verified_state, require_state_pair


@pytest.mark.parametrize("summary", [
    {"PASS": 1, "ERROR": 1},
    {"PASS": 2, "SKIP": 1},
    {"PASS": 1, "NOT_TESTED": 1},
    {"PASS": 1, "INDETERMINATE": 1},
    {"PASS": 1, "NOT_IMPLEMENTED": 1},
    {"PASS": "invalid"},
    {"PASS": -1},
])
def test_incomplete_or_invalid_producer_evidence_never_passes(summary):
    assert producer_status({"summary": summary}) == "indeterminate"


def test_explicit_negative_result_is_preserved():
    assert producer_status({"summary": {"FAIL": 1, "PASS": 1, "ERROR": 2}}) == "fail"


def test_complete_positive_result_is_accepted():
    assert producer_status({"summary": {"PASS": 2, "FAIL": 0, "NOT_APPLICABLE": 1}}) == "pass"


def test_empty_summary_is_not_success():
    assert producer_status({"summary": {}}) == "indeterminate"
    assert producer_status({}) == "indeterminate"


def _state(digest):
    return {"algorithm": "sha256", "digest": digest, "identity": "sha256:" + digest,
            "source": "snapshot.json", "status": "verified"}


@pytest.mark.parametrize("digest", ["z" * 64, "A" * 64, "a" * 63, ""])
def test_invalid_sha256_identity_rejected(digest):
    with pytest.raises(SystemExit, match="digest invalid"):
        require_verified_state({"target_state": _state(digest)}, "CTS")


def test_valid_state_pair_does_not_establish_live_deployment_authenticity():
    cts = {"target_state": _state("a" * 64)}
    tspp = {"target_state": _state("a" * 64)}
    assert require_state_pair(cts, tspp)["digest"] == "a" * 64
    # Live deployment provenance is an external assurance proposition, not asserted here.
