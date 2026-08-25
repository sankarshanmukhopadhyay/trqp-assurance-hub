---
layout: default
title: "Canonical TRQP stack adopter case"
nav_exclude: true
---

# Canonical TRQP stack adopter case

This fixture is the adopter-facing reference target for coordinated TRQP Stack release eligibility. It proves that a new adopter can start from the Assurance Hub, resolve one declared component tuple, run the three repositories, and inspect evidence without independently choosing compatible versions.

## Decisive test

A stack candidate is eligible only when the declared immutable component tuple proves release resolution, clean bootstrap, TSPP/CTS execution, deterministic CTS replay, fail-closed Hub composition, provenance/integrity preservation, whole-stack semantic replay equivalence, and an executable walkthrough.

The target descriptor in `target.json` is deliberately small: it defines the shared identity and expected cross-stack properties while authoritative producer fixtures and evidence semantics remain in TSPP and CTS.

## Run

From the Assurance Hub repository root:

```bash
make stack-release-check
```

For an explicit clean-room release-engineering run:

```bash
python tools/stack_validate.py --check-remote
python tools/stack_bootstrap.py --clean
python tools/stack_evaluate.py
```

These commands generate candidate validation evidence. A coordinated release exists only after the candidate passes the decisive workflow and a maintainer deliberately promotes the validated release record.

TRQP Stack 2026.1 — Coconut is the first release produced through this process.
