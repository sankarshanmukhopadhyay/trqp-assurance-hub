# GRID Profile (TRQP Assurance Hub)

This profile defines the **minimum, verifier-oriented requirements** for operating a **Global Registrar Information Directory (GRID)** using TRQP-style assurance artifacts.

It is intentionally small: it specifies *what must be true* for a registrar to be listed, verified, and lifecycle-managed.

## Scope

- Entity type: **Registrar** (operator of an authoritative register)
- Surface: **Directory listing + status feed**
- Objective: allow independent verifiers to determine whether a registrar listing is **legitimate, current, and sufficiently assured**.

## Required artifacts

A registrar listing **MUST** publish:

1. **Registrar listing record** (`registrar.json`) conforming to `schemas/registrar.schema.json`
2. **Governance policy pointer + hash** (`trqp.governance_policy`)
3. **Evidence references** appropriate to the claimed assurance level
4. **Lifecycle status** (`status`, `status_effective_at`) and reason where relevant
5. Inclusion in a **signed status feed** conforming to `schemas/grid-status-feed.schema.json`

## Lifecycle states

`proposed → under_review → approved → active → suspended|revoked → archived`

Each status transition **SHOULD** be reflected in the signed status feed within the directory operator’s stated SLA.

## Assurance binding

See: `docs/grid-assurance-mapping.md`

## Interop with GTR

This schema is designed to be compatible with the GTR `registrar-v1.json` fields and extends it with TRQP assurance metadata.

See: `docs/grid-gtr-crosswalk.md`
