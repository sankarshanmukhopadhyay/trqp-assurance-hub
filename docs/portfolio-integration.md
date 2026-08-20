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

TRQP-TSPP supplies protocol-side evidence. The TRQP Conformance Suite supplies execution and conformance evidence. The Assurance Hub combines those inputs without redefining their upstream semantics.

## Automated validation

`tools/validate_portfolio_contract.py` checks the release version, upstream version pins, required local evidence, repository relationships, and invalidation conditions. `.github/workflows/portfolio-contract.yml` runs these checks for pull requests and pushes to `main` and uploads a JSON validation result.

Missing required evidence, incompatible upstream versions, or invalid source assurance evidence makes the integration contract invalid.
