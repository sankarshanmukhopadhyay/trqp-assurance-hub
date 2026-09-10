---
layout: default
title: "Roadmap"
nav_exclude: true
owner: maintainers
last_reviewed: 2026-09-10
---

# TRQP Stack Roadmap

This roadmap is the coordinated delivery view for the TRQP Operational Trust Stack. Component repositories retain independent authority and semantic versioning; the Hub coordinates compatibility, integration evidence, and Stack release eligibility.

## Current baseline: TRQP Stack 2026.3 — Banyan

**TRQP Stack 2026.3 — Banyan** is the current published coordinated release.

It establishes profile-aware compositional assurance on top of the lifecycle guarantees introduced by Stack 2026.2. The current frozen tuple is:

| Layer | Release | Exact commit |
|---|---:|---|
| TRQP-TSPP | `v0.17.0` | `328e19c71f407ebdb2bc92828a3ae037a843f285` |
| TRQP Conformance Suite | `v1.10.0` | `1e5dc2646c75390444d9ae86f3d6136d7c033463` |
| TRQP Assurance Hub | `v1.13.0` | `5346b83545bf042360eb32691dfc907135d233dd` |
| TSMM | `0.24.0` | `8ddfd52c876faf368241bc11101681fb1fe49398` |
| TIS | `0.15.0` | `edda0e87ced40797d22e3df542099871c57fcb59` |

The immutable release record is under [`stack/releases/2026.3/`](../stack/releases/2026.3/). The current adopter path is [`docs/adoption/stack-quickstart.md`](adoption/stack-quickstart.md), with the profile-aware walkthrough at [`docs/adoption/stack-2026.3-walkthrough.md`](adoption/stack-2026.3-walkthrough.md).

## Capability state

Stack 2026.3 proves the following coordinated properties:

- immutable component and authority-pin resolution;
- clean-room bootstrap against the frozen tuple;
- producer-owned CTS conformance/replay evidence;
- producer-owned TSPP security/privacy posture evidence;
- profile-aware composition without authority transfer;
- fail-closed handling of missing, stale, `FAIL`, `INDETERMINATE`, and otherwise non-current producer evidence;
- deterministic CTS replay and whole-stack semantic replay equivalence;
- provenance and artifact-integrity validation;
- lifecycle invalidation, reassessment, authority-drift and supersession handling inherited from Stack 2026.2;
- executable Ayra first-profile assurance; and
- human release judgment as a mandatory publication gate.

## Authority boundaries

The roadmap does not transfer authority between repositories:

| Authority | Owns |
|---|---|
| TRQP upstream | Core protocol semantics |
| TRQP Conformance Suite | Executable conformance and replay evidence semantics |
| TRQP-TSPP | Security/privacy control and posture evidence semantics |
| Ecosystem profile authorities | Profile normative strength and profile requirements |
| TSMM | Canonical trust-system semantics |
| TIS | Portable machine-readable contracts |
| TRQP Assurance Hub | Evidence composition, compatibility coordination and coordinated release declaration |

Governance legitimacy remains dependent on applicable external authority evidence and is not inferred from API correctness alone.

## Historical progression

| Stack release | Capability established |
|---|---|
| 2026.1 — Coconut | First immutable coordinated tuple, clean bootstrap, deterministic replay, combined assurance and executable adopter walkthrough |
| 2026.2 — Ashoka | Assurance validity under change: invalidation, reassessment, authority drift, supersession and post-change recomposition |
| 2026.3 — Banyan | Profile-aware compositional assurance using independently authoritative producer evidence |

Historical candidate roadmaps and evidence under `stack/candidates/` are retained as audit artifacts. They describe what was proposed and tested at the time and must not be rewritten merely because a later release is now current.

## Next-release rule

There is no automatically scheduled next coordinated Stack release. A new release should be proposed only when a material capability, compatibility change, authority change, or assurance requirement justifies a new frozen tuple.

Any next release proposal must begin with an explicit governing proposition and then produce machine-verifiable evidence for:

1. the exact component and authority tuple;
2. the capability or assurance change being claimed;
3. compatibility and invalidation consequences;
4. negative and adversarial cases;
5. reproducible clean-room execution;
6. evidence provenance and integrity;
7. residual uncertainty and bounded limitations; and
8. the required visible human release judgment.

A green workflow remains necessary but is not itself the release judgment.

## Release discipline

Component releases continue independently. Coordinated Stack publication occurs only when a materially useful combination has accumulated and the complete tuple passes the Stack release gate.

The machine identity remains `trqp-stack-YYYY.N`; the tree codename is human-facing only. Historical release records are immutable evidence and are superseded by later releases rather than silently rewritten.
