# How to Verify a GRID Listing (Verifier-First)

This is a practical, minimal workflow for an independent verifier consuming a GRID-style directory.

## Inputs

- Registrar listing record (`registrar.json`)
- Signed status feed (`grid-status-feed.json`)
- Governance policy artifact (URI + hash)
- Evidence artifacts (URIs + optional hashes)

## Steps

1. **Validate schema**
   - Validate `registrar.json` against `schemas/registrar.schema.json`
   - Validate the status feed against `schemas/grid-status-feed.schema.json`

2. **Check lifecycle status**
   - Confirm the registrar appears in the signed status feed
   - Confirm `status` is acceptable for your use case (typically `active`)
   - Confirm `effective_at` / `status_effective_at` are within your freshness window

3. **Verify feed signature**
   - Verify that the status feed signature(s) are valid for the stated `issuer`
   - Reject unsigned or unverifiable feeds

4. **Verify governance policy integrity**
   - Fetch the policy at `trqp.governance_policy.uri`
   - Hash the content and compare to `trqp.governance_policy.sha256`

5. **Evaluate evidence**
   - Fetch evidence artifacts referenced in `trqp.evidence[]`
   - Where hashes are provided, verify integrity
   - Confirm evidence sufficiency for the asserted `assurance_level` (see `docs/grid-assurance-mapping.md`)

## Output

A verifier should be able to produce a decision record:

- Accept / reject the registrar as authoritative
- The reason (status, insufficient evidence, signature failure, stale audit, etc.)
- The input artifact hashes used for the decision
