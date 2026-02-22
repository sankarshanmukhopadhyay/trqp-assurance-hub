# Lifecycle state model

This repository introduces a minimal lifecycle model to make registry posture and assurance declarations **operationally legible**.

The lifecycle model is intentionally small to avoid protocol-level bikeshedding.
It exists to help implementers and verifiers align on:

- what state a registry (or profile) is in,
- what that implies for caching and reliance,
- when recognition should be re-evaluated or revoked.

## States

The following states are defined for the assurance layer:

- `draft` — not yet intended for reliance.
- `active` — intended for reliance within the declared scope.
- `suspended` — temporarily not intended for reliance.
- `deprecated` — intended for a limited transition window.
- `revoked` — explicitly not intended for reliance (trust-impacting).
- `retired` — end-of-life.

## Lifecycle Assertion

Lifecycle state is expressed via a standalone artifact:

- Schema: [`schemas/lifecycle-assertion.schema.json`](../../schemas/lifecycle-assertion.schema.json)
- Example: [`examples/lifecycle-assertion.example.json`](../../examples/lifecycle-assertion.example.json)

## How this relates to TRQP RFEs

Upstream discussions around lifecycle and revocation semantics often drift into transport mechanics.
This repo stays at the assurance layer:

- lifecycle state is **publishable metadata**,
- transitions are **evidence-linked**,
- revocation is **explicit** and can be propagated through recognition relationships.

## Practical expectations

At higher assurance levels, lifecycle transitions should be supported by stronger evidence, for example:

- control satisfaction declarations,
- incident reports,
- audit results,
- revocation reason codes.
