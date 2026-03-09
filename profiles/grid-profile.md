# GRID Profile (Global Registrar Information Directory)

This profile defines the minimum publishable artifacts for a **GRID-listed registrar**.

This is an *instance profile* that implements **SAD-1 (Sovereign Authoritative Directory)**: `profiles/sad-1-profile.md`.

GRID is treated here as an *implementation pattern* for trust registries/directory ecosystems that can be queried via TRQP.

## Scope

- Entity class: **Registrar**
- Output surface: **Directory listing + status feed**
- Assurance: bound to TRQP Assurance Levels (AL1–AL4)
- Verification model: **verifier-first** (hash + signature + policy binding)

## Required artifacts

1. **Registrar listing** (machine-readable)
   - Conforms to: `schemas/registrar.schema.json`
   - Example: `examples/registrar.example.json`

2. **Status feed** (machine-readable)
   - Conforms to: `schemas/grid-status-feed.schema.json`
   - Example: `examples/grid-status-feed.example.json`

3. **Assurance mapping**
   - See: `docs/grid-assurance-mapping.md`

4. **Threat annex**
   - See: `docs/grid-threat-annex.md`

5. **Verification workflow**
   - See: `docs/how-to-verify-grid.md`

## External references

GRID is used here to demonstrate how TRQP can be extended to support **different trust registry implementations**, including:

- UN/CEFACT Global Trust Registry (GTR) / GRID workstream: https://un.opensource.unicc.org/unece/uncefact/gtr/
- EBSI Trusted Issuers Registry / Trusted Entity Registry APIs: https://hub.ebsi.eu/apis/pilot/trusted-issuers-registry

See also: `docs/grid-gtr-crosswalk.md`.
