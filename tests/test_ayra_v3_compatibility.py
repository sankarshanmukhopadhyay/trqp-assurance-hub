from pathlib import Path

import pytest
import yaml
from jsonschema import ValidationError

from tools.validate_ayra_v3_compatibility import load_and_validate, status_for_revisions

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "profiles" / "ayra" / "v3-compatibility.yaml"


def test_matrix_validates_and_covers_current_catalogue():
    document = load_and_validate(MATRIX)
    assert len(document["mappings"]) == 13


def test_unknown_classification_is_rejected(tmp_path):
    document = yaml.safe_load(MATRIX.read_text(encoding="utf-8"))
    document["mappings"][0]["classification"] = "compatible_enough"
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(ValidationError):
        load_and_validate(path)


def test_evidence_gap_requires_explanation(tmp_path):
    document = yaml.safe_load(MATRIX.read_text(encoding="utf-8"))
    document["mappings"][0]["classification"] = "evidence_gap"
    document["mappings"][0]["evidence_gap"] = None
    path = tmp_path / "bad-gap.yaml"
    path.write_text(yaml.safe_dump(document), encoding="utf-8")
    with pytest.raises(ValueError, match="evidence gap lacks explanation"):
        load_and_validate(path)


def test_exact_revisions_are_current():
    document = load_and_validate(MATRIX)
    assert status_for_revisions(
        document,
        ayra_revision=document["current_authority"]["source_revision"],
        candidate_revision=document["candidate_source"]["revision"],
    ) == "CURRENT"


def test_upstream_or_candidate_revision_change_requires_reassessment():
    document = load_and_validate(MATRIX)
    assert status_for_revisions(document, ayra_revision="deadbeef", candidate_revision=document["candidate_source"]["revision"]) == "REASSESSMENT_REQUIRED"
    assert status_for_revisions(document, ayra_revision=document["current_authority"]["source_revision"], candidate_revision="deadbeef") == "REASSESSMENT_REQUIRED"


def test_current_conformance_is_not_migration_readiness():
    document = load_and_validate(MATRIX)
    classifications = {m["classification"] for m in document["mappings"]}
    assert "changed_in_v3_draft" in classifications
    assert "evidence_gap" in classifications
    assert "conflict_candidate" in classifications
