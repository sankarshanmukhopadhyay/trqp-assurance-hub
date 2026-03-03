# Directory assurance workflow (SAD-1 / GRID)

This guide defines an **end-to-end workflow** for evaluating authoritative digital trust directories using the TRQP ecosystem.

The workflow is designed to be *verifier-first*: a third party should be able to validate core claims without privileged access.

## Outcome

An evaluation produces:

- A directory-specific **profile declaration** (SAD-1 or instance profile such as GRID)
- A set of **evidence artifacts** (schemas, signed manifests, status feeds, governance bindings)
- A **combined assurance manifest** (Hub) linking CTS outputs, TSPP expectations, and directory artifacts
- A publishable **evaluation report** with explicit scope and limitations

## Step 1: Select a profile

- Generic: `profiles/sad-1-profile.md`
- Instance: `profiles/grid-profile.md`

Record:

- target directory identifier
- publication model (API, publication, hybrid)
- intended AL target (AL1–AL4)

## Step 2: Collect directory artifacts

Minimum artifacts are defined by SAD-1:

- directory entries (schema validated)
- publication manifest (hashes, signatures, artifact inventory)
- status feed (lifecycle changes)

Recommended additions at AL3/AL4:

- independent audit statement
- incident response evidence
- redress procedure and operational proofs
- revocation propagation evidence

## Step 3: Validate directory artifacts (schema + integrity)

Validate JSON artifacts against Hub schemas:

- `schemas/authoritative-directory-entry.schema.json`
- `schemas/directory-publication-manifest.schema.json`
- `schemas/directory-status-feed.schema.json`

Then validate integrity:

- digests match the referenced artifacts
- signatures verify against declared keys
- status feed events are consistent with entry states

## Step 4: Run TRQP CTS (conformance)

Run the TRQP Conformance Suite against the SUT TRQP endpoints using an appropriate profile, for example:

- `profiles/smoke.yaml` for quick checks
- `profiles/high_assurance.yaml` for stricter gating

The CTS output becomes evidence linked into the combined assurance manifest.

## Step 5: Apply TSPP controls (security and privacy)

Use TSPP to evaluate the security and privacy posture of the directory's publication and operational model:

- publication authenticity and replay resistance
- access control for administrative actions
- logging, monitoring, and incident response
- privacy constraints around directory metadata

## Step 6: Build the combined assurance manifest

Use Hub tooling to generate a combined manifest that binds:

- directory artifacts (SAD-1 / GRID)
- CTS outputs
- TSPP outputs
- AL target and scope

See: `schemas/combined-assurance-manifest.schema.json`.

## Step 7: Produce an evaluation report

Use the Hub report template:

- What was evaluated
- What evidence was available
- Which controls were satisfied
- What is out of scope
- What would change the verdict at higher ALs

## Notes

This workflow supports evaluation with partial evidence. The report MUST state limitations and should mark any higher-AL claims as **not evaluable** without additional artifacts.

## Step 4A: Validate identity anchoring (DIA)

If the evaluated directory binds subjects to an identity anchoring mechanism (for example UNTP DIA), the assessor should:

- verify that any published DIA credentials are syntactically valid JSON-LD and reference the correct context
- verify that issuer identifiers (for example DIDs) are resolvable via the declared method or resolver
- verify that revocation/status mechanisms are published and operational (if applicable)

Evidence outputs should be captured in the evidence bundle as identity anchor artifacts and verification notes.

### Step 6A — Supply chain integrity evidence (recommended for AL3+)

Collect and validate implementation supply chain integrity evidence aligned to **TSPP-SCI**:

- SBOM for deployed artifacts (`software_sbom`)
- Build provenance / attestation (`build_provenance`)
- Scorecard output or equivalent posture evidence (`openssf_scorecard_report`)

This step treats the directory as a **composite trust system**: governance + publication + anchoring + software integrity.
