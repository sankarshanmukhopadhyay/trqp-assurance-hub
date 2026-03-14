#!/usr/bin/env python3
"""Minimal JSON-backed Trust Registry reference service."""
from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict | list) -> None:
    body = json.dumps(payload, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class RegistryHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        parts = [p for p in parsed.path.split("/") if p]

        try:
            if not parts:
                return json_response(self, HTTPStatus.OK, {
                    "service": "trust-registry-reference",
                    "status": "ok",
                    "endpoints": [
                        "/health",
                        "/trust-services",
                        "/trust-services/{service_id}",
                        "/assurance/{service_id}",
                        "/conformance/{service_id}",
                    ],
                })
            if parts == ["health"]:
                return json_response(self, HTTPStatus.OK, {"status": "ok"})
            if parts == ["trust-services"]:
                return json_response(self, HTTPStatus.OK, load_json(DATA / "trust-services.json"))
            if len(parts) == 2 and parts[0] == "trust-services":
                return json_response(self, HTTPStatus.OK, load_json(DATA / "services" / f"{parts[1]}.json"))
            if len(parts) == 2 and parts[0] == "assurance":
                return json_response(self, HTTPStatus.OK, load_json(DATA / "assurance" / f"{parts[1]}.json"))
            if len(parts) == 2 and parts[0] == "conformance":
                return json_response(self, HTTPStatus.OK, load_json(DATA / "conformance" / f"{parts[1]}.json"))
            return json_response(self, HTTPStatus.NOT_FOUND, {"error": "not_found", "path": parsed.path})
        except FileNotFoundError:
            return json_response(self, HTTPStatus.NOT_FOUND, {"error": "not_found", "path": parsed.path})

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def main() -> int:
    ap = argparse.ArgumentParser(description="Run the minimal Trust Registry reference service")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", default=8090, type=int)
    args = ap.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), RegistryHandler)
    print(f"Trust Registry reference service listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
