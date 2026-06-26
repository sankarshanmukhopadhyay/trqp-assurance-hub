# Compatibility Matrix

This matrix identifies coordinated release sets for the TRQP Operational Trust Stack. Operators SHOULD use a supported release set unless they have an explicit compatibility exception.

| Assurance Hub | Conformance Suite | TRQP-TSPP | Status | Notes |
|---|---:|---:|---|---|
| v1.6.1 | v1.3.1 | v0.11.1 | supported | Operational Trust Stack: Public Assurance and Adoption Readiness. Adds public assurance summaries, scenario profiles, interop evidence matrices, relying-party controls, and adoption packs. |
| v1.5.0 | v1.2.1 | v0.10.1 | supported | Release Set C: fail-closed CAM identity validation, checked-in operational stack bundle validation, refreshed cross-repo output contract. |
| v1.4.0 | v1.2.0 | v0.10.0 | supported | Release Set B: AL1/AL2 MVBs, audit guides, adopter template, schema contract, SCI controls, decision tree, crosswalk. |
| v1.3.1 | v1.1.0 | v0.9.0 | maintenance | Release Set A: deterministic replay, fixture-pinned runs, posture metrics, dry-run. |
| v1.2.0 | v1.0.0 | v0.8.0 | legacy | Operational Trust Stack stabilization baseline. |
| v1.1.0 | v0.9.1 | v0.7.1 | legacy | Combined-assurance smoke workflow and machine-readable assurance profiles. |

## Compatibility rule

A Combined Assurance Manifest SHOULD declare the exact release tuple used to produce it. Hub v1.6.1 validates identity binding across CTS and TSPP reports and adds a public assurance summary layer for relying-party review.
