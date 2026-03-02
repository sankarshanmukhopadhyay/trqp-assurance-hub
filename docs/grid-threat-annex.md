# GRID Threat Annex (Minimum)

This annex lists a minimal set of threats that any GRID-style directory operator should consider.

The goal is not completeness; the goal is to prevent naive deployments.

## Threats

### 1) Registrar impersonation
**Attack:** A malicious party publishes a listing claiming to be a registrar.  
**Mitigation:** Strong DID binding, governance policy hash anchoring, independent evidence.

### 2) Evidence spoofing
**Attack:** Evidence URIs point to fabricated artifacts or mutable content.  
**Mitigation:** Hashes for evidence artifacts; signed bundles; immutable storage where possible.

### 3) Status replay / rollback
**Attack:** Consumers are served an older “active” status after suspension/revocation.  
**Mitigation:** Signed status feed with timestamps; caching and freshness rules; monotonic sequence numbers (optional).

### 4) Governance capture
**Attack:** Legitimate registrar governance is captured and used to publish “valid” but malicious updates.  
**Mitigation:** Quorum / role-based signing; independent oversight signers; transparent audit trail.

### 5) Jurisdictional spoofing
**Attack:** Listing misrepresents legal basis, authority, or jurisdiction.  
**Mitigation:** Human-validated attestations; standardized jurisdiction coding; external references.

## Verifier posture

Verifiers **SHOULD** treat directory data as *claims*, not truth, and validate per the workflow in `docs/how-to-verify-grid.md`.
