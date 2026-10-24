"""Structural provenance-receipt validation; no re-retrieval or authentication."""

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _retrieval_urls(receipt, name):
    listed = receipt.get("queries") or receipt.get("urls") or []
    urls = ([receipt["url"]] if isinstance(receipt.get("url"), str) else []) + [u for u in listed if isinstance(u, str)]
    if not urls:
        raise ValueError(f"{name}: needs a retrieval URL")
    for url in urls:
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != "www.ebi.ac.uk" or "/europepmc/webservices/rest/" not in parsed.path:
            raise ValueError(f"{name}: retrieval must be an HTTPS Europe PMC REST URL")
    return urls


def validate_receipt(receipt, name):
    """Structural checks on one provenance receipt; never re-retrieval.

    A hash proves which response was retrieved, not that any interpretation of
    it is correct. Record-to-card binding and source truth are not authenticated.
    """
    if not isinstance(receipt, dict):
        raise ValueError(f"{name}: receipt must be an object")  # noqa: TRY004 -- malformed external data is a CLI validation error
    _retrieval_urls(receipt, name)
    digest = receipt.get("response_sha256") or receipt.get("records_sha256")
    if not isinstance(digest, str) or not HEX64.match(digest):
        raise ValueError(f"{name}: needs a 64-hex response or records SHA-256")
    scope = receipt.get("scope")
    if not isinstance(scope, str) or not scope.strip():
        raise ValueError(f"{name}: needs a scope statement")
    if "retrieved_utc" not in receipt:
        raise ValueError(f"{name}: needs retrieved_utc")
    try:
        datetime.fromisoformat(receipt["retrieved_utc"])
    except (TypeError, ValueError) as error:
        raise ValueError(f"{name}: retrieved_utc must be ISO format") from error
    records = receipt.get("records")
    if records is None:
        return
    if not isinstance(records, list) or not records:
        raise ValueError(f"{name}: records must be a nonempty list")
    for record in records:
        if not isinstance(record, dict) or not str(record.get("id", "")).strip() or not str(record.get("title", "")).strip():
            raise ValueError(f"{name}: every record needs id and title")  # noqa: TRY004 -- malformed external data is a CLI validation error
    if "records_sha256" in receipt:
        encoded = json.dumps(records, indent=2, allow_nan=False) + "\n"
        if hashlib.sha256(encoded.encode("utf-8")).hexdigest() != receipt["records_sha256"]:
            raise ValueError(f"{name}: records_sha256 does not bind the committed record block")


def verify_receipts(paths):
    """Validate receipt files structurally and report names, not source truth."""
    results = {}
    for path in paths:
        name = Path(path).name
        try:
            receipt = json.loads(Path(path).read_bytes().decode("utf-8-sig"))
            validate_receipt(receipt, name)
            results[name] = "verified"
        except (ValueError, OSError) as error:
            results[name] = str(error)
    return {"schema_version": 1, "status": "receipt_integrity_reported_not_retrieved",
            "receipts": dict(sorted(results.items())),
            "failures": sorted(name for name, result in results.items() if result != "verified"),
            "limits": ["Structural validation checks declared retrieval URLs, digests and record fields.",
                       "A receipt hash proves which response was retrieved, never that an interpretation of it is correct.",
                       "Record-to-study-card binding and source truth are not authenticated by this report."]}