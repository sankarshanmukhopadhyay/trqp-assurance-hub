---
owner: maintainers
last_reviewed: 2026-03-04
tier: 0
---

# Quickstart

This repo is the front door for running **combined assurance** in the TRQP ecosystem.

## What you should do first

1. Pick your goal:
   - Protocol behavior assurance → use the Conformance Suite
   - Security and privacy posture assurance → use TRQP-TSPP
   - Production readiness → run both and bind evidence together

2. Read the operating docs:
   - Combined assurance workflow: `docs/guides/combined-assurance.md`
   - Evidence artifacts and expectations: `docs/guides/evidence-artifacts.md`
   - Assurance profile (candidate): `docs/guides/assurance-profile.md`
   - Compatibility policy and matrix: `docs/policies/compatibility.md`
   - Upstream TRQP RFE alignment: `docs/trqp-alignment.md`

## Repository links

- Conformance Suite: <https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite>
- TRQP-TSPP: <https://github.com/sankarshanmukhopadhyay/TRQP-TSPP>


## Operational Stack baseline

Use `tools/run_operational_stack.py` together with `docs/guides/run-the-stack.md` to combine a CTS report, a TSPP report, and a combined assurance manifest into a single portable artifact set.
