---
layout: default
title: "Public Assurance Publication"
nav_exclude: true
---

# Public Assurance Publication

A Combined Assurance Manifest is an audit artifact. A Public Assurance Summary is an adoption artifact. The summary gives ecosystem operators, relying parties, assessors, and affected users a compact description of what was checked, when it was checked, and what remains out of scope.

## Governance objective

The publication flow makes assurance evidence discoverable without asking every reader to understand the full evidence bundle. The underlying manifest remains the source of truth. The summary is a bounded presentation layer.

## Publication workflow

1. Run CTS against the target registry.
2. Run TSPP posture checks against the same target.
3. Generate the Combined Assurance Manifest in the Hub.
4. Generate `public-assurance-summary.json` from the manifest.
5. Publish the summary with a link to the full evidence manifest where policy allows.
6. Refresh the summary before `valid_until`.

## Required properties

The summary MUST identify the target, assurance level, status, freshness window, evidence manifest, limitations, and consumer relevance statement.

## Non-goals

The summary does not certify legal authority, financial solvency, business continuity, or every ecosystem-specific governance rule. Those may be layered through higher assurance profiles or ecosystem policy.
