# Roadmap

This roadmap is intentionally lightweight and focused on adoption and socialization.

## 2026 Q1: Socialization and trust signaling

- Done: onboarding docs (`START_HERE`, `SOCIALIZING_NOTES`, `FAQ`)
- Done: reference evidence bundles (`docs/reference-reports/`)
- Done: evidence bundle descriptor + checksums schemas (`schemas/evidence/`)
- Done: CI publishes evidence bundles as build artifacts (descriptor + checksums + bundle.zip)
- Done: Smoke profile for Hub combined-assurance workflow (`profiles/smoke.yaml`)
- Done: Hub crosswalk mapping (`docs/hub-crosswalk.md`)
- Done: `--dry-run` and `--list-tests` CLI flags for developer tooling
- Done: `identifiers:` SUT config block for real-SUT parameterization
- Done: JSONPath wildcard token indexing fix
- Done: `QUICKSTART.md` for fast onboarding

## 2026 Q2: Deterministic replay and state models

- Planned: deterministic replay mode (`--replay <run-dir>`)
- Planned: state snapshot verification models (fixture ID, snapshot hash, signed snapshot)

## 2026 Q3: Security profiles and plugfests

- Planned: mTLS security profile
- Planned: interoperability plugfest mode and matrix generation

## 2026 Q4: Performance and operational readiness

- Planned: performance conformance harness and SLA-oriented checks


## Completed

- ✅ AL semantic lock to Assurance Hub (`al-contract.json` + explicit README/docs pointers)
- ✅ Runner refactored into named functions for testability


## Release readiness (v0.7.1)

- `--dry-run` and `--list-tests` flags enable safer CI integration and developer inspection.
- Identifier parameterization via `sut.yaml` allows real SUTs to run the suite without modifying core tests.
- JSONPath wildcard bug fixed for correct assertion evaluation on array paths.
- QUICKSTART and expanded SECURITY documentation complete.

_Last updated: 2026-03-06_

## UNTP DIA considerations

Where a directory uses UNTP Digital Identity Anchor (DIA) / Identity Resolver (IDR), conformance evidence SHOULD include DIA context references and resolver documentation. The CTS validator includes lightweight checks for DIA context wiring when `identity_anchor.anchor_type` indicates UNTP DIA.
