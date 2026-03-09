---
owner: maintainers
last_reviewed: 2026-03-04
tier: 0
---

# Start Here

This repository provides a conformance testing approach for TRQP with profile-based assurance and evidence bundles.

---

## Implementing TRQP

1. Run the **Baseline** profile.
2. Review `reports/<run-id>/verdicts.json` for requirement-level failures.
3. Compare your evidence outputs to `docs/reference-reports/`.
4. Move to **High-Assurance** only after you can provide a stable `state_reference`.

---

## Spec authors and working groups

1. Review `docs/TRQP_Conformance_Philosophy.md`.
2. Review `docs/profiles.md`.
3. Use the WG Alignment issue template to propose clarifications and profile gating changes.

---

## Governance and assurance teams

1. Review `docs/evidence_bundle.schema.json`.
2. Inspect reference reports for expected artifact completeness.
3. Validate that a High-Assurance run includes a declared `state_reference`.

---

## Methodology references
- TRACE ↔ TSAM relationship: `docs/reference/TRACE-TSAM.md`
