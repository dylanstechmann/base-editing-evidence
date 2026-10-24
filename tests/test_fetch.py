import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from baseevidence.cli import main
from baseevidence.fetch import build_query_url, canonical_records_bytes, transcribe_records, write_receipt
from baseevidence.receipts import validate_receipt


class FakeResponse:
    """Minimal urlopen stand-in; tests never touch the network."""

    def __init__(self, payload, status=200):
        self.status = status
        self._payload = payload

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


PAYLOAD = {
    "resultList": {"result": [{
        "id": "99900001", "source": "MED", "pmid": "99900001",
        "doi": "10.0000/fake.0001",
        "title": "Synthetic example article title.",
        "firstPublicationDate": "2026-01-02",
        "abstractText": "Synthetic abstract text for offline tests only.",
    }]},
}


class FetchChecks(unittest.TestCase):
    """Mocked retrieval only; no test in this file touches the network."""

    def payload_bytes(self):
        return json.dumps(PAYLOAD, indent=1).encode("utf-8")

    def test_query_url_is_exact_id_core_and_rejects_loose_identifiers(self):
        self.assertEqual(
            build_query_url("99900001"),
            "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A99900001&format=json&resultType=core&pageSize=1")
        for bad in ("", " ", "abc", "EXT_ID:1", "99900001 OR 2"):
            with self.assertRaises(ValueError):
                build_query_url(bad)

    def test_write_receipt_retains_and_binds_raw_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            with mock.patch("baseevidence.fetch.urlopen", return_value=FakeResponse(self.payload_bytes())) as retrieval:
                receipt = write_receipt("99900001", Path(directory) / "receipt.json", Path(directory) / "raw", now="2026-10-24T00:00:00+00:00")
            retrieval.assert_called_once()
            self.assertEqual(retrieval.call_args[0][0], build_query_url("99900001"))
            raw_path = Path(directory) / "raw" / "99900001.json"
            raw = self.payload_bytes()
            self.assertEqual(raw_path.read_bytes(), raw)
            self.assertEqual(receipt["response_path"], "raw/99900001.json")
            self.assertEqual(receipt["response_sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(receipt["records_sha256"], hashlib.sha256(canonical_records_bytes(receipt["records"])).hexdigest())
            self.assertEqual(receipt["records"][0]["title"], "Synthetic example article title.")
            validate_receipt(receipt, "receipt.json", base_dir=Path(directory))
            raw_path.write_bytes(raw + b"\n")
            with self.assertRaisesRegex(ValueError, "does not bind"):
                validate_receipt(receipt, "receipt.json", base_dir=Path(directory))

    def test_zero_hits_and_failed_status_write_nothing(self):
        for empty in ({"resultList": {"result": []}}, {}):
            with self.assertRaises(ValueError):
                transcribe_records(empty)
        with mock.patch("baseevidence.fetch.urlopen", return_value=FakeResponse(b"{}", status=404)):
            with tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    write_receipt("99900001", Path(directory) / "receipt.json", Path(directory) / "raw")
                self.assertFalse((Path(directory) / "receipt.json").exists())
                self.assertFalse((Path(directory) / "raw").exists())

    def test_cli_fetch_writes_verifiable_receipt_and_refuses_overwrites(self):
        with tempfile.TemporaryDirectory() as directory:
            out, raw_dir = Path(directory) / "receipt.json", Path(directory) / "raw"
            with mock.patch("baseevidence.fetch.urlopen", return_value=FakeResponse(self.payload_bytes())), redirect_stdout(io.StringIO()):
                self.assertEqual(main(["fetch-receipt", "99900001", "--out", str(out), "--raw-dir", str(raw_dir)]), 0)
                self.assertTrue(out.is_file() and (raw_dir / "99900001.json").is_file())
                with self.assertRaises(SystemExit):
                    main(["fetch-receipt", "99900001", "--out", str(out), "--raw-dir", str(raw_dir)])
            receipt = json.loads(out.read_bytes().decode("utf-8-sig"))
            validate_receipt(receipt, out.name, base_dir=out.parent)


if __name__ == "__main__":
    unittest.main()