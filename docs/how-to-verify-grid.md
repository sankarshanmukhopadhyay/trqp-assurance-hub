# How to verify a GRID listing (verifier-first)

This is a practical, minimal workflow for verifying a registrar listing in a GRID-style directory.

## Inputs

- A registrar listing (JSON)
- A signed status feed (JSON)
- The directory operator policy (and its hash)

## Steps

1. **Validate shapes**
   - Validate listing against `schemas/registrar.schema.json`
   - Validate feed against `schemas/grid-status-feed.schema.json`

2. **Verify issuer identity**
   - Confirm the status feed `issuer` is the trusted directory operator for your policy.

3. **Verify cryptographic proof**
   - Verify the feed’s `proof` using your accepted proof suite (e.g., JWS or Data Integrity).
   - Reject unsigned feeds in operational modes.

4. **Check freshness**
   - Use the latest feed by `issued_at`.
   - Reject replayed/older feeds when a newer feed exists.

5. **Confirm registrar status**
   - Find the entry for the registrar’s `id`.
   - Ensure status is acceptable for your use (e.g., `active`).

6. **Apply assurance eligibility**
   - Map `assurance.assurance_level` using `docs/grid-assurance-mapping.md`.
   - Apply any additional sector-specific rules.

This workflow is deliberately implementation-agnostic about the proof format; deployments MUST specify accepted proof suites and key discovery rules.
