import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from baseevidence.cli import main
from baseevidence.variants import UNACCEPTABLE_KEYS, variant_batch

ROOT = Path(__file__).resolve().parents[1]


class VariantBatchChecks(unittest.TestCase):
    """Declared-direction batch classification; no targetability, design or protocol."""

    def setUp(self):
        self.document = json.loads((ROOT / "examples/variant_batch.json").read_text(encoding="utf-8"))
        self.row = {
            "id": "published-row",
            "origin": "published_source",
            "pathogenic_base": "G",
            "corrected_base": "A",
            "coordinate_system": "reference_forward_strand",
            "source_reference": "https://example.org/declared-variant-catalog-entry",
        }

    def test_example_batch_counts_directions_without_designing_anything(self):
        report = variant_batch(self.document)
        self.assertEqual(report["status"], "declared_variant_batch_classified_not_designed")
        self.assertEqual(report["counts"], {"variants": 4, "within_classical_chemistry": 2,
                                            "transversions": 1, "no_sequence_change": 1})
        self.assertEqual(report["counts_by_direction"],
                         {"classical_ABE_chemistry_direction": 1,
                          "classical_CBE_chemistry_direction": 1,
                          "outside_classical_chemistry": 2})
        self.assertFalse(report["guide_design_provided"])
        self.assertFalse(report["clinical_protocol_provided"])
        self.assertEqual({v["origin"] for v in report["variants"]}, {"synthetic_example"})

    def test_personal_genomes_undocumented_origins_and_targetability_fields_fail(self):
        document = {**self.document, "declared_variants": [self.row]}
        self.assertEqual(variant_batch(document)["counts"]["variants"], 1)
        for patch in ({"origin": "personal_genome"}, {"origin": None},
                      {"origin": ""}, {"source_reference": " "}):
            with self.assertRaisesRegex(ValueError, "origin|source_reference"):
                variant_batch({**document, "declared_variants": [{**self.row, **patch}]})
        for key in UNACCEPTABLE_KEYS:
            with self.assertRaisesRegex(ValueError, "not accepted"):
                variant_batch({**document, "declared_variants": [{**self.row, key: "value"}]})

    def test_duplicate_ids_malformed_rows_and_bad_schema_fail(self):
        document = {**self.document, "declared_variants": [self.row, {**self.row, "pathogenic_base": "A"}]}
        with self.assertRaisesRegex(ValueError, "unique"):
            variant_batch(document)
        for bad in ({"declared_variants": []}, {"declared_variants": [None]},
                    {"declared_variants": [self.row]}, {"schema_version": "1", "declared_variants": [self.row]}):
            with self.assertRaises(ValueError):
                variant_batch(bad)

    def test_cli_writes_report_and_preserves_failed_input_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "report"
            with redirect_stdout(io.StringIO()):
                self.assertEqual(main(["audit-variant-batch", str(ROOT / "examples/variant_batch.json"), "--out", str(out)]), 0)
            written = json.loads((out / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(written["counts"]["variants"], 4)
            self.assertEqual(len(written["input_sha256"]), 64)
            bad = Path(directory) / "bad.json"
            bad.write_text(json.dumps({"schema_version": 1, "declared_variants": [{"id": "x", "origin": "personal_genome"}]}), encoding="utf-8")
            failed = Path(directory) / "must-not-exist"
            with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()):
                main(["audit-variant-batch", str(bad), "--out", str(failed)])
            self.assertFalse(failed.exists())


if __name__ == "__main__":
    unittest.main()