import hashlib
import json
import re
import unittest
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class ReceiptChecks(unittest.TestCase):
    """Structural provenance-receipt validation, not re-retrieval.

    Response bodies and full texts stay in ignored workbench provenance storage
    and cannot be re-fetched offline, so a response hash proves which response
    was retrieved, never that an interpretation of it is correct. Receipt records
    use Europe PMC identifiers while study cards cite publisher or PMC pages, so
    record-to-card binding is not mechanically asserted here.
    """

    def receipts(self):
        paths = sorted((ROOT / "data").glob("*receipt*.json"))
        self.assertTrue(paths, "data/ must keep at least one provenance receipt")
        return {path.name: json.loads(path.read_text(encoding="utf-8-sig")) for path in paths}

    @staticmethod
    def urls(receipt):
        listed = receipt.get("queries") or receipt.get("urls") or []
        return ([receipt["url"]] if isinstance(receipt.get("url"), str) else []) + [u for u in listed if isinstance(u, str)]

    def test_every_receipt_cites_a_verifiable_europepmc_retrieval(self):
        for name, receipt in self.receipts().items():
            urls = self.urls(receipt)
            self.assertTrue(urls, f"{name} needs a retrieval URL")
            for url in urls:
                parsed = urlparse(url)
                self.assertEqual(parsed.scheme, "https", name)
                self.assertEqual(parsed.netloc, "www.ebi.ac.uk", name)
                self.assertIn("/europepmc/webservices/rest/", parsed.path, name)
            digest = receipt.get("response_sha256") or receipt.get("records_sha256")
            self.assertIsInstance(digest, str, name)
            self.assertRegex(digest, HEX64, name)
            self.assertIsInstance(receipt.get("scope"), str)
            self.assertTrue(receipt["scope"].strip(), name)
            self.assertIn("retrieved_utc", receipt, name)
            datetime.fromisoformat(receipt["retrieved_utc"])

    def test_recorded_metadata_keeps_identifiers_and_committed_integrity(self):
        for name, receipt in self.receipts().items():
            records = receipt.get("records")
            if records is None:
                continue
            self.assertIsInstance(records, list)
            self.assertTrue(records, name)
            for record in records:
                self.assertTrue(str(record.get("id", "")).strip(), name)
                self.assertTrue(str(record.get("title", "")).strip(), name)
            if "records_sha256" in receipt:
                encoded = json.dumps(records, indent=2, allow_nan=False) + "\n"
                self.assertEqual(hashlib.sha256(encoded.encode("utf-8")).hexdigest(), receipt["records_sha256"], name)


if __name__ == "__main__":
    unittest.main()