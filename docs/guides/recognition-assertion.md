# Recognition Assertion artifact

This repository treats **recognition** as something you can *publish, sign, and audit* — not a purely social relationship.

A **Recognition Assertion** is a machine-readable artifact that expresses:

- who is recognizing what/who
- why (basis / policy / trust framework / audit)
- what evidence backs the claim
- when the assertion becomes effective and when it expires (optional)
- how the assertion can be revoked / superseded (optional)

This is intentionally *not* a full recognition graph model. It is the smallest useful object that can be:

- published as a registry artifact,
- referenced from an Assurance Profile,
- linked into a Combined Assurance Manifest, and
- checked by independent verifiers.

## When to use

Use this artifact when you need to operationalize upstream TRQP RFEs around **recognition relationship modeling and proofs**.

Typical uses:

- a registry operator recognizes an auditor or assessment body
- a registry operator recognizes a governance framework
- a registry operator recognizes another registry (or its operator) for specific purposes

## Artifact format

Schema:

- [`schemas/recognition-assertion.schema.json`](../../schemas/recognition-assertion.schema.json)

Example:

- [`examples/recognition-assertion.example.json`](../../examples/recognition-assertion.example.json)

## Evidence linkage

Evidence references are strings. For early implementations, treat them as pointers:

- `artifact://…` for local build artifacts (recommended)
- `https://…` for stable public URLs
- `urn:…` or other identifiers, if your ecosystem supports them

For AL3/AL4, treat recognition assertions as **signable artifacts** (for example JWS/JWT, COSE, or an external signature envelope) and include integrity checksums in your Combined Assurance Manifest.
