# Compatibility Policy

This document defines how the TRQP Conformance Suite and TRQP-TSPP stay interoperable **without** being forced into a monorepo.

## Goals

- Minimize adopter confusion (“which repo do I start with?”)
- Preserve independent release cadence
- Establish a **clear compatibility signal** for combined assurance runs

## Compatibility statement

A combined assurance run is considered **supported** when:

- The implementer uses a listed **known-good pair** of versions (see matrix below), **or**
- The implementer demonstrates successful execution of both tools against the same target and produces evidence bundles conforming to the expected schemas.

## Versioning expectations

- Each repo MUST publish releases using SemVer.
- Each repo SHOULD publish a short compatibility note in its release notes that references the other repo.

## Known-good matrix

Maintain this table over time.

| Conformance Suite version | TRQP-TSPP version | Status | Notes |
|---:|---:|---|---|
| 0.4.3 | 0.2.3 | Supported | Deterministic bundles + verifier-first workflow; recommended pairing |
| 0.4.2 | 0.2.2 | Supported | Documentation alignment increment |
| 0.4.1 | 0.2.1 | Supported | Baseline pairing prior to determinism hardening |

## Shared contracts

The following are treated as cross-repo contracts. Breaking changes must be clearly flagged in release notes.

1. **Requirement ID conventions**
2. **Evidence bundle naming & structure**
3. **Result semantics** (pass/fail/skip + rationale)
4. **Machine-readable metadata** about run context (tool version, profile, timestamp)

## Breaking change discipline

A change is breaking if it causes:

- Evidence bundles to be non-comparable across tools
- A profile pack to stop running on the runner (or vice versa)
- Requirement IDs to become unstable (renamed/repurposed)

Breaking changes MUST:

- Increment MAJOR version
- Include a migration note
- Update the known-good matrix
