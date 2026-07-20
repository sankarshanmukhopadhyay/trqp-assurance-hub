---
layout: default
title: "Schema contract"
nav_exclude: true
---

# Schema contract

This document declares the stability guarantees and migration policy for all
JSON Schema definitions in `schemas/`. Read this before upgrading AL contract
pins in downstream repositories.

## Stability tiers

| Tier | Meaning | Examples |
|---|---|---|
| **Stable** | Field names, types, and enum values are frozen across minor versions. Changes require a major version bump and explicit migration notes. | `manifest_version`, `build.build_id`, `build.run_id`, `tools.trqp_conformance_suite.version` |
| **Extensible** | New fields MAY be added in minor versions. Existing fields are stable. Consumers MUST tolerate unknown fields (do not use `additionalProperties: false` on your side). | `summary.*`, `artifacts[*].notes`, `generator.*` |
| **Experimental** | Field may change shape, be renamed, or be removed in any minor version. Will be graduated or removed at the next major version. Declared by a `"x-stability": "experimental"` annotation in the schema. | Currently none. |

## Schema-by-schema contract

### `combined-assurance-manifest.schema.json`

| Field | Tier | Notes |
|---|---|---|
| `manifest_version` | Stable | Currently `"0.2.0"`. Version bump signals breaking change. |
| `build.build_id`, `build.target`, `build.run_id`, `build.target_id` | Stable | Required fields; never removed. |
| `build.commit`, `build.ci_run_url` | Extensible | Optional; may be enriched. |
| `tools.trqp_conformance_suite.*`, `tools.trqp_tspp.*` | Stable | Required sub-fields frozen. |
| `artifacts[*].kind`, `artifacts[*].path` | Stable | Required per-artifact fields. |
| `artifacts[*].sha256`, `artifacts[*].media_type`, `artifacts[*].produced_by` | Extensible | Optional; new optional fields may be added. |
| `summary.*` | Extensible | All summary fields are optional. New fields (e.g. new metrics) may appear in minor versions. |
| `generator.*` | Extensible | Informational; never required for compliance. |

### `certification-attestation.schema.json`

| Field | Tier | Notes |
|---|---|---|
| `type`, `id`, `certified_entity`, `assurance_level`, `assessor`, `in_scope_controls`, `validity`, `evidence_refs`, `issued_at` | Stable | All required fields. |
| `scope`, `revocation_uri`, `signature` | Extensible | Optional; may be enriched. |

### `control-satisfaction.schema.json`

| Field | Tier | Notes |
|---|---|---|
| `type`, `id`, `subject`, `controls`, `issued_at` | Stable | All required fields. |
| `catalog_ref`, `expires_at`, `signature` | Extensible | Optional. |
| `controls[*].control_id`, `controls[*].status` | Stable | Required per-control fields. |
| `controls[*].evidence`, `controls[*].notes` | Extensible | Optional; evidence array may gain new `kind` values. |

### `lifecycle-assertion.schema.json`

| Field | Tier | Notes |
|---|---|---|
| `type`, `id`, `subject`, `state`, `issued_at` | Stable | All required fields. |
| `state` enum (`draft`, `active`, `suspended`, `deprecated`, `revoked`, `retired`) | Stable | Enum values are frozen. New states require a minor version bump with migration notes. |
| `scope`, `effective_from`, `effective_to`, `reason`, `evidence`, `signature` | Extensible | Optional. |

### `recognition-assertion.schema.json`, `registrar.schema.json`, `trqp-assurance-profile.schema.json`

All required fields are **Stable**. Optional fields are **Extensible**.

### `directory-publication-manifest.schema.json`, `directory-status-feed.schema.json`, `grid-status-feed.schema.json`

All required fields are **Stable**. Optional fields are **Extensible**.

---

## Migration policy

### Minor version bump (e.g. v1.3.0 → v1.4.0)

- New **optional** fields may be added to any schema.
- Enum values for **Extensible** fields may be extended.
- No field removals. No type changes on **Stable** fields.
- Downstream pins: no change required. Existing evidence bundles remain valid.

### Major version bump (e.g. v1.x → v2.0)

- Any **Stable** field may be renamed, retyped, or removed with explicit migration notes published in `CHANGELOG.md` and a new `releases/` entry.
- A migration guide will be published in `docs/guides/` before the major release.
- AL contract pins in downstream repos (`al-contract.json`) MUST be updated to the new release tag.
- The `manifest_version` field in `combined-assurance-manifest.schema.json` will be bumped.

### AL contract pin upgrade path

When upgrading AL contract pins in downstream repositories:

1. Check this document for any **Stable → changed** fields in the release notes.
2. Run `scripts/verify_al_contract.py` in each downstream repo after updating `al-contract.json`.
3. Re-run `tools/validate_examples.py` to confirm no example drift.
4. Update `docs/reference/compatibility-matrix.md` if the new versions are now the supported baseline.

---

## Canonical schema source

All schemas in `schemas/` are the authoritative definitions.
Alias `$ref` wrappers exist in `schemas/` root for backwards compatibility — always
read the canonical schema at the declared `$id` URI.

_Last updated: 2026-03-19_
