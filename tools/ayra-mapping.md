# Assurance Hub Controls ↔ Ayra Trust Network Crosswalk

This document maps the five Assurance Hub canonical controls to the conformance
requirements of the [Ayra Trust Network TRQP Profile](https://ayraforum.github.io/ayra-trust-registry-resources/api.html),
with notes on evidence sufficiency per assurance level (AL) tier.

## Control mapping

### TRQP-CTRL-01 — Policy publication

**Hub definition:** The operator MUST publish a machine-readable governance framework
declaration reachable at `/.well-known/trqp-metadata`.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Registry self-declaration endpoint | TSPP metadata schema validation (`test_01_metadata.py`) | AL1 |
| Governance framework URI present in provenance | `tspp_conformance_report.json` — metadata provenance fields | AL1 |
| Ayra network registration | Ayra member directory entry (out of scope for this toolset) | AL1 |

**Sufficiency notes:** TSPP `test_01_metadata.py` passing at AL1 is necessary but not
sufficient for Ayra registration. The `governance_framework_id` in the metadata must
reference an Ayra-registered governance framework URI.

---

### TRQP-CTRL-02 — Evidence bundle integrity

**Hub definition:** Conformance and posture evidence MUST be packaged in a signed,
hash-pinned evidence bundle to prevent tampering.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Conformance evidence bundle | CTS `manifest.json` + `checksums.json` | AL1 |
| TSPP posture evidence | `tspp_conformance_report.json` + `manifest.sig` | AL2 |
| Combined assurance manifest | Hub `combined-assurance-manifest.json` (via `generate-manifest.py`) | AL2 |

**Sufficiency notes:** For Ayra Basic tier, unsigned CTS Baseline bundle is accepted.
For Cross-Ecosystem and Sovereign tiers, TSPP AL2 signed report with `manifest.sig`
is required. Generate the combined manifest before submission.

---

### TRQP-CTRL-03 — Directory lifecycle

**Hub definition:** The registry MUST implement and expose a machine-readable lifecycle
state (active, suspended, revoked) and keep it current.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| GRID status feed schema conformance | CTS GRID status feed verdicts (if GRID profile) | AL1 |
| Registrar listing accuracy | CTS `registrar.schema.json` validation output | AL1 |
| Lifecycle state transitions auditable | Audit log URI in TSPP metadata `audit` block | AL2 |

**Sufficiency notes:** Ayra requires registries to participate in the GRID status feed
protocol. Run the CTS with `profiles/grid-profile.yaml` and include the verdicts.

---

### TRQP-CTRL-04 — Operator identity assurance

**Hub definition:** The operator MUST bind its identity to the registry via a verifiable
credential or signed attestation at the declared assurance level.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| JWKS endpoint reachable and pinned | TSPP `test_06_al2_signed_responses.py` — JWKS preflight | AL2 |
| Signed response envelopes | TSPP AL2 harness run — `test_06_al2_signed_responses.py` | AL2 |
| Key protection posture declared | TSPP metadata `key_protection` block | AL2 |
| DPoP for bulk clients | TSPP `test_05_ratelimits.py` — sender-constrained token checks | AL3 |

**Sufficiency notes:** For Ayra Sovereign tier, HSM-backed keys (`key_protection.protection: "HSM"`)
with an `evidence_uri` pointing to an independent key attestation are expected.

---

### TRQP-CTRL-07 — Incident response

**Hub definition:** The operator MUST maintain a documented and tested incident response
runbook and provide a security contact reachable within the declared SLA.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Security contact declared | TSPP metadata `operator.security_contact` | AL1 |
| Incident runbook URI declared | TSPP metadata `monitoring.runbook_uri` | AL2 |
| Evidence retention declared | TSPP metadata `monitoring.evidence_retention_days` | AL2 |
| Independent assessment reference | TSPP metadata `audit.independent_assessment_uri` | AL3 |

**Sufficiency notes:** Ayra does not mandate a specific incident response SLA, but
`monitoring.evidence_retention_days` SHOULD be ≥ 90 for Basic tier and ≥ 365 for
Sovereign tier per the Ayra member agreement template.

---

## End-to-end evidence checklist for Ayra submission

### Basic member registry (AL1 + CTS Baseline)

- [ ] CTS Baseline profile run: all MUST-level tests PASS
- [ ] TSPP AL1 run: `test_01_metadata.py`, `test_02_freshness.py`, `test_03_context_allowlist.py`,
      `test_04_anti_enumeration.py`, `test_05_ratelimits.py` all PASS
- [ ] `combined-assurance-manifest.json` produced by `generate-manifest.py`
- [ ] `operator.security_contact.email` present in TSPP metadata
- [ ] `governance_framework_id` references an Ayra-registered URI

### Cross-ecosystem recognition registry (AL2 + CTS Enterprise)

- [ ] All Basic requirements above
- [ ] CTS Enterprise profile run (includes TRQP-FRESH-001/002): all PASS
- [ ] TSPP AL2 run: `test_06_al2_signed_responses.py` PASS
- [ ] Signed `manifest.sig` included in evidence package
- [ ] `key_protection` block declared in metadata
- [ ] `monitoring.runbook_uri` and `evidence_retention_days` declared

### Sovereign / regulated ecosystem (AL3 + CTS High-Assurance)

- [ ] All Cross-Ecosystem requirements above
- [ ] CTS High-Assurance profile run: all gates PASS
- [ ] TSPP AL3 run: `test_08_al3_controls.py` PASS
- [ ] `audit.independent_assessment_uri` present and reachable
- [ ] `key_protection.protection: "HSM"` with `evidence_uri`
