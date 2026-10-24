import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from baseevidence.cli import main
from baseevidence.receipts import validate_receipt, verify_receipts

ROOT = Path(__file__).resolve().parents[1]


class ReceiptChecks(unittest.TestCase):
    """Structural provenance-receipt validation, not re-retrieval.

    Response bodies and full texts stay in ignored workbench provenance storage
    and cannot be re-fetched offline, so a hash proves which response was
    retrieved, never that an interpretation of it is correct. Receipt records
    use Europe PMC identifiers while study cards cite publisher or PMC pages,
    so record-to-card binding is not mechanically asserted here.
    """

    def receipts(self):
        paths = sorted((ROOT / "data").glob("*receipt*.json"))
        self.assertTrue(paths, "data/ must keep at least one provenance receipt")
        return {path.name: json.loads(path.read_bytes().decode("utf-8-sig")) for path in paths}

    def test_every_committed_receipt_passes_structural_validation(self):
        for name, receipt in self.receipts().items():
            validate_receipt(receipt, name)

    def test_malformed_receipts_fail_structural_validation(self):
        receipt = next(iter(self.receipts().values()))
        for patch in ({"scope": ""}, {"records_sha256": "nothex"}, {"retrieved_utc": "yesterday"},
                      {"queries": []}, {"records": [{"id": "", "title": ""}]}):
            with self.assertRaises(ValueError):
                validate_receipt({**receipt, **patch}, "broken.json")

    def test_verify_receipts_reports_failures_without_raising(self):
        receipt = next(iter(self.receipts().values()))
        with tempfile.TemporaryDirectory() as directory:
            good = Path(directory) / "good.json"
            good.write_text(json.dumps(receipt), encoding="utf-8")
            bad = Path(directory) / "bad.json"
            bad.write_text(json.dumps({**receipt, "scope": " "}), encoding="utf-8")
            report = verify_receipts([good, bad])
            self.assertEqual(report["receipts"]["good.json"], "verified")
            self.assertEqual(report["failures"], ["bad.json"])
            self.assertIn("scope", report["receipts"]["bad.json"])
            self.assertEqual(report["status"], "receipt_integrity_reported_not_retrieved")

    def test_cli_verifies_default_receipts_and_failing_paths_exit_nonzero(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(main(["verify-receipts"]), 0)
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "bad.json"
            bad.write_text("{}", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(main(["verify-receipts", str(bad)]), 1)


if __name__ == "__main__":
    unittest.main()
