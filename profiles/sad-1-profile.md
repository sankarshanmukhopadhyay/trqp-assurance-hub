# SAD-1 Profile (Sovereign Authoritative Directory)

SAD-1 is a **registry-agnostic assurance profile** for evaluating *authoritative digital trust directories*.

It is designed to make TRQP a **meta-assurance framework**: the same evaluation logic can be applied to
sovereign registries, standards directories, and cross-jurisdiction registrar catalogs, including UN/CEFACT GRID
as one concrete instance.

## What SAD-1 covers

SAD-1 evaluates a directory as a *publishable authority surface*:

- **Who is listed** (directory entries, identifiers, roles, scopes)
- **Why they are listed** (admission policy, criteria, and decision records)
- **How listings evolve** (lifecycle, suspension, removal, revocation propagation)
- **How the directory can be verified** (hashes, signatures, transparency, replay resistance)
- **How accountability works** (auditability, incident response, redress, dispute handling)

SAD-1 is intentionally compatible with different publication models:

- API-based directory services
- Publication-based directories (files, feeds, signed bundles)
- Hybrid implementations

## Required artifacts (minimum)

1. **Directory entry** (machine-readable)
   - Conforms to: `schemas/authoritative-directory-entry.schema.json`
   - Example: `examples/authoritative-directory-entry.example.json`

2. **Directory publication manifest** (machine-readable)
   - Conforms to: `schemas/directory-publication-manifest.schema.json`
   - Example: `examples/directory-publication-manifest.example.json`

3. **Status feed** (machine-readable)
   - Conforms to: `schemas/directory-status-feed.schema.json`
   - Example: `examples/directory-status-feed.example.json`

4. **Governance binding**
   - Admission and removal policy
   - Decision record model (who approved what, when, under which policy version)

5. **Verification workflow**
   - How a verifier validates the directory without privileged access
   - See: `docs/guides/directory-assurance-workflow.md`

## Assurance and AL parameterization

SAD-1 is parameterized by TRQP Assurance Levels (AL1–AL4). At higher ALs, the profile tightens:

- provenance requirements for directory entries
- independent audit expectations
- revocation and incident response obligations
- transparency and redress operability

See: `docs/guides/assurance-levels.md` and `docs/guides/directory-assurance-workflow.md`.

## Profiles that implement SAD-1

- **GRID Profile**: `profiles/grid-profile.md` (instance profile aligned to UN/CEFACT directory patterns)
