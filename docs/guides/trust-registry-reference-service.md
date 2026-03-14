# Trust Registry Reference Service

This guide describes the minimal Trust Registry reference service included in the Assurance Hub.

The service is intentionally small. It exists to demonstrate how conformance reports, posture reports, combined manifests, and machine-readable assurance profiles can become **discoverable artifacts**.

## Why a reference service exists

Running CTS and TSPP locally is useful, but it is not enough for ecosystem operations. Parties need a way to discover:

- what trust services are published,
- what evidence artifacts exist for a service,
- what assurance profile is claimed,
- where the combined manifest can be retrieved.

That is the job of a trust registry layer.

## Endpoints

The reference service exposes four GET endpoints:

- `/health`
- `/trust-services`
- `/trust-services/{service_id}`
- `/assurance/{service_id}`
- `/conformance/{service_id}`

These endpoints return JSON from the local `data/` directory.

## Data model

The service expects the following files:

```text
services/trust-registry-reference/data/
  trust-services.json
  services/<service_id>.json
  assurance/<service_id>.json
  conformance/<service_id>.json
```

The sample dataset includes one service, `demo-registry`.

## Running the service

From the repository root:

```bash
python services/trust-registry-reference/app.py --port 8090
```

Then query:

```bash
curl http://localhost:8090/health
curl http://localhost:8090/trust-services
curl http://localhost:8090/trust-services/demo-registry
curl http://localhost:8090/assurance/demo-registry
curl http://localhost:8090/conformance/demo-registry
```

## Intended use

The reference service is appropriate for:

- local demos,
- GitHub Pages-adjacent static data modelling,
- integration tests,
- showing how assurance evidence becomes discoverable.

It is **not** a production-ready registry. That would require stronger authentication, integrity protection, operational controls, and publication governance.

## Relationship to the Operational Stack

The intended flow is:

1. produce CTS and TSPP reports,
2. generate a combined manifest,
3. validate or select a machine-readable assurance profile,
4. publish service and evidence metadata through the trust registry.

In other words, the registry is the discovery surface for the stack's output.
