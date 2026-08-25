---
layout: default
title: "Compatibility Matrix"
nav_exclude: true
---

# Compatibility Matrix

This matrix identifies coordinated release sets for the TRQP Operational Trust Stack. Operators SHOULD use a validated or supported release set unless they have an explicit compatibility exception.

| Stack release | Assurance Hub | Conformance Suite | TRQP-TSPP | Status | Notes |
|---|---:|---:|---:|---|---|
| **TRQP Stack 2026.1 — Coconut** | **v1.11.0** | **v1.8.0** | **v0.15.0** | **validated** | First formal adopter-facing coordinated release. Passed immutable tuple resolution, clean bootstrap, component evidence generation, deterministic CTS replay, combined assurance, fail-closed cases, full-stack semantic replay equivalence, provenance/integrity checks, and executable walkthrough. TSMM v0.24.0; TIS v0.14.1. |
| pre-Stack coordinated set | v1.9.0 | v1.6.0 | v0.14.0 | supported | End-to-End Assurance Execution and Evidence Chain with authentic producer evidence, canonical compatibility, traceability, and fail-closed identity validation. |
| pre-Stack coordinated set | v1.8.0 | v1.5.0 | v0.13.0 | supported | Operational Trust Stack Maturity Release with release governance, validation evidence, adoption packaging, and Runtime Assurance Contract Pack. |
| pre-Stack coordinated set | v1.7.0 | v1.4.0 | v0.12.0 | maintenance | Runtime Assurance Contract Pack aligned with TSMM v0.21.0 and TIS v0.10.0. |
| pre-Stack coordinated set | v1.6.1 | v1.3.1 | v0.11.1 | supported | Public Assurance and Adoption Readiness. |
| pre-Stack coordinated set | v1.5.0 | v1.2.1 | v0.10.1 | supported | Fail-closed CAM identity validation and checked-in operational stack bundle validation. |
| pre-Stack coordinated set | v1.4.0 | v1.2.0 | v0.10.0 | supported | AL1/AL2 MVBs, audit guides, adopter template, schema contract, SCI controls, decision tree, and crosswalk. |
| pre-Stack coordinated set | v1.3.1 | v1.1.0 | v0.9.0 | maintenance | Deterministic replay, fixture-pinned runs, posture metrics, and dry-run. |
| pre-Stack coordinated set | v1.2.0 | v1.0.0 | v0.8.0 | legacy | Operational Trust Stack stabilization baseline. |
| pre-Stack coordinated set | v1.1.0 | v0.9.1 | v0.7.1 | legacy | Combined-assurance smoke workflow and machine-readable assurance profiles. |

## Compatibility rule

A Combined Assurance Manifest SHOULD declare the exact release tuple used to produce it. A formal `TRQP Stack YYYY.N` identity means the tuple has additionally passed the coordinated Stack eligibility gate and has an immutable machine-readable release record under `stack/releases/`.

TRQP Stack 2026.1 requires CTS replay-determinism evidence and records the comparison-policy identity, semantic hashes, reproducibility status, exact component tags/commits, authority pins, decisive workflow run, and eligibility artifact digest. The Hub does not redefine CTS policy or TSPP control semantics; incompatible or failed producer evidence invalidates the integration state.
