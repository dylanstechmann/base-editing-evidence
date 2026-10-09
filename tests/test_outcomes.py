import copy
import json
import tempfile
import unittest
from pathlib import Path

from baseevidence.audit import validate_studies
from baseevidence.cli import main
from baseevidence.outcomes import audit_outcomes, outcome_report

ROOT = Path(__file__).resolve().parents[1]


class OutcomeTests(unittest.TestCase):
    def setUp(self):
        self.document = json.loads((ROOT / "data/outcomes.json").read_text(encoding="utf-8"))
        self.studies = validate_studies(json.loads((ROOT / "data/studies.json").read_text(encoding="utf-8")))

    def test_clinical_case_does_not_fill_molecular_or_durability_domains(self):
        report = outcome_report(ROOT / "data/outcomes.json", ROOT / "data/studies.json")
        self.assertEqual(report["documented_domains_by_study"]["cps1-case-2025"], ["adverse_events", "clinical_function"])
        self.assertIn("durability", report["undocumented_domains_in_catalog"]["cps1-case-2025"])
        self.assertIn("dna_product", report["undocumented_domains_in_catalog"]["cps1-case-2025"])
        self.assertFalse(report["functional_rescue_inferred"])
        self.assertEqual(len(report["study_catalog_sha256"]), 64)

    def test_single_case_cannot_be_replicated_by_visits_or_assays(self):
        self.document["observations"][0]["n_independent_units"] = 7
        with self.assertRaisesRegex(ValueError, "single-patient"):
            audit_outcomes(self.document, self.studies)

    def test_unknown_count_and_review_gap_remain_unknown(self):
        row = self.document["observations"][2]
        row["status"] = "not_assessed_in_review"
        report = audit_outcomes(self.document, self.studies)
        self.assertIsNone(report["observations"][2]["n_independent_units"])
        self.assertEqual(report["documented_domains_by_study"][row["study_id"]], [])

    def test_unknown_sources_duplicates_invalid_counts_and_scope_overrides_fail(self):
        for patch in ({"study_id": "unknown"}, {"domain": "rejuvenation"}, {"stage": "human_trial"},
                      {"n_independent_units": True}, {"n_independent_units": 0}, {"source_locator": ""}):
            document = copy.deepcopy(self.document)
            document["observations"][0].update(patch)
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                audit_outcomes(document, self.studies)
        self.document["observations"].append(self.document["observations"][0])
        with self.assertRaises(ValueError):
            audit_outcomes(self.document, self.studies)

    def test_malformed_catalog_member_fails_before_outcome_binding(self):
        with self.assertRaisesRegex(ValueError, "Study must be an object"):
            validate_studies({"schema_version": 1, "studies": [None]})

    def test_invalid_cli_input_leaves_no_report_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text('{"schema_version":1,"observations":[]}', encoding="utf-8")
            output = Path(directory) / "report"
            with self.assertRaises(SystemExit):
                main(["audit-outcomes", str(path), "--studies", str(ROOT / "data/studies.json"), "--out", str(output)])
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
