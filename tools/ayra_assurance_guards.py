"""Adversarial guards for Ayra profile assurance.

These guards prevent execution against an unknown profile revision and preserve
Ayra response-signing semantics as a SHOULD rather than silently promoting them
to a universal MUST.
"""
from __future__ import annotations

AYRA_PROFILE_ID = "ayra-trqp"
AYRA_PROFILE_VERSION = "0.6.0-draft"
AYRA_SOURCE_REVISION = "ec7768572592b50ba3f4102c026c2449148b5e11"


def profile_binding_state(document: dict) -> str:
    binding = document.get("profile_binding")
    if not isinstance(binding, dict):
        return "INDETERMINATE"
    if (
        binding.get("profile_id") == AYRA_PROFILE_ID
        and binding.get("profile_version") == AYRA_PROFILE_VERSION
        and binding.get("source_revision") == AYRA_SOURCE_REVISION
    ):
        return "PASS"
    return "INDETERMINATE"


def signing_state(observation: dict) -> str:
    """Evaluate bounded signing evidence without converting SHOULD into MUST.

    applicability=false is NOT_APPLICABLE. Unknown applicability or absent
    evidence is INDETERMINATE. Explicitly invalid evidence is FAIL, but that
    failure remains a SHOULD-level security observation and is not a global
    conformance veto by itself.
    """
    applicable = observation.get("signing_applicable")
    if applicable is False:
        return "NOT_APPLICABLE"
    if applicable is not True:
        return "INDETERMINATE"
    if "signature_valid" not in observation:
        return "INDETERMINATE"
    return "PASS" if observation.get("signature_valid") is True else "FAIL"
