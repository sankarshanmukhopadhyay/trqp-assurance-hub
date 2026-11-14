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
    assert producer_status({"summary": {"PASS": 2, "FAIL": 0, "NOT_APPLICABLE": 1},
                            "results": [{"result": "PASS"}, {"result": "PASS"},
                                        {"result": "NOT_APPLICABLE"}]}, require_details=True) == "pass"


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


def test_state_bound_cli_does_not_publish_pass_for_mixed_operational_evidence(tmp_path, monkeypatch):
    """Exercise the consumer-facing composition entry point, not only the reducer."""
    import json
    import sys
    from tools import run_state_bound_assurance as state_bound

    snapshot = _state("a" * 64)
    cts = {
        "run_id": "adversarial-1", "target_id": "service-1",
        "target_state": snapshot, "suite_version": "1.11.1",
        "summary": {"PASS": 2, "FAIL": 0, "ERROR": 1},
        "results": [{"result": "PASS"}, {"result": "PASS"}, {"result": "ERROR"}],
    }
    tspp = {
        "run_id": "adversarial-1", "target_id": "service-1",
        "target_state": snapshot, "tool_version": "0.18.1",
        "summary": {"PASS": 2, "FAIL": 0, "NOT_TESTED": 0},
        "results": [{"outcome": "PASS"}, {"outcome": "PASS"}],
    }
    cp, tp, dp = [tmp_path / name for name in ("cts.json", "tspp.json", "determinism.json")]
    cp.write_text(json.dumps(cts), encoding="utf-8")
    tp.write_text(json.dumps(tspp), encoding="utf-8")
    dp.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(state_bound, "load_and_validate", lambda path: {
        "source": {"run_id": "fixture-source", "target_state": snapshot},
        "replay": {"run_id": "fixture-replay", "target_state": snapshot}
    })
    monkeypatch.setattr(state_bound, "assurance_projection", lambda raw: {"verified": True})
    out = tmp_path / "out"
    monkeypatch.setattr(sys, "argv", [
        "run_state_bound_assurance.py", "--cts-report", str(cp),
        "--tspp-report", str(tp), "--cts-determinism-report", str(dp),
        "--out", str(out),
    ])

    assert state_bound.main() == 0
    decision = json.loads((out / "assurance-decision.json").read_text(encoding="utf-8"))
    manifest = json.loads((out / "state-bound-assurance-manifest.json").read_text(encoding="utf-8"))
    assert decision["outcome"] == "indeterminate"
    assert manifest["producer_results"]["cts"] == "indeterminate"
    assert manifest["producer_results"]["tspp"] == "pass"


def test_nonzero_producer_exit_never_becomes_pass():
    assert producer_status({"summary": {"PASS": 1, "FAIL": 0, "exit_status": 2}}) == "indeterminate"


def test_report_backed_manifest_does_not_upgrade_operational_uncertainty():
    import importlib.util
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("manifest_generator", root / "tools/generate-manifest.py")
    generator = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(generator)

    assert generator._infer_status({"summary": {"PASS": 1, "ERROR": 1}}) == "partial"
    assert generator._infer_status({"summary": {"PASS": 1, "NOT_TESTED": 1}}) == "partial"
    assert generator._infer_status({"summary": {"PASS": 1, "exit_status": 2}}) == "partial"
    assert generator._infer_status({"summary": {"PASS": 1, "FAIL": 0}}) == "pass"
    with pytest.raises(SystemExit, match="cannot override"):
        generator._assert_no_positive_override("pass", "partial", "overall_status")
    with pytest.raises(SystemExit, match="cannot override"):
        generator._assert_no_positive_override("pass", "fail", "conformance_status")



def test_contradictory_summary_and_detail_never_passes():
    report = {"summary": {"PASS": 2, "FAIL": 0},
              "results": [{"result": "PASS"}, {"result": "FAIL"}]}
    assert producer_status(report, require_details=True) == "indeterminate"


def test_unknown_operational_category_fails_closed():
    report = {"summary": {"PASS": 1, "WARN": 1},
              "results": [{"result": "PASS"}, {"result": "WARN"}]}
    assert producer_status(report, require_details=True) == "indeterminate"


def test_missing_results_cannot_produce_state_bound_pass():
    assert producer_status({"summary": {"PASS": 2}}, require_details=True) == "indeterminate"


def test_missing_state_source_is_not_verified():
    state = _state("a" * 64)
    state.pop("source")
    with pytest.raises(SystemExit, match="source missing"):
        require_verified_state({"target_state": state}, "TSPP")
