# Security Policy

## Reporting a vulnerability
Do not disclose vulnerabilities in public issues. Report privately to the maintainers with the affected component, impact, safe reproduction steps, and any suggested remediation.

## Scope
This repository is in scope for reports affecting:

- manifest and example validation tooling under `tools/`
- schemas, examples, and combined-assurance guidance that could mislead auditors or implementers
- GitHub Actions workflows that generate or publish assurance artifacts
- cross-repo contracts such as `al-contract.json` and evidence-artifact guidance
- AL3/AL4 evidence bundle examples that could propagate incorrect assurance claims

## Threat model references
Security reports should be read alongside the following threat framing:

- `docs/grid-threat-annex.md` — threat categories applicable to directory-style deployments
- `docs/guides/assurance-levels.md` — canonical AL definitions and evidence expectations
- `docs/guides/combined-assurance.md` — combined workflow threat surface
- TRQP-TSPP `docs/threat-model.md` — adversarial model for the protocol layer (external repo)

## Reporting scope clarification
This repository produces **assurance guidance, schemas, and evidence templates** — not production trust decisions. A vulnerability that causes the Hub's guidance or tooling to produce misleading assurance claims is in scope. Vulnerabilities in downstream trust registries discovered during an assurance workflow should be reported to the operator of that registry. Schema drift that silently invalidates downstream AL contract pins is in scope.

## Related guidance
Security review should be read together with `docs/guides/assurance-levels.md`, `docs/guides/combined-assurance.md`, and `docs/grid-threat-annex.md`.
