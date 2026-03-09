# GRID assurance mapping

This document binds TRQP Assurance Levels (AL) to **directory eligibility** decisions for GRID-style directories.

## Mapping

- **AL1** — Informational listing only (not eligible for operational reliance)
- **AL2** — Listing eligible for low-risk reliance (requires explicit verifier policy)
- **AL3** — Eligible for operational reliance (default for active registrars)
- **AL4** — Eligible for critical infrastructure reliance (highest scrutiny)

## Policy note

Directory operators SHOULD publish their eligibility policy (including exceptional cases) and MUST publish the evidence expectations for AL3/AL4 listings.

## UNTP DIA considerations

If GRID implementations use UNTP Digital Identity Anchor (DIA) and Identity Resolver (IDR) patterns, assessments MUST treat GRID as a composite trust system (directory governance + publication integrity + identity anchoring). SAD-1 supports this via the `identity_anchor` extension and vendored DIA JSON-LD context.
