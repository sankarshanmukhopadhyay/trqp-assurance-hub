---
owner: maintainers
last_reviewed: 2026-07-03
tier: 0
---

# Release Policy

The TRQP Assurance Hub is now managed as the adoption front door for the Operational Trust Stack. Releases should demonstrate usable assurance value, not routine activity.

## Release classes

| Class | Allowed when | Example |
|---|---|---|
| Patch | Security fix, broken CI, broken internal link, schema regression, incorrect release metadata | `v1.8.1` |
| Minor | New adopter-facing capability with tests, documentation, and evidence impact | `v1.9.0` |
| Maturity | Coordinated cross-repo improvement across Hub, CTS, and TSPP | Operational Trust Stack maturity release |
| No release | Typo, prose polish, non-substantive link rearrangement, exploratory notes | Batch into next milestone |

## Required release evidence

Every release must provide:

- A compatibility tuple for Hub, CTS, and TSPP.
- Validation commands and outcomes in `docs/release-validation.md` or the release note.
- Documentation impact summary.
- Evidence impact summary covering produced, consumed, or validated artifacts.
- Adoption impact summary for at least one role: implementer, assessor, operator, relying party, or governance steward.

## Release blockers

A release must not be cut when:

- Required validation commands fail.
- README version metadata does not match `VERSION`.
- Cross-repo compatibility references are inconsistent.
- A schema, example, or manifest changes without documentation.
- New assurance claims are prose-only and not tied to machine-verifiable evidence.
