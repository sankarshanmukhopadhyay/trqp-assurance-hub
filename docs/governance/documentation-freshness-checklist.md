---
owner: maintainers
last_reviewed: 2026-03-04
tier: 2
---

# Documentation freshness and relevance checklist

This repo adopts the shared checklist below as the baseline for documentation quality gates.

# Repository Documentation Freshness & Relevance Checklist

## Purpose

This checklist helps engineering teams validate that repository
documentation remains accurate, current, and operationally useful. It is
designed for repeatable audits and CI integration.

------------------------------------------------------------------------

# 1. Documentation Inventory & Ownership

-   Documentation index exists listing README, /docs, architecture docs,
    ADRs, runbooks, API docs, diagrams.
-   Each document has an explicit owner (person/team).
-   Documentation tiers defined:
    -   Tier 0: onboarding / quickstart
    -   Tier 1: API and behavioral documentation
    -   Tier 2: operational runbooks
    -   Tier 3: architectural rationale (ADRs)
-   Review cadence defined for each tier.

------------------------------------------------------------------------

# 2. Freshness Metadata

-   Last reviewed date present.
-   Documentation states applicable version or branch.
-   Deprecated docs clearly marked and linked to replacements.
-   Release notes reference documentation-impacting changes.

------------------------------------------------------------------------

# 3. Reality Alignment Checks

-   Installation steps work on a clean machine/container.
-   Commands execute successfully.
-   Configuration examples match current schema.
-   CLI flags match CLI help output.
-   API documentation matches actual interfaces.
-   Examples compile or run successfully.
-   Architecture diagrams reflect current system structure.

------------------------------------------------------------------------

# 4. Audience Completeness

-   Clear onboarding path exists.
-   Conceptual system overview exists.
-   Happy path documented end-to-end.
-   Known constraints and limits documented.
-   Decision guidance exists ("Use X when...").

------------------------------------------------------------------------

# 5. Documentation-Code Coupling

-   Documentation examples tested in CI.
-   API documentation generated from canonical specification where
    possible.
-   Configuration schemas validated automatically.
-   Single source of truth for API schemas and CLI definitions.

------------------------------------------------------------------------

# 6. Link Integrity

-   Internal links validated.
-   External links validated.
-   References pinned to versioned sources where appropriate.
-   No unresolved TODO markers.

------------------------------------------------------------------------

# 7. Security & Compliance Relevance

-   Threat model documented.
-   Security guidance included for authentication, authorization, and
    secrets.
-   SECURITY.md present with vulnerability reporting guidance.
-   Licensing documented.
-   Data handling requirements described where relevant.

------------------------------------------------------------------------

# 8. Operations Readiness

-   Deployment documentation reflects current infrastructure.
-   Observability documented: logs, metrics, tracing.
-   Incident runbooks exist.
-   Backup and restore procedures documented.
-   Upgrade and rollback procedures documented.

------------------------------------------------------------------------

# 9. Discoverability & Structure

-   README answers:
    -   What this project is
    -   Who it is for
    -   How to run it quickly
    -   Where documentation lives
-   Documentation has structured navigation.
-   Terminology glossary exists if domain complexity requires it.

------------------------------------------------------------------------

# 10. Clarity & Consistency

-   Instructions unambiguous.
-   Naming consistent across code and documentation.
-   Examples copy-pasteable.
-   Expected outputs shown for commands.

------------------------------------------------------------------------

# 11. Drift Indicators

-   Old product or repository names removed.
-   Version numbers current.
-   Badges reflect current CI pipelines.
-   No references to deleted files or branches.

------------------------------------------------------------------------

# 12. Issue Severity Model

P0: Broken onboarding, incorrect API, incorrect security guidance\
P1: Missing sections, broken links, incomplete examples\
P2: Style, formatting, clarity improvements

Release gating recommendation: No P0 documentation defects allowed at
release time.

------------------------------------------------------------------------

# Repeatable Pipeline Strategy

## 1. Link Checking

Run automated validation for both internal and external links.

Recommended tools: - markdown-link-check - lychee

Example CI step:

    lychee ./docs ./README.md --exclude-mail

## 2. Documentation Tests

Execute examples embedded in documentation.

Approaches: - Run code blocks using doctest frameworks - Validate
JSON/YAML examples against schemas - Validate OpenAPI specs
automatically

Example schema validation:

    ajv validate -s schema.json -d examples/*.json

## 3. Freshness SLA Enforcement

Define policy thresholds:

  Tier     Max Age
  -------- ----------
  Tier 0   30 days
  Tier 1   60 days
  Tier 2   90 days
  Tier 3   180 days

CI step example:

-   Parse markdown frontmatter or metadata
-   Fail pipeline if `last_reviewed` exceeds SLA

Pseudo check:

    if doc_age > SLA:
        fail_pipeline

## 4. Example Execution in CI

Run quickstart instructions in containerized environment.

Example pattern:

    docker build .
    docker run project-test ./examples/run_example.sh

## 5. Schema & API Validation

Validate machine-readable interfaces automatically:

-   OpenAPI validation
-   JSON schema validation
-   CLI help output comparison

Example:

    openapi-cli validate openapi.yaml

## 6. Documentation Drift Detection

CI check compares: - CLI help output vs documented flags - Config schema
vs documented config examples

Fail build if mismatch detected.

------------------------------------------------------------------------

# Recommended CI Pipeline Order

1.  Markdown linting
2.  Link checking
3.  Schema validation
4.  Example execution
5.  API specification validation
6.  Documentation freshness SLA enforcement

------------------------------------------------------------------------

# Outcome

When implemented properly this pipeline ensures:

-   Documentation reflects reality
-   Examples remain executable
-   Links stay valid
-   Operational knowledge stays current
