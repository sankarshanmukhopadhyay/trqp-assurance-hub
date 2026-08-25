---
layout: default
title: "TRQP Stack quickstart"
nav_exclude: true
---

# TRQP Stack quickstart

Use this page when you want the validated TRQP components to behave as one adopter workflow rather than selecting repository versions independently.

## Current validated release

**TRQP Stack 2026.1 — Coconut** is the current coordinated release. Its immutable record is `stack/releases/2026.1/manifest.json` and its human-readable explanation is `stack/releases/2026.1/README.md`.

The validated tuple is:

| Layer | Release |
|---|---:|
| TRQP-TSPP | v0.15.0 |
| TRQP Conformance Suite | v1.8.0 |
| TRQP Assurance Hub | v1.11.0 |
| TSMM | v0.24.0 |
| TIS | v0.14.1 |

## 1. Understand the release contract

A coordinated Stack release means the declared component versions have been exercised together under the Stack eligibility gate. It removes adopter-side version selection while preserving the independent authority and version lifecycle of each repository.

For future releases, the next proposed tuple is first recorded in `stack/releases/candidate/manifest.json`. A candidate is not a release.

## 2. Validate the candidate or current tuple

For release engineering against the current candidate:

```bash
python tools/stack_validate.py --check-remote
```

This fails if the candidate manifest is incomplete, a component ref is mutable, or a declared tag does not resolve to the pinned commit.

For adoption of Stack 2026.1, inspect `stack/releases/2026.1/manifest.json` for the immutable component tags, commits, authority versions, decisive workflow run, and evidence artifact digest.

## 3. Bootstrap a clean workspace

```bash
python tools/stack_bootstrap.py --clean
```

The bootstrap command clones only the tagged component versions declared by the candidate release engineering manifest and verifies their commits. No adopter-side compatibility choice is required.

The same clean-room property was a mandatory eligibility condition for Stack 2026.1.

## 4. Execute the declared components

```bash
python tools/stack_evaluate.py
```

This invokes each component's `assurance-check` surface and writes a run record to `artifacts/stack-candidate/run-manifest.json` during release engineering.

The coordinated Stack workflow then correlates TSPP and CTS evidence using the same run and target identity before the Hub produces combined assurance.

## 5. Verify release eligibility

```bash
make stack-release-check
```

The local gate validates the Hub, candidate tuple, remote tag provenance, and fail-closed release-readiness tests. The `stack-release-eligibility` GitHub Actions workflow additionally performs clean bootstrap, tagged component execution, CTS deterministic replay, combined assurance composition, whole-stack semantic replay comparison, negative cases, and candidate evidence publication.

Stack 2026.1 passed that decisive workflow on the merged Hub baseline before its release record was promoted to `validated`.

## Evidence a coordinated release provides

A coordinated release is publishable only when CI demonstrates immutable tuple resolution, clean bootstrap, TSPP evidence validity, CTS conformance and deterministic replay, shared run/target correlation, combined assurance, provenance/integrity, negative-case rejection, whole-stack semantic replay equivalence, and an executable walkthrough.

The release record preserves the exact workflow run and evidence artifact digest so the claim can be audited later.

## Authority boundary

The Assurance Hub owns coordinated release declaration and compatibility evidence. TSPP remains authoritative for its controls and posture semantics. CTS remains authoritative for protocol conformance and replay-comparison semantics. TSMM/TIS retain their declared semantic/schema authority.

A Stack release therefore records **tested interoperability and assurance evidence**; it does not transfer normative authority.

## Release cadence

Coordinated Stack releases are expected approximately monthly when meaningful capability has accumulated, or earlier when a capability/compatibility change makes a new validated tuple materially useful or necessary. Component releases continue independently and do not automatically trigger a Stack release.
