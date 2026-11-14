"""A producer rerun may vary artifact hashes but not assurance propositions."""
import json
from tools.stack_compare import digest


def test_reexecuted_evidence_does_not_require_byte_identical_reports(tmp_path):
    a, b = tmp_path / "a.json", tmp_path / "b.json"
    base = {"schema_version": "1.0", "run_id": "run-a",
            "target_state": {"identity": "sha256:" + "a"*64},
            "producer_results": {"cts": "fail", "tspp": "pass"},
            "artifacts": [{"role": "cts", "sha256": "a"*64}]}
    changed = {**base, "run_id": "run-b",
               "artifacts": [{"role": "cts", "sha256": "b"*64}]}
    a.write_text(json.dumps(base))
    b.write_text(json.dumps(changed))
    assert digest(a) != digest(b)
    assert digest(a, producer_reexecution=True) == digest(b, producer_reexecution=True)


def test_reexecution_cannot_hide_changed_outcome(tmp_path):
    a, b = tmp_path / "a.json", tmp_path / "b.json"
    a.write_text(json.dumps({"producer_results": {"cts": "pass"}}))
    b.write_text(json.dumps({"producer_results": {"cts": "fail"}}))
    assert digest(a, producer_reexecution=True) != digest(b, producer_reexecution=True)
