---
owner: maintainers
last_reviewed: 2026-03-19
tier: 1
---

# Assurance level decision tree

Use this guide to choose the right assurance level (AL1–AL4) for your deployment
context. Work through the questions in order and stop at the first match.

Canonical AL definitions: `docs/guides/assurance-levels.md`

---

## Step 1 — What is the consequence of a wrong trust decision?

**Low consequence** — A wrong decision affects only internal tooling, a sandbox,
or a development environment. No third-party reliance; no regulatory exposure.
→ Start at **AL1**.

**Medium consequence** — A wrong decision could affect a real relying party
(e.g., an organization validating a credential), but errors are detectable and
recoverable within hours. No regulatory or contractual mandate.
→ Start at **AL2**.

**High consequence** — A wrong decision could result in legal, financial, or
reputational harm to a third party. Errors may not be immediately detectable.
A regulator, auditor, or contractual counterpart may review evidence.
→ Start at **AL3**.

**Critical consequence** — A wrong decision could have cascading effects across
a trust ecosystem (e.g., a root-of-trust registry, a government-issued credential
registry, or critical infrastructure). Continuous operation is contractually or
legally required.
→ Start at **AL4**.

---

## Step 2 — Is external review required?

If you started at **AL1** or **AL2**, ask: will an external party (customer,
regulator, certifier, or procurement authority) rely on your assurance claim
without independent verification of their own?

**No** — external reliance is internal or informal only. Stay at your current level.

**Yes** — external reliance exists. Upgrade one level (AL1 → AL2; AL2 → AL3).

---

## Step 3 — Is continuous operation required?

If you are now at AL3, ask: does your trust claim need to remain valid under
change (code deploys, key rotations, policy updates) without a reassessment
each time?

**No** — periodic reassessment (e.g., annual) is acceptable. Stay at **AL3**.

**Yes** — continuous evidence of operational posture is required. Upgrade to **AL4**.

---

## Decision summary table

| Deployment context | External reliance? | Continuous operation? | Recommended AL |
|---|---|---|---|
| Internal tooling / sandbox | No | No | AL1 |
| Pilot / pre-production with internal stakeholders | No | No | AL1 |
| Production with informal external reliance | Informal | No | AL2 |
| Production with formal external reliance (contracts/procurement) | Yes | No | AL3 |
| Production registry in a governed trust framework | Yes | No | AL3 |
| Root-of-trust or critical infrastructure registry | Yes | Yes | AL4 |
| Regulatory or legally-mandated trust registry | Yes | Yes | AL4 |
| Ayra Trust Network cross-ecosystem participant | Yes (Ayra review) | No | AL3 minimum |

---

## AL selection quick reference

### AL1 — Baseline conformance and hygiene

**Choose AL1 when:** You need to demonstrate that your implementation behaves
correctly and can produce machine-readable evidence, but external reliance is
internal or informal.

**Minimum toolchain:** CTS baseline profile + TSPP AL1 harness + version tuple.

**Evidence you need:** CTS evidence bundle, TSPP posture report, version declarations.

**Evidence you do not need:** Independent assessor, Control Satisfaction Declaration,
Lifecycle Assertion, Certification Attestation.

→ Example bundle: `examples/al1-evidence-bundle/`

---

### AL2 — Evidence-bound self-attestation

**Choose AL2 when:** A real relying party will depend on your registry's outputs,
but you are attesting to your own conformance (no independent assessor required).

**Minimum toolchain:** CTS baseline profile + TSPP AL2 harness (signed responses) +
Combined Assurance Manifest with shared `run_id` + checksums + CI run link.

**Evidence you need:** All AL1 artifacts, plus: Combined Assurance Manifest (Required),
checksums (Recommended), CI provenance link (Recommended).

**Evidence you do not need:** Independent assessor, Control Satisfaction Declaration,
Certification Attestation.

→ Example bundle: `examples/al2-evidence-bundle/`

---

### AL3 — Independently reviewed assurance

**Choose AL3 when:** An external auditor, certifier, or procurement authority will
review your evidence. Your claim must be independently assessable.

**Minimum toolchain:** All AL2 toolchain, plus: TSPP AL3 harness (default signing,
independent assessment URI) + Control Satisfaction Declaration + Lifecycle Assertion
+ Certification Attestation (with independent assessor identity) + remediation closure
records.

**Evidence you need:** All AL2 artifacts (now all Required), plus: Control Satisfaction
Declaration, Lifecycle Assertion, Certification Attestation, Independent Assessment
Report, Remediation Closure records.

→ Example bundle: `examples/al3-evidence-bundle/`
→ Audit checklist: `examples/al3-evidence-bundle/AUDIT_GUIDE.md`

---

### AL4 — High-consequence / continuously evidenced assurance

**Choose AL4 when:** Your registry operates in a context where trust decisions have
cascading effects, continuous operation is contractually or legally required, or a
regulatory body may audit your evidence at any time.

**Minimum toolchain:** All AL3 toolchain, plus: TSPP AL4 harness (key protection,
monitoring, audit log, policy + rollback URIs) + continuous monitoring artifacts +
operationalized revocation and renewal.

**Evidence you need:** All AL3 artifacts, plus: monitoring evidence (logs + summary),
incident metrics, key rotation proof, operational attestation statement, change log,
revocation notice, renewal plan.

→ Example bundle: `examples/al4-evidence-bundle/`
→ Audit checklist: `examples/al4-evidence-bundle/AUDIT_GUIDE.md`

---

## When to reassess

Your AL claim should be reassessed when any of the following occur:

- The registry is deployed to a new environment or trust domain.
- A material change is made to the code, configuration, or key material.
- A nonconformity is detected that has not been closed.
- The Certification Attestation validity window expires (AL3/AL4).
- A trust framework you participate in updates its own assurance requirements.

_Last updated: 2026-03-19_
