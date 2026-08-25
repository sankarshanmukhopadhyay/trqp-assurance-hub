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
