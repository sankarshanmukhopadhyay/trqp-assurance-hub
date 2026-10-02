---
layout: default
title: "Portfolio Integration"
nav_exclude: true
permalink: /docs/portfolio-integration/
---

# Portfolio Integration

The TRQP Assurance Hub participates in the coordinated TRQP repository set through `portfolio/integration-contract.json`.

## Repository responsibilities

The Assurance Hub aggregates evidence and produces combined assurance decisions. Shared semantic definitions are referenced from `trust-systems-meta-model` v0.24.0, while shared portfolio and repository schemas are referenced from `trust-infrastructure-schemas` v0.14.1.

TRQP-TSPP supplies security/privacy posture evidence. The TRQP Conformance Suite supplies execution, conformance and replay evidence. For state-bound composition, both producers additionally supply independently derived `target_state.digest` evidence. The Assurance Hub compares those producer-owned state identities and combines the inputs without redefining their upstream semantics.

## Automated validation

`tools/validate_portfolio_contract.py` checks the release version, upstream version pins, required local evidence, repository relationships, and invalidation conditions. `.github/workflows/portfolio-contract.yml` runs these checks for pull requests and pushes to `main` and uploads a JSON validation result.

Missing required evidence, incompatible upstream versions, or invalid source assurance evidence makes the integration contract invalid.


## Development component compatibility

The current state-bound development tuple is recorded separately in `data/component-compatibility.yaml`:

- CTS v1.11.1;
- TSPP v0.18.1;
- Hub v1.14.0 development line.

This record is deliberately separate from `data/compatibility-registry.yaml`, which retains coordinated/historical compatibility records. A supported development tuple is not a coordinated Stack release. Stack 2026.3 — Banyan remains the current published Stack baseline until a future complete tuple independently satisfies the coordinated release policy.
