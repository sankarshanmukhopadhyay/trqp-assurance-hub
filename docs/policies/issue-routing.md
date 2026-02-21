# Issue Routing Policy

The point of this policy is to avoid “triage ping-pong” and keep contributor effort compounding.

## Route issues to the right repo

### File in `trqp-conformance-suite`

Use when the issue is about:

- Runner behavior / CLI / packaging
- Evidence bundle formatting produced by the runner
- Profiles that live inside the conformance suite repo
- CI failures, test discovery, report generation

Repo: <https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite>

### File in `TRQP-TSPP`

Use when the issue is about:

- AL1/AL2 security & privacy requirements
- Posture checks, hardening recommendations
- TSPP schemas, OpenAPI contract, or its pytest harness

Repo: <https://github.com/sankarshanmukhopadhyay/TRQP-TSPP>

### File in this repo (`trqp-assurance-hub`)

Use when the issue is about:

- Cross-repo onboarding/documentation
- Compatibility matrix updates
- Combined workflow guidance
- Terminology / user journey / adoption packaging
