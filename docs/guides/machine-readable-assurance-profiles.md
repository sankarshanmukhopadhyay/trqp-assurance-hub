# Machine-readable Assurance Profiles

This repository now publishes a small set of machine-readable assurance profiles that make AL1-AL4 usable as **operational contracts**.

## Why these profiles exist

Assurance levels are useful as vocabulary, but vocabulary alone does not tell an implementer what to publish. The profiles in `profiles/` close that gap by declaring:

- the profile identifier,
- the target assurance level,
- the minimum required evidence,
- the expected artifact layout,
- the publication and governance commitments.

That turns assurance into something that can be validated in CI rather than merely argued about in issue threads.

## Published profiles

- `profiles/al1-basic.yaml`
- `profiles/al2-verified.yaml`
- `profiles/al3-audited.yaml`
- `profiles/al4-regulated.yaml`

## Schema

- `schemas/machine-readable-assurance-profile.schema.json`

## Validation

Use:

```bash
python tools/validate_assurance_profile.py profiles/al2-verified.yaml
```

## How to use them

Recommended flow:

1. choose the profile that matches the deployment target,
2. run CTS and TSPP,
3. generate the combined assurance manifest,
4. publish the profile and manifest via the trust registry service.

This keeps the ecosystem honest: profile claims, evidence outputs, and registry publication all line up.
