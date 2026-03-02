# GRID ↔ GTR Crosswalk

This repo adds **TRQP assurance metadata** to support GRID-style directory operations, while remaining compatible with the **GTR registrar schema** (`schemas/registrar-v1.json` in the GTR repository).

## Field mapping

| GTR registrar-v1.json field | TRQP Assurance Hub registrar.schema.json field | Notes |
|---|---|---|
| `country_code` | `country_code` | Same semantics |
| `registrar_name` | `registrar_name` | Same semantics |
| `register_name` | `register_name` | Same semantics |
| `register_type` | `register_type` | Same semantics |
| `legal_basis` | `legal_basis` | Same semantics |
| `authoritative_body` | `authoritative_body` | Same semantics |
| `register_id` | `register_id` | Same semantics |
| `registered_id_pattern` | `registered_id_pattern` | Same semantics |
| `query_endpoint` | `query_endpoint` | Optional |
| `resolver_endpoint` | `resolver_endpoint` | Optional |
| `did` | `did` | Same semantics |
| `grid_reference` | `grid_reference` | Optional |

## TRQP extensions (not present in GTR schema)

| TRQP extension | Purpose |
|---|---|
| `assurance_level` | Directory eligibility class (AL1–AL4) |
| `status` / `status_effective_at` / `status_reason` | Lifecycle management |
| `trqp.governance_policy` | Policy pointer + hash for audit integrity |
| `trqp.evidence[]` | Evidence references for verifier-first validation |
| `trqp.quorum` | Optional listing governance semantics |
| `trqp.last_audit_at` | Currency / recency signal |

## Compatibility guidance

- A GTR-conformant record can be made TRQP/GRID-ready by adding the TRQP extensions and tightening required fields.
- Directory operators **SHOULD** maintain backward compatibility with GTR fields to reduce ecosystem fragmentation.
