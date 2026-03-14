from pathlib import Path

import importlib.util

MODULE_PATH = Path(__file__).resolve().parent.parent / "services" / "trust-registry-reference" / "app.py"
spec = importlib.util.spec_from_file_location("trust_registry_reference_app", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_sample_data_files_exist():
    data = MODULE_PATH.parent / "data"
    assert (data / "trust-services.json").exists()
    assert (data / "services" / "demo-registry.json").exists()
    assert (data / "assurance" / "demo-registry.json").exists()
    assert (data / "conformance" / "demo-registry.json").exists()


def test_load_registry_listing():
    data = MODULE_PATH.parent / "data"
    listing = module.load_json(data / "trust-services.json")
    assert listing["registry_id"] == "trqp-reference-registry"
    assert listing["items"][0]["service_id"] == "demo-registry"
