# DeDi Mapping Matrix (Experimental Spine)

**Purpose:** Provide a single, auditable spine linking **DeDi artifacts** to the TRQP Assurance Hub **control objectives**, the CTS **checks**, and the **expected evidence** patterns.

**Status:** Experimental (non-normative)  
**Upstream:** https://github.com/LF-Decentralized-Trust-labs/decentralized-directory-protocol  
**Snapshot date:** 2026-03-03

## Matrix

| DeDi artifact | Hub control objective (what is being assured) | CTS check (how we validate) | Expected evidence (what an assessor expects) |
|---|---|---|---|
| `public_key` (Public Key Directory) | **Key management & authenticity.** Operator publishes current key material + rotation metadata to enable verifier-grade signature validation. | `dedi_public_key_schema` via `profiles/dedi_experimental.yaml` → `scripts/validate_dedi_artifacts.py --public-key …` | Published `public_key` doc; key rotation procedure; rotation drill evidence at AL3/AL4 (e.g., rotation proof, compromise response runbook). |
| `revoke` (Negative list / revocations) | **Revocation semantics.** Operator can invalidate identifiers/records with timestamps and reason codes; supports downstream safety and dispute handling. | `dedi_revoke_schema` via `profiles/dedi_experimental.yaml` → `… --revoke …` | Published `revoke` doc(s); revocation policy; incident ticket references for AL3/AL4; renewal/reinstatement policy if applicable. |
| `membership` (Affiliation record) | **Directory entry correctness.** Membership assertions are structured, scoped, time-bounded, and reviewable (who is a member, of what, under what status). | `dedi_membership_schema` via `profiles/dedi_experimental.yaml` → `… --membership …` | Published `membership` record(s); governance policy describing issuance and update authority; audit trail or change-log expectations for AL3/AL4. |
| `Beckn_subscriber` (ecosystem record) | **Ecosystem-specific directory integrity.** Subscriber metadata is well-formed and publishable under deterministic integrity expectations. | `dedi_subscriber_schema` via `profiles/dedi_experimental.yaml` → `… --subscriber …` | Published subscriber records; ecosystem governance rules; publication cadence; integrity manifest (recommended) and checksums; operator declaration for higher ALs. |

## Notes on “experimental”

- The Hub’s **AL definitions** remain canonical. This matrix only defines how DeDi artifacts map into Hub controls and evidence patterns.
- CTS checks are currently **schema-level** (structural) and intentionally do not perform cryptographic verification.
- Operators MAY supplement DeDi publishing with Hub-style publication artifacts (e.g., manifest + status feed) to reach higher assurance targets.

## Where this spine is referenced

- **TRQP Assurance Hub:** DeDi experimental profile mapping  
- **TRQP Conformance Suite:** DeDi experimental profile checks  
- **TRQP-TSPP:** DeDi operator posture expectations

