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

## Compatibility matrix (known-good)

This matrix records combinations of tool versions that have been validated together.

### Legend

- **Test level:** Smoke = checkout + installability checks + minimal invocation; Partial = key profiles; Full = suite + TSPP AL checks + evidence bundle
- **Evidence:** link to CI run / artifact bundle / release tag notes

| Date (UTC) | Hub | Conformance Suite | TSPP | Test level | Environment | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| 2026-02-21 | main | main | main | Smoke | ubuntu-latest, py3.11 | [combined-assurance-smoke workflow](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/actions/workflows/combined-assurance-smoke.yml) | Initial alignment gate |

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

## Machine-readable index

For automation, this repo also publishes a machine-readable compatibility index:

- `docs/policies/compatibility.json`


## Assurance Level dimension

Known-good sets may be **assurance-level specific**. Higher assurance levels (AL3/AL4) introduce additional
evidence expectations (e.g., binding meta, transparency URIs, key custody evidence), so implementers should
treat the matrix as a (Conformance Suite, TSPP, Hub, AL) compatibility signal.
