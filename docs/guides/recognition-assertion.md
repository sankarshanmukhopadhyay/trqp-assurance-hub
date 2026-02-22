# Recognition Assertion

The **Recognition Assertion** is a standalone artifact used to express registry-to-registry (or operator-to-operator) recognition in a **signable** and **evidence-linked** way.

This repo treats recognition as a governance claim that must be **falsifiable**:

- it has an issuer and a subject,
- it is bounded by scope,
- it can be revoked or expire,
- it can point to evidence bundles (audit reports, conformance results, manifests).

## Artifact

- Schema: [`schemas/recognition-assertion.schema.json`](../../schemas/recognition-assertion.schema.json)
- Example: [`examples/recognition-assertion.example.json`](../../examples/recognition-assertion.example.json)

## Intended usage

Use a Recognition Assertion when you need to publish statements like:

- “Registry A recognizes Registry B for domain X in jurisdiction Y.”
- “Registry A recognizes Registry B **with conditions** (controls, audits, lifecycle expectations).”
- “Registry A revokes recognition of Registry B due to a trust-impacting event.”

## Evidence linking

Recognition assertions should reference evidence artifacts, for example:

- combined assurance manifests,
- conformance evidence bundles,
- security posture evidence bundles,
- control satisfaction declarations.

This keeps recognition from becoming a vibes-based relationship and turns it into an operational, reviewable surface.

## Signing

The schema includes an optional `signature` block.

This repository does not mandate a signing envelope.
Publishers may use JOSE/JWS, Data Integrity proofs, or a detached signature scheme consistent with their trust framework.
