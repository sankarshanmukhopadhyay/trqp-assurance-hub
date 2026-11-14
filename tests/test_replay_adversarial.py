"""Verify CTS replay evidence cannot be promoted from contradictory assertions."""
import json
import pytest
from tools.cts_determinism import DeterminismEvidenceError, load_and_validate


def report():
    state = {"algorithm": "sha256", "digest": "a" * 64,
             "identity": "sha256:" + "a" * 64, "source": "snapshot.json", "status": "verified"}
    return {
        "report_version": "1.0.0",
        "policy": {"id": "cts-policy", "version": "1.0.0", "sha256": "b"*64},
        "source": {"run_id": "source", "semantic_sha256": "c"*64, "target_state": state},
        "replay": {"run_id": "replay", "semantic_sha256": "c"*64, "target_state": state},
        "deterministic": True,
        "summary": {"difference_count": 0, "permitted_difference_count": 0,
                    "prohibited_difference_count": 0},
        "differences": [],
    }


def verify(tmp_path, doc):
    path = tmp_path / "replay.json"
    path.write_text(json.dumps(doc))
    return load_and_validate(path)


def test_matching_semantics_accepted(tmp_path):
    assert verify(tmp_path, report())["deterministic"] is True


def test_forged_deterministic_true_with_mismatched_hashes_rejected(tmp_path):
    value = report()
    value["replay"]["semantic_sha256"] = "d"*64
    with pytest.raises(DeterminismEvidenceError, match="semantic hashes"):
        verify(tmp_path, value)


def test_difference_counts_must_agree(tmp_path):
    value = report()
    value["summary"]["difference_count"] = 1
    with pytest.raises(DeterminismEvidenceError, match="summary disagrees"):
        verify(tmp_path, value)


def test_missing_producer_run_identity_rejected(tmp_path):
    value = report()
    value["source"]["run_id"] = None
    with pytest.raises(DeterminismEvidenceError, match="run_id missing"):
        verify(tmp_path, value)


def test_reused_run_identity_rejected(tmp_path):
    value = report()
    value["replay"]["run_id"] = "source"
    with pytest.raises(DeterminismEvidenceError, match="distinct executions"):
        verify(tmp_path, value)
