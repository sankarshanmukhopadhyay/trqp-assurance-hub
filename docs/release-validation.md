---
owner: maintainers
last_reviewed: 2026-07-03
tier: 0
---

# Release Validation

This record defines the validation gate for Hub v1.8.0 in the Operational Trust Stack Maturity Release.

## Compatibility tuple

| Repository | Version | Role |
|---|---:|---|
| TRQP Assurance Hub | v1.8.0 | Combined assurance orchestration and publication |
| TRQP Conformance Suite | v1.5.0 | Protocol conformance evidence producer |
| TRQP-TSPP | v0.13.0 | Security and privacy posture evidence producer |

## Required commands

```bash
python tools/validate_examples.py
python scripts/doc_tests.py
python scripts/check_doc_freshness.py
python tools/validate_operational_stack.py --bundle-dir artifacts/operational-stack
```

## Acceptance criteria

- All JSON examples parse and validate against paired schemas where available.
- Markdown internal links resolve.
- Documentation freshness metadata is present for governed documents.
- Operational stack artifacts share the expected `run_id`, `target_id`, version tuple, and SHA-256 integrity references.
- The release note includes adoption impact, evidence impact, and cross-repo compatibility impact.

## Local validation status

| Check | Status | Notes |
|---|---|---|
| `python scripts/doc_tests.py` | Passed | Markdown links and parse checks completed locally. |
| `python scripts/check_doc_freshness.py` | Passed | Governed document freshness metadata refreshed for the maturity release. |
| `python tools/validate_examples.py` | Blocked locally | Local environment lacked `jsonschema`; dependency installation was blocked by package-index/proxy access. Must be rerun in CI or a developer environment with `cts/requirements.txt` installed. |
| `python tools/validate_operational_stack.py --bundle-dir artifacts/operational-stack` | Blocked locally | Same `jsonschema` dependency blocker as above. |

## Release decision

Hub v1.8.0 is release-worthy because it changes the operating model of the stack. It introduces the governance and validation gates required to stop low-signal release churn while preserving the ability to ship urgent fixes.
