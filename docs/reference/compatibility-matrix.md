# Compatibility Matrix

This matrix pins the Operational Stack baseline across the three TRQP repositories.

| Assurance Hub | Conformance Suite | TSPP | Status | Notes |
|---|---|---|---|---|
| v1.5.0 | v1.2.1 | v0.10.1 | supported | Release Set C: fail-closed CAM identity validation, checked-in operational stack bundle validation, refreshed cross-repo output contract |
| v1.4.0 | v1.2.0 | v0.10.0 | supported | Release Set B: AL1/AL2 MVBs, audit guides, adopter template, schema contract, SCI controls, decision tree, crosswalk |
| v1.3.0 | v1.1.0 | v0.9.0 | supported | Release Set A: deterministic replay, fixture-pinned runs, posture metrics, dry-run |
| v1.2.0 | v1.0.0 | v0.8.0 | legacy | Operational Trust Stack v1 stabilization baseline |
| v1.1.0 | v0.9.1 | v0.7.1 | legacy | Combined-assurance smoke workflow and machine-readable assurance profiles |
| v1.1.x | v0.8.x | v0.6.x | legacy | Works for older combined-assurance flows but lacks shared `run_id` and `target_id` fields |

Use the top supported line for new deployments, demonstrations, and cross-repo documentation.
