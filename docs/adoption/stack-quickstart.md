---
layout: default
title: "TRQP Stack quickstart"
nav_exclude: true
---

# TRQP Stack quickstart

Use this page when you want the validated TRQP components to behave as one adopter workflow rather than selecting repository versions independently.

## Current validated release

**TRQP Stack 2026.3 — Banyan** is the current coordinated release. Its immutable release record is under `stack/releases/2026.3/`, and its profile-aware execution walkthrough is [`stack-2026.3-walkthrough.md`](stack-2026.3-walkthrough.md).

The validated tuple is:

| Layer | Release | Exact commit |
|---|---:|---|
| TRQP-TSPP | v0.17.0 | `328e19c71f407ebdb2bc92828a3ae037a843f285` |
| TRQP Conformance Suite | v1.10.0 | `1e5dc2646c75390444d9ae86f3d6136d7c033463` |
| TRQP Assurance Hub | v1.13.0 | `5346b83545bf042360eb32691dfc907135d233dd` |
| TSMM | 0.24.0 | `8ddfd52c876faf368241bc11101681fb1fe49398` |
| TIS | 0.15.0 | `edda0e87ced40797d22e3df542099871c57fcb59` |

## 1. Understand the release contract

A coordinated Stack release means the declared component versions have been exercised together under the Stack eligibility gate. It removes adopter-side version selection while preserving the independent authority and version lifecycle of each repository.

For future releases, the next proposed tuple is first recorded in `stack/releases/candidate/manifest.json`. A candidate is not a release.

## 2. Validate the candidate or current tuple

For release engineering against the current candidate manifest:

```bash
python tools/stack_validate.py --check-remote
```

This fails if the candidate manifest is incomplete, a component ref is mutable, or a declared tag does not resolve to the pinned commit.

For adoption of Stack 2026.3, inspect `stack/releases/2026.3/manifest.json` and `stack/releases/2026.3/publication.json` for the immutable component tags, commits, authority versions, decisive workflow run, human release judgment, evidence artifact digest, and publication metadata.

## 3. Bootstrap a clean workspace

```bash
python tools/stack_bootstrap.py --clean
```

The bootstrap command clones only the tagged component versions declared by the release engineering manifest and verifies their commits. No adopter-side compatibility choice is required.

The same clean-room property was a mandatory eligibility condition for Stack 2026.3.

## 4. Execute the declared components

```bash
python tools/stack_evaluate.py
```

This invokes each component's `assurance-check` surface and writes a run record to `artifacts/stack-candidate/run-manifest.json` during release engineering.

The coordinated Stack workflow correlates TSPP and CTS evidence using the same run and target identity before the Hub produces combined assurance. In Stack 2026.3, profile-aware composition additionally consumes producer-owned CTS and TSPP evidence while preserving their authority boundaries.

## 5. Verify release eligibility

```bash
make stack-release-check
```

The local gate validates the Hub, candidate tuple, remote tag provenance, and fail-closed release-readiness tests. The `stack-release-eligibility` GitHub Actions workflow additionally performs clean bootstrap, tagged component execution, CTS deterministic replay, profile-aware producer/consumer validation, combined assurance composition, whole-stack semantic replay comparison, negative cases, and candidate evidence publication.

Stack 2026.3 passed the decisive eligibility workflow on merged `main`, received the required visible human `ACCEPT` judgment, and then passed a fresh post-acceptance merged-main eligibility run before automated publication.

## Evidence a coordinated release provides

A coordinated release is publishable only when CI demonstrates immutable tuple resolution, clean bootstrap, TSPP evidence validity, CTS conformance and deterministic replay, shared run/target correlation, profile-aware evidence composition, combined assurance, provenance/integrity, negative-case rejection, whole-stack semantic replay equivalence, and an executable walkthrough.

The release record preserves the exact workflow run, evidence artifact digest, human release judgment, and publication metadata so the claim can be audited later.

## Authority boundary

The Assurance Hub owns coordinated release declaration and compatibility evidence. TSPP remains authoritative for its controls and posture semantics. CTS remains authoritative for protocol conformance and replay-comparison semantics. Ecosystem profile authorities remain authoritative for profile normative strength. TSMM and TIS retain their declared semantic/schema authority.

A Stack release therefore records **tested interoperability and assurance evidence**; it does not transfer normative authority or infer governance legitimacy from API correctness.

## Release cadence

Coordinated Stack releases are capability-driven and are published when meaningful capability has accumulated and the complete tuple passes the release gate. Component releases continue independently and do not automatically trigger a Stack release.
