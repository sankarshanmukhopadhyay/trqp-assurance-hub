# Error states

This guide documents error categories that are relevant for combined assurance.

The goal is determinism: if an error can influence verification or policy outcomes now or later (via caching/storage),
it should be treated as machine-consumed and handled consistently.

## Suggested categories

- **AuthN/AuthZ failures**: missing/invalid credentials, denied access
- **Rate limits**: explicit throttling signals
- **Not found / invalid inputs**: structured client errors
- **Policy denials**: explicit refusal due to policy
- **Transient failures**: upstream outages, timeouts

## Evidence expectations

When an error response is machine-consumed (affects verifier behavior), evidence should capture:

- endpoint + request context (redacted as needed)
- status code and structured error payload
- timestamp
- rationale (why this is expected or acceptable)
