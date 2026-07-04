---
owner: maintainers
last_reviewed: 2026-07-03
tier: 0
---

# Change Intake

This repository accepts changes that improve the Hub as an executable assurance publication layer. The default expectation is batching: small improvements should accumulate into a milestone unless they unblock adoption or correct a release risk.

## Intake checklist

| Question | Required answer |
|---|---|
| What authority or scope changes? | Identify the assurance object, release tuple, profile, or artifact scope. |
| What evidence changes? | Name the schema, manifest, summary, example, or validation output affected. |
| What can be tested? | Provide the local command or CI workflow that proves the change. |
| Who benefits? | Identify implementer, operator, assessor, relying party, procurement, or governance use. |
| Is a release justified? | Explain why the change is patch, minor, maturity, or no-release. |

## Batching rule

Do not cut releases for isolated wording changes, narrow formatting cleanup, or minor cross-link adjustments. Batch those changes into the next adoption-facing release unless they fix a broken public path or incorrect assurance statement.
