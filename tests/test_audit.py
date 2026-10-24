import copy
import json
import tempfile
import unittest
from pathlib import Path

from baseevidence.audit import (
    coverage,
    load,
    study_report,
    substitution,
    validate_studies,
)
from baseevidence.cli import main

ROOT = Path(__file__).resolve().parents[1]


class AuditChecks(unittest.TestCase):
    def setUp(self):
        self.counts = json.loads((ROOT / "examples/coverage.json").read_text())

    def test_strand_complements_have_same_class_without_targetability_claim(self):
        for a, b in [("AG", "TC"), ("CT", "GA")]:
            self.assertEqual(substitution(*a, coordinate_system="reference_forward_strand"), substitution(*b, coordinate_system="reference_forward_strand"))
        self.assertEqual(substitution("A", "T", coordinate_system="reference_forward_strand"), "outside_classical_ABE_CBE_conversion_classes")

    def test_ambiguous_bases_and_unstated_strand_fail(self):
        for ref, alt, strand in [("N","A","reference_forward_strand"), ("AA","G","reference_forward_strand"), ("A","G","transcript"), ("a","g","reference_forward_strand")]:
            with self.assertRaises(ValueError):
                substitution(ref, alt, coordinate_system=strand)

    def test_whole_population_fraction_is_not_conditional_edit_fraction(self):
        result = coverage(self.counts)
        self.assertEqual(result["whole_population_fractions"]["intended_only_cells"], .25)
        self.assertEqual(result["conditional_fractions"]["intended_edited_cells_given_reached_cells"], .6)
        self.assertFalse(result["functional_rescue_inferred"])

    def test_unknown_is_not_zero_and_zero_denominator_is_not_a_rate(self):
        self.counts.update(reached_cells=0, intended_edited_cells=0, intended_only_cells=0)
        self.assertEqual(coverage(self.counts)["whole_population_fractions"]["intended_only_cells"], 0)
        self.assertIsNone(coverage(self.counts)["conditional_fractions"]["intended_only_cells_given_intended_edited_cells"])
        self.counts.update(reached_cells=None, intended_edited_cells=None, intended_only_cells=None)
        self.assertIsNone(coverage(self.counts)["whole_population_fractions"]["intended_only_cells"])

    def test_reads_non_nested_counts_and_boolean_counts_are_rejected(self):
        for patch in [{"count_unit":"reads"}, {"target_cells":True}, {"intended_only_cells":301}, {"reached_cells":None}]:
            record = {**self.counts, **patch}
            with self.assertRaises(ValueError):
                coverage(record)

    def test_curated_sources_have_scopes_and_no_inherited_human_validation(self):
        report = study_report(ROOT / "data/studies.json")
        self.assertEqual(len(report["studies"]), 23)
        self.assertEqual(report["counts_by_stage"]["human_cells"], 7)
        self.assertEqual(report["counts_by_stage"]["animal"], 7)
        self.assertEqual(report["counts_by_stage"]["human_case"], 1)
        self.assertEqual(report["counts_by_stage"]["plant"], 3)
        self.assertEqual(report["counts_by_stage"]["human_cohort"], 2)
        self.assertEqual(report["counts_by_stage"]["human_trial"], 3)
        by_id = {study["id"]: study for study in report["studies"]}
        self.assertEqual(by_id["kcnj13-retina-2023"]["stage"], "animal")
        self.assertEqual(by_id["col7a1-rdeb-2022"]["stage"], "human_cells")
        self.assertEqual(by_id["plant-cbe-2017"]["stage"], "plant")
        self.assertEqual(by_id["plant-cbe-offtargets-2019"]["stage"], "plant")
        self.assertEqual(by_id["cancer-be-screens-2026"]["stage"], "animal")
        self.assertEqual(by_id["car-t-pik3cd-2026"]["stage"], "animal")
        self.assertEqual(by_id["clonal-hematopoiesis-2014"]["stage"], "human_cohort")
        self.assertEqual(by_id["stemcell-mutation-accumulation-2016"]["stage"], "human_cohort")
        self.assertEqual(by_id["tyr-ipsc-correction-2025"]["stage"], "human_cells")
        self.assertEqual(by_id["rice-seedcoat-cbe-2021"]["stage"], "plant")
        self.assertEqual(by_id["pcsk9-primates-2021"]["stage"], "animal")
        self.assertEqual(by_id["pcsk9-macaques-2021"]["stage"], "animal")
        self.assertEqual(by_id["pcsk9-vereve102-humans-2026"]["stage"], "human_trial")
        self.assertEqual(by_id["pcsk9-yolt101-humans-2026"]["stage"], "human_trial")
        self.assertEqual(by_id["sickle-beacon-risto-2026"]["stage"], "human_trial")
        studies = copy.deepcopy(report["studies"])
        studies[0]["functional_scope"] = ""
        with self.assertRaises(ValueError):
            validate_studies({"schema_version":1,"studies":studies})

    def test_duplicate_json_keys_fail_before_hash_can_qualify_data(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "input.json"
            file.write_text('{"target_cells":100,"target_cells":10}')
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                load(file)

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "output"
            out.mkdir()
            (out / "sentinel").write_text("saved")
            with self.assertRaises(SystemExit):
                main(["audit-coverage",str(ROOT / "examples/coverage.json"),"--out",str(out)])
            self.assertEqual((out / "sentinel").read_text(), "saved")


if __name__ == "__main__":
    unittest.main()
