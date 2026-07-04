# Compatibility Matrix

This matrix identifies coordinated release sets for the TRQP Operational Trust Stack. Operators SHOULD use a supported release set unless they have an explicit compatibility exception.

| Assurance Hub | Conformance Suite | TRQP-TSPP | Status | Notes |
|---|---:|---:|---|---|
| v1.8.0 | v1.5.0 | v0.13.0 | supported | Operational Trust Stack Maturity Release. Adds release governance, validation evidence, adoption packaging, and high-value commit discipline while retaining the Runtime Assurance Contract Pack. |
| v1.7.0 | v1.4.0 | v0.12.0 | maintenance | Runtime Assurance Contract Pack. Aligns Hub, CTS, and TSPP with TSMM v0.21.0 semantics and TIS v0.10.0 executable artifact contracts for authority, evidence, decision, registry publication, and lifecycle/status evidence. |
| v1.6.1 | v1.3.1 | v0.11.1 | supported | Operational Trust Stack: Public Assurance and Adoption Readiness. Adds public assurance summaries, scenario profiles, interop evidence matrices, relying-party controls, and adoption packs. |
| v1.5.0 | v1.2.1 | v0.10.1 | supported | Release Set C: fail-closed CAM identity validation, checked-in operational stack bundle validation, refreshed cross-repo output contract. |
| v1.4.0 | v1.2.0 | v0.10.0 | supported | Release Set B: AL1/AL2 MVBs, audit guides, adopter template, schema contract, SCI controls, decision tree, crosswalk. |
| v1.3.1 | v1.1.0 | v0.9.0 | maintenance | Release Set A: deterministic replay, fixture-pinned runs, posture metrics, dry-run. |
| v1.2.0 | v1.0.0 | v0.8.0 | legacy | Operational Trust Stack stabilization baseline. |
| v1.1.0 | v0.9.1 | v0.7.1 | legacy | Combined-assurance smoke workflow and machine-readable assurance profiles. |

## Compatibility rule

A Combined Assurance Manifest SHOULD declare the exact release tuple used to produce it. Hub v1.8.0 validates identity binding across CTS and TSPP reports, supports public assurance summaries, can carry TSMM/TIS runtime assurance references for evidence, decision, registry publication, and status/revocation artifacts, and adds a release governance gate for future maturity increments.
