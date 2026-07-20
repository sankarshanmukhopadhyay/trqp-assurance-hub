---
layout: default
title: "TRQP Assurance Hub v1.6.1 Release Notes"
nav_exclude: true
---

# TRQP Assurance Hub v1.6.1 Release Notes

## Summary

This patch makes combined assurance lifecycle-aware. The Combined Assurance Manifest and public assurance summary can now carry lifecycle state, status feed URI, revocation support, publication SLA, and last-checked timestamp.

## Added

- Optional `lifecycle` block in `schemas/combined-assurance-manifest.schema.json`.
- Lifecycle and revocation flags in `tools/generate-manifest.py`.
- Lifecycle output in `tools/generate-public-summary.py` and `schemas/public-assurance-summary.schema.json`.
- Updated combined assurance guidance and examples.

## Validation

- Generated a lifecycle-aware Combined Assurance Manifest.
- Generated a public assurance summary from the lifecycle-aware manifest.
- Direct JSON parse checks for updated schemas and examples.

## Coordinated Release Tuple

- TRQP-TSPP: v0.11.1
- TRQP Conformance Suite: v1.3.1
- TRQP Assurance Hub: v1.6.1
