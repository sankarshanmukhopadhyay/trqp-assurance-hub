---
layout: default
title: TRQP assurance profiles
nav_exclude: true
---

# TRQP assurance profiles

Profiles extend TRQP assurance without redefining TRQP. The protocol specification remains authoritative for core TRQP semantics; each named profile's upstream source remains authoritative for profile semantics. This repository records version-bound derived assurance propositions and evidence.

Each profile lives under `profiles/<name>/profile.yaml` and MUST validate against `schemas/trqp-profile-contract.schema.json`. The contract binds the profile to a TRQP version and an exact upstream source revision. Requirements are resolved separately so that profile-specific policy cannot silently override generic TRQP behaviour.

## Resolution

Validate a contract:

```bash
python tools/validate_trqp_profile.py --profile profiles/example/profile.yaml
```

Resolve a registered profile deterministically:

```bash
python tools/validate_trqp_profile.py --id example --version 0.1.0
```

Unknown or ambiguous profile/version pairs fail explicitly. A run with no selected profile continues to use the existing TRQP assurance path.

## Authority boundary

A profile adapter MAY add tests for profile constraints and extensions. It MUST NOT mutate the meaning of TRQP core requirements. Assurance output must preserve protocol and profile conclusions separately, and missing evidence must never be promoted to success.
