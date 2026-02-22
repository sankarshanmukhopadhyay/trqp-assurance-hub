# Error states

This guide documents common error and failure modes across the TRQP assurance toolchain.

## Categories

- **Configuration errors**: missing environment variables, incorrect base URLs, invalid profile selection
- **Connectivity errors**: DNS failures, TLS issues, timeouts, rate limiting
- **Authorization errors**: missing or invalid credentials, access denied
- **Protocol errors**: malformed responses, invalid schemas, unexpected status codes
- **Posture errors**: missing required headers, weak policies, integrity/signing expectations unmet

## Reporting guidance

For machine-consumed output, prefer structured errors with:
- a stable error code
- a human-readable message
- a remediation hint
- a correlation/run identifier where available
