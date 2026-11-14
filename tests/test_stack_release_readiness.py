import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("stack_validate", ROOT / "tools" / "stack_validate.py")
stack_validate = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(stack_validate)


def manifest():
    return json.loads((ROOT / "stack" / "releases" / "candidate" / "manifest.json").read_text())


def test_candidate_manifest_is_structurally_eligible():
    assert stack_validate.validate_structure(manifest()) == []


def test_missing_component_fails_closed():
    candidate = manifest()
    candidate["components"].pop("cts")
    assert stack_validate.validate_structure(candidate)


def test_mutable_component_ref_fails_closed():
    candidate = manifest()
    candidate["components"]["cts"]["ref"] = "main"
    assert any("immutable version tag" in error for error in stack_validate.validate_structure(candidate))


def test_invalid_component_provenance_fails_closed():
    candidate = manifest()
    candidate["components"]["tspp"]["commit"] = "deadbeef"
    assert any("40-character commit SHA" in error for error in stack_validate.validate_structure(candidate))


def test_all_decisive_release_gates_are_declared():
    candidate = manifest()
    assert stack_validate.REQUIRED_GATES <= set(candidate["release_gates"])



def test_manifest_schema_accepts_all_frozen_historical_releases():
    for release in ("2026.1", "2026.2", "2026.3", "2026.4"):
        data = json.loads((ROOT / "stack" / "releases" / release / "manifest.json").read_text())
        assert stack_validate.validate_structure(data) == []


def test_deleted_lotus_gate_fails_closed():
    data = json.loads((ROOT / "stack/releases/2026.4/manifest.json").read_text())
    data["release_gates"].remove("target-state-identity-verified")
    assert any("missing release gates" in error for error in stack_validate.validate_structure(data))


def test_unmapped_gate_is_not_authorized_by_manifest():
    candidate = manifest()
    candidate["release_gates"].append("self-declared-assurance")
    assert any("unmapped release gates" in error for error in stack_validate.validate_structure(candidate))


def test_manifest_schema_must_validate():
    candidate = manifest()
    candidate["stack"]["unexpected_claim"] = True
    assert any("release manifest schema" in error for error in stack_validate.validate_structure(candidate))


def test_gate_registry_maps_every_lotus_gate_to_verification_step():
    data = json.loads((ROOT / "stack/releases/2026.4/manifest.json").read_text())
    registry = stack_validate._gate_registry()
    steps = (ROOT / ".github/workflows/stack-release-eligibility.yml").read_text()
    assert set(data["release_gates"]) == set(registry["gates"])
    for key in data["release_gates"]:
        assert f'- name: {registry["gates"][key]["check_step"]}' in steps
