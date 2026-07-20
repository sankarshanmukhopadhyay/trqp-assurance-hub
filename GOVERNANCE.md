---
layout: default
title: "Governance"
nav_exclude: true
---

# Governance

## Repository mandate

`trqp-assurance-hub` is a Tier 1 flagship repository in the TRQP assurance stack. Its mandate is **assurance orchestration and publication**. The repository is maintained as executable governance: material claims should map to artifacts, validation, evidence, and a reviewable change record.

## Authority

This repository is authoritative for:

- assurance evidence ingestion and composition
- assurance profile evaluation
- portable assurance publication

This repository is not authoritative for:

- the TRQP protocol specification
- raw conformance test execution
- TSPP control definition

Normative authority originating in an upstream specification remains with that specification and its governing body. Local profiles, mappings, examples, and implementation choices must not be represented as amendments to upstream standards.

## Decision rights

Maintainers may accept changes that remain within the mandate above and pass the repository validation gate. Changes affecting cross-repository contracts require compatibility evidence and review against the TRQP adoption path. Security-sensitive changes require explicit threat, migration, and revocation analysis.

## Delegation and scope

Contributors may propose changes through pull requests. Review authority is delegated only for the scope of the reviewed change; it does not transfer repository ownership or upstream standards authority. Automated workflows enforce minimum validation but do not substitute for maintainer review.

## Enforcement and revocation

Non-conforming artifacts may be rejected, reverted, deprecated, or superseded. Compromised evidence, signing material, profiles, or implementation outputs must be withdrawn or marked invalid through the relevant lifecycle mechanism. Security reports follow [`SECURITY.md`](SECURITY.md).

## Evidence and auditability

Every substantive change should identify:

1. the authority or requirement affected;
2. the executable validation performed;
3. the evidence produced;
4. compatibility or migration impact; and
5. known limitations or unresolved risks.

Repository state is declared in [`data/repository-metadata.yaml`](data/repository-metadata.yaml).
