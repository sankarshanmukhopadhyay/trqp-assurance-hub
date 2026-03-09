# Security Policy

## Reporting a vulnerability
Do not open public issues for vulnerabilities. Report privately to maintainers with the affected component, impact, safe reproduction steps, and any suggested remediation.

## Scope
The following areas are in scope for security reports:

- CTS runner logic under `cts/`, especially bugs that can produce false PASS, FAIL, or ERROR verdicts
- example SUT code under `examples/`, including replay protection, signing, and example credential handling
- schemas, evidence bundle outputs, and documentation that could mislead implementers or auditors
- CI workflows and artifact production steps
- identifier parameterization logic in `cts/run.py` that maps SUT-supplied values into test bodies

## Threat model references
Security reports should be interpreted alongside the following threat framing:

- TRQP Assurance Hub: `docs/grid-threat-annex.md` — threat categories applicable to directory-style deployments
- TRQP-TSPP: `docs/threat-model.md` — adversarial model of harms relevant to protocol conformance
- `docs/reference/TRACE-TSAM.md` — mapping from control objectives to testable assertions

## Reporting scope clarification
This repository produces **conformance evidence artifacts** — not production trust decisions. A vulnerability in CTS that causes false PASSes is in scope because it undermines the integrity of the evidence relied on by auditors and operators. Vulnerabilities in downstream trust registries that happen to be discovered during CTS runs should be reported to the operator of that registry, not this repository.

## Related guidance
Read reports alongside `docs/VERIFY_EVIDENCE.md` and the TRQP Assurance Hub combined-assurance documentation.
