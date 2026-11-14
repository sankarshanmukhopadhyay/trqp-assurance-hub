"""Adversarial publication proof checks with synthetic GitHub API responses."""
import copy
import json
from pathlib import Path
from tools.verify_release_publication import verify

ROOT = Path(__file__).resolve().parents[1]


def fixture():
    manifest = json.loads((ROOT / "stack/releases/2026.4/manifest.json").read_text())
    registry = json.loads((ROOT / "stack/schema/release-gates.json").read_text())
    evidence, coord = manifest["eligibility_evidence"], manifest["coordinator"]
    run = {"id": evidence["workflow_run_id"], "head_sha": coord["validated_main_commit"],
           "path": ".github/workflows/stack-release-eligibility.yml", "head_branch": "main",
           "conclusion": "success"}
    steps = sorted({mapping["check_step"] for mapping in registry["gates"].values()})
    jobs = {"jobs": [{"name": "decisive-test", "conclusion": "success",
                      "steps": [{"name": step, "conclusion": "success"} for step in steps]}]}
    comment = {"id": coord["human_release_judgment_comment_id"],
               "user": {"login": "sankarshanmukhopadhyay"},
               "created_at": "2026-10-02T01:47:27Z",
               "updated_at": "2026-10-02T01:47:27Z",
               "body": ("Human release judgment: ACCEPT " + manifest["stack"]["id"] +
                        " " + str(evidence["workflow_run_id"]) + " " + coord["validated_main_commit"] +
                        " " + evidence["artifact_digest"])}
    return manifest, run, jobs, comment, registry


def test_provenance_accepts_complete_evidence_chain():
    assert verify(*fixture()) == []


def test_foreign_workflow_is_rejected():
    m, r, j, c, g = fixture()
    r["path"] = ".github/workflows/other.yml"
    assert any("workflow path" in e for e in verify(m, r, j, c, g))


def test_mismatched_validated_commit_is_rejected():
    m, r, j, c, g = fixture()
    r["head_sha"] = "f" * 40
    assert any("SHA" in e for e in verify(m, r, j, c, g))


def test_unexecuted_gate_cannot_publish():
    m, r, j, c, g = fixture()
    j["jobs"][0]["steps"][0]["conclusion"] = "skipped"
    assert any("no successful execution step" in e for e in verify(m, r, j, c, g))


def test_wrong_or_changed_human_acceptance_rejected():
    m, r, j, c, g = fixture()
    c["updated_at"] = "2026-10-03T00:00:00Z"
    assert any("edited" in e for e in verify(m, r, j, c, g))
    c["updated_at"] = c["created_at"]
    c["user"]["login"] = "unauthorized"
    assert any("author" in e for e in verify(m, r, j, c, g))


def test_missing_artifact_digest_in_acceptance_rejected():
    m, r, j, c, g = fixture()
    c["body"] = "Human release judgment: ACCEPT"
    assert any("does not bind" in e for e in verify(m, r, j, c, g))



def test_original_lotus_human_judgment_spelling_is_accepted():
    m, r, j, c, g = fixture()
    c["body"] = c["body"].replace("trqp-stack-2026.4", "TRQP Stack 2026.4")
    assert verify(m, r, j, c, g) == []


def test_foreign_release_identity_is_rejected():
    m, r, j, c, g = fixture()
    c["body"] = c["body"].replace("trqp-stack-2026.4", "TRQP Stack 2026.5")
    assert any("release identity" in e for e in verify(m, r, j, c, g))
