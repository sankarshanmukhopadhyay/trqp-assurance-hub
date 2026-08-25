---
owner: maintainers
last_reviewed: 2026-08-25
tier: 0
---

# Release Policy

The TRQP Assurance Hub is the adoption front door and coordinated-release authority for the TRQP Operational Trust Stack. Releases must demonstrate usable assurance value, not routine activity.

## Release classes

| Class | Allowed when | Example |
|---|---|---|
| Patch | Security fix, broken CI, broken internal link, schema regression, incorrect release metadata | `v1.11.1` |
| Minor | New adopter-facing Hub capability with tests, documentation, and evidence impact | `v1.12.0` |
| Coordinated Stack | A validated Hub/CTS/TSPP compatibility tuple provides meaningful adopter value or a capability/compatibility change makes a new tuple necessary | `TRQP Stack 2026.1 — Coconut` |
| No release | Typo, prose polish, non-substantive link rearrangement, exploratory notes | Batch into next milestone |

Component releases retain independent semantic versioning. A component release does not automatically cause a coordinated Stack release.

## Coordinated Stack cadence

The target cadence is approximately monthly when meaningful capability has accumulated. A coordinated release may be cut earlier when a capability, compatibility, security, evidence, or authority change makes a newly validated tuple materially necessary for adopters.

The release decision is capability-driven rather than calendar-driven: a month may pass without a Stack release when there is no meaningful new adopter contract to publish.

## Coordinated Stack naming

Each coordinated Stack release receives:

- a stable machine identity of the form `trqp-stack-YYYY.N`;
- a human-facing title of the form `TRQP Stack YYYY.N — <codename>`; and
- a randomly selected codename from the Wikipedia **List of Indian state trees**.

The codename is descriptive release identity only and carries no protocol, assurance-level, or authority semantics. The selected common and scientific names are recorded in the immutable Stack manifest so release naming remains auditable.

## Required release evidence

Every Hub component release must provide:

- a compatibility tuple for Hub, CTS, and TSPP;
- validation commands and outcomes in `docs/release-validation.md` or the release note;
- a documentation impact summary;
- an evidence impact summary covering produced, consumed, or validated artifacts; and
- an adoption impact summary for at least one role: implementer, assessor, operator, relying party, or governance steward.

Every coordinated Stack release must additionally provide:

- a machine-readable immutable Stack manifest;
- exact component tags and commit SHAs;
- pinned TSMM/TIS authority versions;
- a successful `stack-release-eligibility` workflow on the merged release baseline;
- the workflow run identifier and candidate evidence artifact digest;
- a clean-room bootstrap result;
- deterministic CTS replay evidence;
- whole-stack semantic replay equivalence;
- fail-closed negative-case evidence;
- an executable adopter walkthrough; and
- synchronized adopter-facing documentation across the Hub, CTS, and TSPP entry points.

## Release blockers

A release must not be cut when:

- required validation commands fail;
- the decisive coordinated-release workflow is missing or not green for a Stack release;
- README version or compatibility metadata is inconsistent with the declared component releases;
- cross-repository compatibility references disagree;
- a schema, example, manifest, or producer contract changes without corresponding documentation;
- new assurance claims are prose-only and not tied to machine-verifiable evidence; or
- the release record cannot identify the authority, scope, provenance, evidence, and invalidation conditions behind its claims.

## Authority and supersession

The Hub may declare that a particular component tuple has passed coordinated integration and assurance gates. This does not transfer TSPP control authority, CTS conformance/replay authority, TSMM semantic authority, TIS schema/portfolio authority, or upstream TRQP specification authority to the Hub.

A coordinated release is immutable historical evidence. When compatibility or assurance conditions change, publish a new Stack release or explicitly supersede the prior release; do not rewrite the historical tuple.
