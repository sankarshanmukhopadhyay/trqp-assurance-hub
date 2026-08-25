---
layout: default
title: "Governance"
nav_exclude: true
---

# Governance

## Repository mandate

`trqp-assurance-hub` is a Tier 1 flagship repository in the TRQP assurance stack. Its mandate is **assurance orchestration, publication, and coordinated stack-release declaration**. The repository is maintained as executable governance: material claims should map to artifacts, validation, evidence, and a reviewable change record.

## Authority

This repository is authoritative for:

- assurance evidence ingestion and composition;
- assurance profile evaluation;
- portable assurance publication;
- coordinated TRQP Stack compatibility tuple declaration;
- stack integration verification and release-eligibility evidence; and
- the canonical adopter workflow for coordinated releases.

This repository is not authoritative for:

- the TRQP protocol specification;
- raw conformance test execution or CTS replay-comparison semantics;
- TSPP control definition or posture semantics;
- TSMM semantic authority;
- TIS schema authority; or
- external certification/accreditation.

Normative authority originating in an upstream specification remains with that specification and its governing body. Local profiles, mappings, examples, release tuples, and implementation choices must not be represented as amendments to upstream standards.

## Coordinated stack releases

A coordinated TRQP Stack release is an interoperability and assurance declaration over an exact immutable component tuple. It does not replace component semantic versioning and does not transfer authority between repositories.

A candidate may be promoted to a coordinated release only when the release-readiness gate demonstrates immutable tuple resolution, clean-room bootstrap, component execution, deterministic CTS replay, valid combined assurance, run/target correlation, provenance and integrity, fail-closed negative cases, and an executable adopter walkthrough.

Changing a candidate to `validated`, creating a coordinated release tag, or publishing release notes is a deliberate maintainer action and is not performed automatically by readiness CI.

## Decision rights

Maintainers may accept changes that remain within the mandate above and pass the repository validation gate. Changes affecting cross-repository contracts require compatibility evidence and review against the TRQP adoption path. Security-sensitive changes require explicit threat, migration, and revocation analysis.

## Delegation and scope

Contributors may propose changes through pull requests. Review authority is delegated only for the scope of the reviewed change; it does not transfer repository ownership or upstream standards authority. Automated workflows enforce minimum validation but do not substitute for maintainer review.

## Enforcement and revocation

Non-conforming artifacts may be rejected, reverted, deprecated, revoked, or superseded. A coordinated stack tuple must be revoked or superseded when a component release, authority version, evidence chain, or security condition invalidates the release claim. Compromised evidence, signing material, profiles, or implementation outputs must be withdrawn or marked invalid through the relevant lifecycle mechanism. Security reports follow [`SECURITY.md`](SECURITY.md).

## Evidence and auditability

Every substantive change should identify:

1. the authority or requirement affected;
2. the executable validation performed;
3. the evidence produced;
4. compatibility or migration impact; and
5. known limitations or unresolved risks.

Repository state is declared in [`data/repository-metadata.yaml`](data/repository-metadata.yaml).
