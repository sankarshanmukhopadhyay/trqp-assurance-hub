# Assurance Hub Controls ↔ Ayra Trust Network Crosswalk

This document maps the five Assurance Hub canonical controls to the conformance
requirements of the [Ayra Trust Network TRQP Profile](https://ayraforum.github.io/ayra-trust-registry-resources/),
with notes on evidence sufficiency per assurance level (AL) tier.

Reference: [Ayra TRQP Profile API](https://ayraforum.github.io/ayra-trust-registry-resources/api.html) |
[Ayra Implementers Guide](https://ayraforum.github.io/ayra-trust-registry-resources/guides/)

Profile version aligned: **Ayra TRQP Profile v0.5.0-draft**

---

## Ayra identifier requirements (normative — applies across all controls)

The Ayra Profile mandates `did:webvh` as the identifier method for all ecosystem,
trust registry, and cluster identifiers. This is a MUST at every Ayra tier and applies
to `entity_id`, `authority_id`, and all service endpoint DIDs.

| Identifier role | Ayra requirement | Minimum endpoint count |
|---|---|---|
| Ecosystem DID | `did:webvh` | 2 (EGF endpoint + Trust Registry endpoint) |
| Trust Registry DID | `did:webvh` | 1 (TRQP service endpoint) |
| Cluster DID | `did:webvh` | 1 (trust metaregistry endpoint) |

The Ayra Trust Network DID is `did:webvh:ayra.forum`. Recognition queries to the ATN
MUST target this DID as `authority_id`.

Automated validation of `did:webvh` format is tracked in `schemas/ayra/` in the CTS
and TSPP repositories. Until that tooling ships, this check is **manual**.

---

## Control mapping

### TRQP-CTRL-01 — Policy publication

**Hub definition:** The operator MUST publish a machine-readable governance framework
declaration reachable at `/.well-known/trqp-metadata`.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Registry self-declaration endpoint | TSPP metadata schema validation (`test_01_metadata.py`) | AL1 |
| `governance_framework_id` references an Ayra-registered URI | `tspp_conformance_report.json` — metadata provenance fields | AL1 |
| Ecosystem DID has EGF service endpoint (`https://ayra.forum/profiles/trqp/egfURI/v1`) | Manual DID document inspection | AL1 |
| Ayra network registration | Ayra member directory entry (out of scope for this toolset) | AL1 |
| `GET /metadata` Ayra extension endpoint present | CTS `ayra_baseline` profile — TC-AYRA-META-001 | AL1 |

**Sufficiency notes:** TSPP `test_01_metadata.py` passing at AL1 is necessary but not
sufficient for Ayra registration. The `governance_framework_id` in the metadata MUST
reference an Ayra-registered governance framework URI, and the ecosystem DID document
MUST expose the EGF service profile URL. Both are currently manual checks.

---

### TRQP-CTRL-02 — Evidence bundle integrity

**Hub definition:** Conformance and posture evidence MUST be packaged in a signed,
hash-pinned evidence bundle to prevent tampering.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Conformance evidence bundle | CTS `manifest.json` + `checksums.json` | AL1 |
| TSPP posture evidence | `tspp_conformance_report.json` + `manifest.sig` | AL2 |
| Combined assurance manifest | Hub `combined-assurance-manifest.json` (via `generate-manifest.py`) | AL2 |
| JWS-signed responses (MUST for all Ayra tiers) | TSPP `test_06_al2_signed_responses.py` | AL2 |

**Sufficiency notes:** Unlike TSPP standalone deployments where JWS signing is optional
at AL1, the **Ayra Profile mandates JWS-signed responses for all trust registries** at
every tier. Response signing is therefore a MUST at Ayra Basic tier and above — not an
AL2 upgrade. The JWS MUST be derived from the controller key of the Trust Registry's
DID document. Key management details SHOULD be documented per TRQP-CTRL-04.

For Ayra Basic tier, an unsigned CTS Baseline bundle is accepted for the conformance
evidence artifact itself. For Cross-Ecosystem and Sovereign tiers, TSPP AL2 signed
report with `manifest.sig` is required.

---

### TRQP-CTRL-03 — Directory lifecycle

**Hub definition:** The registry MUST implement and expose a machine-readable lifecycle
state (active, suspended, revoked) and keep it current.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| GRID status feed schema conformance | CTS GRID status feed verdicts (if GRID profile) | AL1 |
| Registrar listing accuracy | CTS `registrar.schema.json` validation output | AL1 |
| Lifecycle state transitions auditable | Audit log URI in TSPP metadata `audit` block | AL2 |
| `GET /ecosystems/{ecosystem_did}` Ayra extension endpoint | CTS `ayra_baseline` profile — TC-AYRA-ECO-001 | AL1 |
| `GET /ecosystems/{ecosystem_did}/recognitions` extension endpoint | CTS `ayra_baseline` profile — TC-AYRA-ECO-002 | AL2 |

**Sufficiency notes:** Ayra requires registries to participate in the GRID status feed
protocol. Run the CTS with `profiles/grid-profile.yaml` and include the verdicts in the
submission bundle. The Ayra extension lookup endpoints (`/lookups/assuranceLevels`,
`/lookups/authorizations`, `/lookups/didMethods`) are RECOMMENDED for full participation
and are covered by the `ayra_baseline` CTS profile.

---

### TRQP-CTRL-04 — Operator identity assurance

**Hub definition:** The operator MUST bind its identity to the registry via a verifiable
credential or signed attestation at the declared assurance level.

| Ayra Requirement | Evidence | Minimum AL |
|---|---|---|
| Trust Registry DID is `did:webvh` | Manual DID document inspection | AL1 |
| Trust Registry DID has TRQP service endpoint (`https://ayra.forum/profiles/trqp/tr/v2`) | Manual DID document inspection | AL1 |
| JWKS endpoint reachable and pinned | TSPP `test_06_al2_signed_responses.py` — JWKS preflight | AL2 |
| Signed response envelopes (JWS from TR controller key) | TSPP AL2 harness run — `test_06_al2_signed_responses.py` | AL2 |
| Key protection posture declared | TSPP metadata `key_protection` block | AL2 |
| Cluster key management documented | Operator declaration (`examples/al3-evidence-bundle/operator-declaration.md`) | AL3 |
| DPoP for bulk clients | TSPP `test_05_ratelimits.py` — sender-constrained token checks | AL3 |
| HSM-backed keys with `evidence_uri` | TSPP metadata `key_protection.protection: "HSM"` + attestation URI | AL4 |

**Sufficiency notes:** The `did:webvh` requirement for Trust Registry and Cluster DIDs
is normative in the Ayra Profile and not currently validated by automated controls.
For Ayra Sovereign tier, HSM-backed keys (`key_protection.protection: "HSM"`) with an
`evidence_uri` pointing to an independent key attestation are expected. Cluster operators
SHOULD publish a description of their key management approach for the DID document and
the metaregistries that serve cluster state.

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

### Basic member registry (AL1 + CTS Baseline + TSPP AL1)

- [ ] Trust Registry and Ecosystem DIDs are `did:webvh` with correct service endpoints
- [ ] CTS Baseline profile run: all MUST-level tests PASS
- [ ] CTS `ayra_baseline` profile run: TC-AYRA-META-001 PASS
- [ ] TSPP AL1 run: `test_01_metadata.py`, `test_02_freshness.py`, `test_03_context_allowlist.py`,
      `test_04_anti_enumeration.py`, `test_05_ratelimits.py` all PASS
- [ ] TSPP AL2 run: `test_06_al2_signed_responses.py` PASS (JWS required at all Ayra tiers)
- [ ] `combined-assurance-manifest.json` produced by `generate-manifest.py`
- [ ] `operator.security_contact.email` present in TSPP metadata
- [ ] `governance_framework_id` references an Ayra-registered URI

### Cross-ecosystem recognition registry (AL2 + CTS Enterprise + Ayra extension endpoints)

- [ ] All Basic requirements above
- [ ] CTS Enterprise profile run (includes TRQP-FRESH-001/002): all PASS
- [ ] CTS `ayra_baseline` profile: TC-AYRA-ECO-001, TC-AYRA-ECO-002 PASS
- [ ] Recognition query security controls verified (TSPP `test_10_recognition_security.py`)
- [ ] Signed `manifest.sig` included in evidence package
- [ ] `key_protection` block declared in metadata
- [ ] `monitoring.runbook_uri` and `evidence_retention_days` declared (≥ 90 days)
- [ ] `GET /ecosystems/{ecosystem_did}/recognitions` endpoint implemented and responding

### Sovereign / regulated ecosystem (AL3 + CTS High-Assurance)

- [ ] All Cross-Ecosystem requirements above
- [ ] CTS High-Assurance profile run: all gates PASS
- [ ] TSPP AL3 run: `test_08_al3_controls.py` PASS
- [ ] `audit.independent_assessment_uri` present and reachable
- [ ] `key_protection.protection: "HSM"` with `evidence_uri`
- [ ] Cluster key management description published
- [ ] `monitoring.evidence_retention_days` ≥ 365

---

## Ayra extension endpoints reference

The following endpoints are RECOMMENDED by the Ayra Profile for full network
participation. CTS `ayra_baseline` profile includes smoke-level test cases for each.

| Endpoint | Method | CTS Test | Notes |
|---|---|---|---|
| `/metadata` | GET | TC-AYRA-META-001 | Trust Registry identity, controllers, default ecosystem |
| `/entities/{entity_id}` | GET | TC-AYRA-ENT-001 | Entity lookup |
| `/entities/{entity_did}/authorizations` | GET | TC-AYRA-ENT-002 | Entity authorization listing |
| `/ecosystems/{ecosystem_did}` | GET | TC-AYRA-ECO-001 | Ecosystem details |
| `/ecosystems/{ecosystem_did}/recognitions` | GET | TC-AYRA-ECO-002 | Recognized ecosystem listing |
| `/lookups/assuranceLevels` | GET | TC-AYRA-LKP-001 | Supported assurance levels |
| `/lookups/authorizations` | GET | TC-AYRA-LKP-002 | Available action+resource pairs |
| `/lookups/didMethods` | GET | TC-AYRA-LKP-003 | Supported DID methods |

---

## Known gaps and manual checks

The following Ayra requirements are not yet covered by automated controls in this toolset:

- **`did:webvh` format validation** — CTS and TSPP do not yet validate that `entity_id`
  and `authority_id` values conform to `did:webvh` syntax. Tracked in `schemas/ayra/`
  work item in both downstream repos.
- **Recognition chain depth** — Transitive recognition across Ayra clusters (does Cluster
  A recognize Cluster B which recognizes Ecosystem C?) is not tested. Tracked in CTS ROADMAP.
- **EGF service endpoint validation** — Automated resolution of the Ecosystem DID to
  verify the `https://ayra.forum/profiles/trqp/egfURI/v1` service endpoint is present
  is not yet implemented.
- **Ayra network registration** — The act of submitting the ecosystem DID to Ayra for
  governance review and network enrollment is entirely out of scope for this toolset.
