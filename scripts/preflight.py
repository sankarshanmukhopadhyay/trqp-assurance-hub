#!/usr/bin/env python3
"""Preflight checks for a TRQP/TSPP deployment.

This is intentionally lightweight:
  - Confirms the base URL is reachable
  - Optionally checks a list of endpoints return an HTTP response
"""

import argparse
import sys
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def check(url, method="GET", timeout=10):
    req = Request(url, method=method, headers={"User-Agent": "trqp-preflight/0.1"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.status, None
    except HTTPError as e:
        # HTTP error still means server is reachable; report status code
        return e.code, str(e)
    except URLError as e:
        return None, str(e)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True, help="Base URL of the service, e.g. https://example.com/")
    ap.add_argument("--endpoint", action="append", default=[], help="Endpoint path to probe, e.g. /.well-known/jwks.json")
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()

    base = args.base_url if args.base_url.endswith("/") else args.base_url + "/"

    status, err = check(base, timeout=args.timeout)
    if status is None:
        print(f"[FAIL] Base URL not reachable: {base} ({err})")
        return 2
    print(f"[OK] Base URL reachable: {base} (HTTP {status})")

    failed = False
    for ep in args.endpoint:
        url = urljoin(base, ep.lstrip("/"))
        st, er = check(url, timeout=args.timeout)
        if st is None:
            print(f"[FAIL] {url} unreachable ({er})")
            failed = True
        else:
            print(f"[OK] {url} (HTTP {st})")

    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
