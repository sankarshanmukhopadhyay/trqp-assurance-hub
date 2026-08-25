---
layout: default
title: "TRQP Stack 2026.1 — Coconut"
nav_exclude: true
---

# TRQP Stack 2026.1 — Coconut

**Status:** Validated coordinated release  
**Release date:** 2026-08-25  
**Codename:** Coconut (*Cocos nucifera*)

TRQP Stack 2026.1 is the first coordinated adopter-facing release of the TRQP Operational Trust Stack. It does not replace the independent versioning or authority of TRQP-TSPP, the TRQP Conformance Suite, or the TRQP Assurance Hub. Instead, it declares a specific combination of those independently versioned components that has been exercised together through the Stack Adoption Conformance gate.

## Consumer-facing value

For an adopter, the coordinated release removes the need to determine compatible component versions independently. Start from this release tuple, follow the canonical stack workflow, and obtain a reproducible evidence chain whose provenance identifies the TSPP posture producer, CTS conformance/replay producer, Assurance Hub aggregator, semantic/schema authorities, execution target, run identity, and release-eligibility evidence.

This release is therefore a **compatibility and assurance contract**, not a fourth implementation product.

## Validated tuple

| Layer | Release | Role |
|---|---:|---|
| TRQP-TSPP | v0.15.0 | Security/privacy posture and control evidence |
| TRQP Conformance Suite | v1.8.0 | Protocol conformance and deterministic replay evidence |
| TRQP Assurance Hub | v1.11.0 | Evidence aggregation and assurance publication |
| TSMM | v0.24.0 | Semantic authority |
| TIS | v0.14.1 | Schema and portfolio authority |

The canonical machine-readable record is [`manifest.json`](manifest.json).

## Decisive release evidence

The release tuple passed the `stack-release-eligibility` workflow on the merged Assurance Hub `main` baseline at commit `045ba10ec436ea5d1e9e443894bbbf7bea27472b`.

- Workflow run: `32802386172`
- Conclusion: `success`
- Candidate evidence artifact: `trqp-stack-release-candidate-32802386172`
- Artifact digest: `sha256:56bc91f89add53ad1cbf78031e1d2e26d7051e5f4cfe36c95ed48226556d17a8`

The gate validates immutable release resolution, clean bootstrap, canonical evaluation, TSPP evidence, CTS evidence, deterministic CTS replay, combined assurance, run/target correlation, provenance, artifact integrity, fail-closed negative cases, whole-stack semantic replay equivalence, and the executable adopter walkthrough.

## Adoption path

Use the Assurance Hub as the front door. The canonical workflow is documented in [`docs/adoption/stack-quickstart.md`](../../../docs/adoption/stack-quickstart.md). Adopters may then move into TSPP or CTS directly when they need to customize controls, profiles, test behavior, or evidence production.

## Authority boundaries

The coordinated release does not transfer authority between repositories. TSPP remains authoritative for its security/privacy controls and posture computation. CTS remains authoritative for executable conformance and replay-comparison semantics. Assurance Hub is authoritative for compatibility tuple declaration, integration verification, combined assurance, and coordinated release evidence. TSMM and TIS retain their declared semantic and schema/portfolio authority.

## Cadence and naming

Coordinated Stack releases are expected approximately monthly when meaningful capability has accumulated, and earlier when a capability or compatibility change makes a new validated tuple materially useful or necessary. Routine component changes do not automatically cause a Stack release.

Each coordinated Stack release receives a randomly selected codename from the Wikipedia list of Indian state trees. The codename is human-facing release identity only; the machine identity remains `trqp-stack-YYYY.N`.

## Supersession and invalidation

This release remains valid only for the declared tuple and evidence conditions. A future component release, authority-version change, replay-policy incompatibility, missing or invalid evidence, or other declared invalidation condition may require a new coordinated release. Historical release manifests are retained rather than silently rewritten.
