# Architecture

## Components

- Runner
- Profiles
- Requirements Catalog
- Tests
- Evidence Packager

## Data Flow

```mermaid
graph TD
  A[Test Runner] --> B[HTTP Requests to SUT]
  B --> C[HTTP Responses]
  A --> D[Schema + Semantic Validators]
  D --> E[Verdicts (Requirement-level)]
  A --> F[Evidence Packager]
  F --> G[Manifest (hashes)]
  G --> H[Signature (High-Assurance)]
  F --> I[Bundle.zip]
```

## Evidence Bundle

Core artifacts:
- run.json
- verdicts.json
- cases/*
- manifest.json
- manifest.sig (where required)

See `docs/evidence_bundle.schema.json`.
