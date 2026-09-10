---
layout: default
title: "TRQP Stack 2026.3 — Profile-Aware Assurance Walkthrough"
nav_exclude: true
---

# TRQP Stack 2026.3 — Profile-Aware Assurance Walkthrough

This walkthrough exercises the frozen **TRQP Stack 2026.3 — Banyan** release candidate as a composition of independently authoritative evidence producers. It is designed for adopters, assessors and governance reviewers who need to understand not only whether a workflow runs, but which component owns each conclusion and what happens when evidence is missing, stale or contradictory.

## Frozen candidate

| Layer | Release / version | Exact commit | Authority |
|---|---|---|---|
| TRQP Conformance Suite | `v1.10.0` | `1e5dc2646c75390444d9ae86f3d6136d7c033463` | core TRQP conformance and replay evidence |
| TRQP-TSPP | `v0.17.0` | `328e19c71f407ebdb2bc92828a3ae037a843f285` | security/privacy posture evidence |
| TRQP Assurance Hub | `v1.13.0` | `5346b83545bf042360eb32691dfc907135d233dd` | profile projection and evidence composition |
| TSMM | `0.24.0` | `8ddfd52c876faf368241bc11101681fb1fe49398` | canonical trust-system semantics |
| TIS | `0.15.0` | `edda0e87ced40797d22e3df542099871c57fcb59` | portable lifecycle/evidence contracts |

The TIS pin is version-and-commit bound because the transferred QBF repository does not expose a `v0.15.0` release tag. No tag is inferred or manufactured solely to make the tuple visually uniform.

## Governing proposition

A profile-aware assurance conclusion must preserve the source authority, provenance, lifecycle state and bounded result of each producer. In particular:

- CTS failure or uncertainty cannot be replaced by a Hub-local positive result;
- TSPP failure, reassessment-required state or missing applicable control evidence cannot be promoted to PASS by profile metadata;
- Ayra normative strength remains defined by the Ayra profile, not by CTS, TSPP or the Hub;
- governance legitimacy remains dependent on applicable external authority evidence;
- a successful workflow does not by itself establish a successful assurance conclusion.

## Execute the candidate

From the Hub repository at the candidate baseline:

```bash
make stack-release-check
python tools/stack_bootstrap.py --clean
python tools/stack_evaluate.py
```

The clean bootstrap resolves each component by immutable version tag and verifies that the checked-out commit equals the candidate manifest. The decisive GitHub Actions workflow additionally generates correlated CTS/TSPP evidence, deterministic CTS replay evidence, two independently composed combined-assurance runs and semantic replay comparison evidence.

## Exercise the profile boundary

The frozen Hub `v1.13.0` profile tests must pass from the clean-room checkout:

```bash
cd .stack-work/assurance_hub
python -m pytest -q \
  tests/test_profile_assurance_model.py \
  tests/test_ayra_profile_runner.py \
  tests/test_ayra_authority_evidence.py \
  tests/test_ayra_adversarial.py \
  tests/test_ayra_assurance_bundle.py \
  tests/test_ayra_v3_compatibility.py \
  tests/test_consume_cts_profile_evidence.py \
  tests/test_compose_profile_producer_evidence.py \
  tests/test_tspp_profile_evidence_consumer.py
```

These tests are not a substitute for live-registry evidence. They prove the composition contract and its fail-safe boundaries against deterministic fixtures.

## Evidence to inspect

A successful `stack-release-eligibility` run publishes a workflow artifact named `trqp-stack-release-candidate-<run-id>`. The artifact must include:

- the frozen candidate manifest;
- clean-room bootstrap manifest;
- CTS conformance and replay-determinism evidence;
- TSPP posture evidence;
- combined-assurance runs used for semantic replay comparison;
- inherited lifecycle/change-assurance evidence from Stack 2026.2; and
- the Stack 2026.3 candidate records.

## Negative cases that must fail closed

The release candidate is not eligible if any of these conditions can silently produce a positive current conclusion:

1. a component tag resolves to a different commit than declared;
2. applicable CTS evidence is absent, stale or contradictory;
3. applicable TSPP evidence is absent, stale or marked `REASSESS_REQUIRED`/`INVALID`;
4. profile metadata attempts to override producer-owned results;
5. profile identity/version/source revision does not match the selected projection;
6. authority or governance evidence is unavailable but legitimacy is nevertheless inferred;
7. deterministic CTS replay contains prohibited semantic drift; or
8. two complete Stack compositions are not semantically equivalent under the declared comparison policy.

## Release decision boundary

Passing this walkthrough and the automated eligibility workflow produces **candidate release evidence**. It does not publish TRQP Stack 2026.3 automatically by itself.

The exact workflow run, evidence artifact and digest must first be recorded on the governing release issue. The repository then requires a visible **HUMAN RELEASE JUDGMENT: ACCEPT** before a pending publication record may be merged and the automated coordinated-release publisher may create the immutable Stack release.

## Non-claims

This walkthrough demonstrates reproducible project assurance and compatibility behavior. It does not certify an Ayra registry, establish governance legitimacy for an operator, or constitute independent accreditation or certification.