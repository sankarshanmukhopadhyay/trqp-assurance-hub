---
layout: default
title: "Security Policy"
nav_exclude: true
---

# Security Policy

## Supported versions

Security and assurance-integrity fixes are applied to current `main` and the latest supported release line identified by repository status/release metadata. Older releases should be treated as unsupported unless a maintainer explicitly states otherwise.

## Reporting a vulnerability

Do not disclose undisclosed vulnerabilities in public issues. Use GitHub private vulnerability reporting when available, or contact maintainers through a private channel identified on the maintainer profile. Include the affected component/version, impact, safe reproduction steps, affected assurance evidence, and any suggested remediation.

## Scope

This repository is in scope for reports affecting:

- manifest and example validation tooling under `tools/`;
- schemas, examples, and combined-assurance guidance that could mislead auditors or implementers;
- GitHub Actions workflows that generate or publish assurance artifacts;
- cross-repo contracts such as `al-contract.json` and evidence-artifact guidance; and
- AL3/AL4 evidence bundle examples that could propagate incorrect assurance claims.

## Threat model references

Read reports alongside `docs/grid-threat-annex.md`, `docs/guides/assurance-levels.md`, `docs/guides/combined-assurance.md`, and TRQP-TSPP `docs/threat-model.md`.

## Reporting scope clarification

This repository produces **assurance guidance, schemas, and evidence templates**, not production trust decisions. A defect that produces misleading assurance claims or silently invalidates downstream AL contract pins is in scope. Remediation MUST identify potentially invalidated evidence and MUST NOT silently preserve a stale assurance result.

Vulnerabilities in downstream trust registries discovered during an assurance workflow should be reported to the operator of that registry.
