# Trust Registry Reference Service

A minimal JSON-backed reference service for publishing and discovering trust-service metadata and related assurance artifacts.

## Purpose

This service provides the smallest useful discovery layer for the Operational Stack.

It lets operators and integrators retrieve:

- a list of published trust services,
- a service record,
- the assurance record for that service,
- the conformance record for that service.

## Run

```bash
python app.py --port 8090
```

## Endpoints

- `GET /health`
- `GET /trust-services`
- `GET /trust-services/{service_id}`
- `GET /assurance/{service_id}`
- `GET /conformance/{service_id}`

## Sample service

The sample dataset publishes `demo-registry` and points to:

- an AL2 machine-readable assurance profile,
- an example combined assurance manifest,
- example CTS and TSPP reports.
