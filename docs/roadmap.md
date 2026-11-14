---
layout: default
title: "Roadmap"
nav_exclude: true
owner: maintainers
last_reviewed: 2026-11-14
---

# TRQP Stack Roadmap

This roadmap is the coordinated delivery view for the TRQP Operational Trust Stack. Component repositories retain independent authority and semantic versioning; the Hub coordinates compatibility, integration evidence, and Stack release eligibility.

## Current baseline: TRQP Stack 2026.4 — Lotus

**TRQP Stack 2026.4 — Lotus** is the current published coordinated release. Its state-bound assurance capability extends Banyan's profile-aware evidence composition.

| Layer | Release | Exact commit |
|---|---:|---|
| TRQP-TSPP | `v0.18.1` | `c1735099cf4bca98c3b4e4f67c151e5508687851` |
| TRQP Conformance Suite | `v1.11.1` | `0738c3cf86fddb99d761ed21d63d870eefdc5f76` |
| TRQP Assurance Hub | `v1.14.0` | `fd2296226dacbe3d5009179803fde23eead1cc6f` |
| TSMM | `0.24.0` | `8ddfd52c876faf368241bc11101681fb1fe49398` |
| TIS | `0.15.0` | `edda0e87ced40797d22e3df542099871c57fcb59` |

The canonical release record is [Lotus](../stack/releases/2026.4/RELEASE_NOTES.md). The [adopter quickstart](adoption/stack-quickstart.md) distinguishes the current frozen release from candidate-oriented CLI defaults. The historical Banyan profile walkthrough remains available unchanged.

## Capability state

The coordinated Stack proves the following capabilities across Banyan and Lotus:

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
| 2026.4 — Lotus | State-bound CTS/TSPP evidence correlation and explicit positive/negative outcome assertions |

Historical candidate roadmaps and evidence under `stack/candidates/` are retained as audit artifacts. They describe what was proposed and tested at the time and must not be rewritten merely because a later release is now current.

## Completed capability tranche: state-bound assurance

The current development tranche strengthens the existing TRQP Stack line without depending on downstream candidate protocol work or any proposed TRQP v3 semantics.

The governing proposition is:

> A combined assurance conclusion must not compose CTS and TSPP evidence merely because both name the same logical target. Both producers must bind their evidence to the same verified deployed-state identity, or the composition must fail closed.

The tranche is implementing:

- CTS-owned SHA-256 target-state identity for conformance and replay evidence;
- TSPP-owned target-state binding with reassessment on state change or unverifiable state;
- Hub-owned cross-producer target-state correlation and fail-closed composition;
- adversarial evidence for logical-target equality with deployment-state mismatch;
- preservation of producer authority boundaries.

This work is **not** itself a declaration of a future coordinated Stack release. Component releases and any coordinated release judgment remain capability- and evidence-driven under the rules below.

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
