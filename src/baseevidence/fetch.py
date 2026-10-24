"""Live exact-ID Europe PMC retrieval with byte-preserving provenance.

This module performs the retrieval that a receipt records. It issues one
exact-EXT_ID core-metadata query, retains the raw response bytes on disk,
transcribes the indexed record fields, and binds the bytes and the record
block with SHA-256 digests. It adds no interpretation, never re-retrieves an
existing receipt, and authenticates nothing.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

SEARCH_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
RECORD_FIELDS = ("id", "source", "pmid", "pmcid", "doi", "title", "firstPublicationDate")
SCOPE = "Exact-ID indexed metadata and abstract retrieval, not a systematic search or independent validation"


def build_query_url(ext_id):
    """Exact-EXT_ID core query URL; never a serendipitous search."""
    text = str(ext_id if ext_id is not None else "").strip()
    if not text.isdigit():
        raise ValueError("EXT_ID must be a bare numeric PubMed identifier")
    params = urlencode({"query": f"EXT_ID:{text}", "format": "json", "resultType": "core", "pageSize": "1"})
    return f"{SEARCH_URL}?{params}"


def fetch_bytes(url, timeout=60):
    """One live HTTPS GET; the raw response bytes are the unit of provenance."""
    with urlopen(url, timeout=timeout) as response:
        if getattr(response, "status", None) != 200:
            raise ValueError(f"retrieval did not return HTTP 200 for {url}")
        return response.read()


def transcribe_records(payload):
    """Mechanical transcription of indexed fields; no interpretation added."""
    results = (payload or {}).get("resultList", {}).get("result")
    if not isinstance(results, list) or not results:
        raise ValueError("query returned no indexed record to transcribe")
    records = []
    for result in results:
        record = {field: result.get(field) for field in RECORD_FIELDS if isinstance(result, dict) and result.get(field) not in (None, "")}
        if not str(record.get("id", "")).strip() or not str(record.get("title", "")).strip():
            raise ValueError("every transcribed record needs id and title")
        records.append(record)
    return records


def canonical_records_bytes(records):
    """The exact serialization form that validate_receipt binds by records_sha256."""
    return (json.dumps(records, indent=2, allow_nan=False) + "\n").encode("utf-8")


def write_receipt(ext_id, out_path, raw_dir, timeout=60, now=None):
    """Retrieve one record live and write an append-only receipt with retained bytes.

    Refuses to overwrite an existing receipt or a previously retained response:
    a receipt is the record of one retrieval event, not a refreshable cache.
    Returns the written receipt object.
    """
    text = str(ext_id if ext_id is not None else "").strip()
    url = build_query_url(text)
    out_path, raw_dir = Path(out_path), Path(raw_dir)
    raw_path = raw_dir / f"{text}.json"
    if out_path.exists():
        raise ValueError(f"receipt exists already; receipts are append-only: {out_path}")
    if raw_path.exists():
        raise ValueError(f"retained response exists already; responses are append-only: {raw_path}")
    raw_bytes = fetch_bytes(url, timeout=timeout)
    records = transcribe_records(json.loads(raw_bytes.decode("utf-8")))
    retrieved_utc = now or datetime.now(timezone.utc).isoformat()
    response_path = Path(os.path.relpath(raw_path, out_path.parent)).as_posix()
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_bytes(raw_bytes)
    receipt = {
        "retrieved_utc": retrieved_utc,
        "retrieval_method": f"Europe PMC REST search API exact-EXT_ID query accessed online on {retrieved_utc[:10]}; raw response bytes retained at {response_path} and bound by response_sha256; indexed metadata and abstract text transcribed from the API response",
        "scope": SCOPE,
        "queries": [url],
        "response_path": response_path,
        "response_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "records": records,
        "records_sha256": hashlib.sha256(canonical_records_bytes(records)).hexdigest(),
        "limits": f"Raw response bytes are retained at {response_path} and bound by response_sha256. Fields and abstract text were transcribed from the indexed API response and not verified against publisher pages. The subscription full text was not accessed.",
    }
    out_path.write_text(json.dumps(receipt, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return receipt