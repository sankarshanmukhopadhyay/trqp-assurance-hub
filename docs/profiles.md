# Profiles

## Smoke

Fast deterministic profile intended for CI sanity checks and the Assurance Hub combined-assurance smoke workflow.

## Baseline

Schema validation, structured errors, deterministic outcomes under stable state.

## Enterprise

Adds governance metadata expectations and operational discipline.

## High-Assurance

Requires declared state reference, replay resistance expectations, and signed evidence bundles.

## DeDi (experimental)

The CTS includes **experimental** structural validation for Decentralized Directory Protocol (DeDi) artifacts.

- Upstream: https://github.com/LF-Decentralized-Trust-labs/decentralized-directory-protocol
- Script: `scripts/validate_dedi_artifacts.py`
- Schemas (vendored snapshot): `schemas/dedi/` (as of 2026-03-03)

This validation is schema-focused and does not perform cryptographic verification.

### DeDi mapping spine

See `docs/reference/dedi-mapping-matrix.md` for the shared DeDi mapping matrix (artifact → Hub control objective → CTS check → expected evidence).

The DeDi mapping matrix is also available in machine-readable form: `docs/reference/dedi-mapping-matrix.yaml`.

