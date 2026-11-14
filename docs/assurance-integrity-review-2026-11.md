---
layout: default
title: "Assurance integrity adversarial assessment (November 2026)"
nav_exclude: true
owner: maintainers
last_reviewed: 2026-11-14
tier: 1
---

# Assurance-integrity adversarial assessment, November 2026

## Basis and scope

This assessment reviews the canonical Lotus release, state-bound Hub composition and representative CTS/TSPP producer contracts. It is a **maintainer adversarial review**, not independent certification or deployment attestation. The immutable 2026.4 release record and previous versioned evidence are not modified. The remote release was verified as published on 2026-10-02, tag `trqp-stack-2026.4`, at commit `3ce4888dcf1fefb2be18a12136459c21a95814e8`.

## Material findings and disposition

| Proposition | Observation | Disposition and verification |
|---|---|---|
| Publication truth agrees with adoption metadata | Release exists, but Hub publication metadata remained `pending-publication`, and README/quickstart claimed Banyan was current. | Repair the derived records; preserve release tag, issue judgment, source commits and evidence digests. |
| Partial operational evidence cannot produce PASS | `producer_status` returned `pass` for `PASS=1, ERROR=1` and `PASS=1, NOT_TESTED=1`. The older combined-assurance path had the same reduction behavior. | Resolve uncertain producer outcomes as `indeterminate`; add regression fixtures for mixed, missing, malformed, negative and complete summaries. |
| Verified state identity has valid SHA-256 notation | Hub accepted 64-character nonhex digests if identity text matched. | Reject invalid hex digests in both the state-bound decision and manifest-generation boundaries; test negative cases. |
| Equal snapshot digests establish deployment authenticity | CTS/TSPP hashing provides integrity of supplied state material; equal hashes alone cannot prove the material matches the live implementation. | **External evidence required.** No new attestation authority or fabricated runtime proof is introduced. Consumers must independently establish deployment-to-snapshot provenance and freshness. |
| Historic PASS remains current after material change | Existing CTS/TSPP lifecycle and Hub composition mechanisms support invalidation and reassessment. | Retain these authority boundaries. Reuse existing lifecycle tests; avoid a parallel status authority. End-to-end external relying-party revocation observation remains unverified by this review. |
| Self-generated test evidence establishes independent assurance | Neither the GitHub release nor the producer contracts assert independent certification. | Maintain that limit explicitly across current documentation. |

## Reproduction and falsification

Use the existing repository entry points:

```sh
make validate
make assurance-check
python -m pytest -q tests/test_state_bound_manifest.py tests/test_cross_stack_negative_cases.py tests/test_state_bound_adversarial.py
```

The adversarial regression cases exercise the same `producer_status` and `require_verified_state` functions used by the state-bound composition command. They do **not** independently attest an external deployment. A release-engineering operator can inspect `stack/releases/2026.4/manifest.json`, `publication.json`, and the remote release attachment to reproduce the frozen release evidence. The `stack_bootstrap.py` default consumes the candidate manifest and must not be described as automatically selecting Lotus.

## Residual assurance boundaries

The assessed snapshot is a claim about the target state. To support operational reliance, an external party must verify that the snapshot describes the running deployment, that the applicable authorization/verification material remains valid, and that post-publication material changes, revocations, or supersessions have been considered. No positive assessment may be inferred from unavailable or contradictory evidence. TSPP owns security/privacy posture and verification-material control semantics; CTS owns protocol conformance and replay; Hub owns bounded composition and release declaration.

## Release impact

This tranche corrects maintained behavior and publication metadata on `main`. It does **not** rewrite Lotus artifacts, create another coordinated release, upgrade TRQP v3, or claim production certification. A future release decision requires evidence of a materially consumable new baseline and repository-approved publication.
