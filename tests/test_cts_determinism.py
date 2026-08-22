import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from cts_determinism import DeterminismEvidenceError, assurance_projection, load_and_validate


def _report(deterministic=True, prohibited=0):
    return {
        "report_version": "1.0.0",
        "policy": {
            "id": "trqp-cts/replay-determinism",
            "version": "1.0.0",
            "sha256": "a" * 64,
        },
        "source": {"run_id": "source", "semantic_sha256": "b" * 64},
        "replay": {"run_id": "replay", "semantic_sha256": "b" * 64},
        "deterministic": deterministic,
        "summary": {
            "difference_count": prohibited,
            "permitted_difference_count": 0,
            "prohibited_difference_count": prohibited,
        },
        "differences": [],
    }


def _write(tmp_path, report):
    import json

    p = tmp_path / "determinism-report.json"
    p.write_text(json.dumps(report), encoding="utf-8")
    return p


def test_valid_determinism_is_projected(tmp_path):
    report = load_and_validate(_write(tmp_path, _report()))
    projection = assurance_projection(report)
    assert projection["status"] == "pass"
    assert projection["prohibited_difference_count"] == 0
    assert projection["policy"]["version"] == "1.0.0"


def test_nondeterministic_report_fails_closed(tmp_path):
    with pytest.raises(DeterminismEvidenceError, match="determinism failed"):
        load_and_validate(_write(tmp_path, _report(deterministic=False)))


def test_prohibited_difference_fails_closed(tmp_path):
    with pytest.raises(DeterminismEvidenceError, match="prohibited difference"):
        load_and_validate(_write(tmp_path, _report(deterministic=True, prohibited=1)))


def test_missing_policy_identity_fails_closed(tmp_path):
    report = _report()
    report["policy"]["sha256"] = ""
    with pytest.raises(DeterminismEvidenceError, match="policy missing sha256"):
        load_and_validate(_write(tmp_path, report))
