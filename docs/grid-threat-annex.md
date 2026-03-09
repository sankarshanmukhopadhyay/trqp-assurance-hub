# GRID threat annex (minimum)

A minimal threat model for GRID-style directories.

## Primary threats

1. **Registrar impersonation**
   - Attack: publish a fake registrar identifier/listing
   - Control: require signed listing + operator-controlled status feed; verify issuer policy

2. **Evidence spoofing**
   - Attack: link to fabricated evidence bundles
   - Control: hash evidence artifacts; require immutable references; publish audit timestamps

3. **Status replay**
   - Attack: replay older “active” status entries
   - Control: monotonic `issued_at`; verifier checks latest signed feed

4. **Governance capture**
   - Attack: directory operator policy changes without transparency
   - Control: publish policy diffs and approval lifecycle; require quorum metadata

5. **Jurisdiction spoofing**
   - Attack: claim authority in a jurisdiction without mandate
   - Control: require authoritative mandate evidence; jurisdictional attestation

This annex is intentionally small: it is a starter pack for implementers, not a complete security assessment.
