# Lifecycle state model

TRQP deployments are living systems. They change owners, rotate keys, migrate infrastructure, and sometimes get shut down.

This repository provides a **minimal lifecycle state model** that can be:

- declared in an Assurance Profile,
- evidenced via a standalone Lifecycle Assertion artifact, and
- bound into a Combined Assurance Manifest.

This is **not** protocol query semantics. This is governance and assurance metadata meant to reduce ambiguity.

## States

The state space is intentionally small:

- `planned` — announced / preparing, not yet operational
- `active` — operational and expected to answer queries
- `suspended` — temporarily non-operational (planned or unplanned)
- `deprecated` — still operational, but scheduled for sunset (replacement path SHOULD be published)
- `terminated` — no longer operational (historical evidence SHOULD remain accessible)

## Transition expectations

These are guidance-level expectations that become stricter at higher assurance levels:

- `active -> suspended`: MUST publish a reason and an expected review date (AL3+)
- `active -> deprecated`: SHOULD publish replacement pointers (AL2+)
- `deprecated -> terminated`: MUST publish a termination notice and retention pointer (AL3+)

## Artifact format

Schema:

- [`schemas/lifecycle-assertion.schema.json`](../../schemas/lifecycle-assertion.schema.json)

Example:

- [`examples/lifecycle-assertion.example.json`](../../examples/lifecycle-assertion.example.json)

## Linking to other artifacts

- Assurance Profile: include lifecycle policy pointers and (optionally) a current-state assertion reference.
- Recognition Assertion: include lifecycle references when recognition is time-bound or contingent.
