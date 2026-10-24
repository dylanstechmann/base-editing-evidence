import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from baseevidence.audit import substitution
from baseevidence.correction import correction
from baseevidence.cli import main

ROOT = Path(__file__).resolve().parents[1]


class CorrectionChecks(unittest.TestCase):
    def test_classical_directions_are_transitions_without_targetability(self):
        for ref, alt, direction in [("C", "T", "classical_CBE_chemistry_direction"),
                                    ("G", "A", "classical_CBE_chemistry_direction"),
                                    ("A", "G", "classical_ABE_chemistry_direction"),
                                    ("T", "C", "classical_ABE_chemistry_direction")]:
            report = correction(ref, alt, coordinate_system="reference_forward_strand")
            self.assertTrue(report["within_classical_chemistry"])
            self.assertEqual(report["change_type"], "transition")
            self.assertEqual(report["classical_chemistry_direction"], direction)
            self.assertFalse(report["functional_rescue_inferred"])
            self.assertFalse(report["clinical_protocol_provided"])

    def test_every_transversion_is_outside_both_classes(self):
        for ref, alt in [("A", "T"), ("T", "A"), ("A", "C"), ("C", "A"),
                         ("T", "G"), ("G", "T"), ("C", "G"), ("G", "C")]:
            report = correction(ref, alt, coordinate_system="reference_forward_strand")
            self.assertFalse(report["within_classical_chemistry"])
            self.assertIsNone(report["classical_chemistry_direction"])
            self.assertEqual(report["change_type"], "transversion")
            self.assertIn("outside both classical conversion classes", report["interpretation"])

    def test_identical_bases_do_not_declare_a_correction(self):
        report = correction("C", "C", coordinate_system="reference_forward_strand")
        self.assertEqual(report["conversion_class"], "no_sequence_change")
        self.assertEqual(report["change_type"], "no_sequence_change")
        self.assertFalse(report["within_classical_chemistry"])

    def test_ambiguous_bases_multibase_and_unstated_strand_fail(self):
        for ref, alt, strand in [("N", "A", "reference_forward_strand"),
                                 ("C", "U", "reference_forward_strand"),
                                 ("CC", "TT", "reference_forward_strand"),
                                 ("c", "t", "reference_forward_strand"),
                                 ("G", "A", "transcript")]:
            with self.assertRaises(ValueError):
                correction(ref, alt, coordinate_system=strand)

    def test_direction_classification_agrees_with_substitution_class(self):
        for ref, alt in [("C", "T"), ("G", "A"), ("A", "G"), ("T", "C"),
                         ("A", "T"), ("C", "G"), ("C", "C")]:
            self.assertEqual(correction(ref, alt, coordinate_system="reference_forward_strand")["conversion_class"],
                             substitution(ref, alt, coordinate_system="reference_forward_strand"))

    def test_cli_prints_class_json_without_protocol_fields(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(["correction-class", "--pathogenic", "G", "--corrected", "A",
                              "--coordinate-system", "reference_forward_strand"])
        self.assertEqual(exit_code, 0)
        report = json.loads(buffer.getvalue())
        self.assertEqual(report["classical_chemistry_direction"], "classical_CBE_chemistry_direction")
        self.assertFalse(report["clinical_protocol_provided"])
        self.assertNotIn("guide_sequence", report)
        self.assertNotIn("dose", report)

    def test_cli_rejects_unstated_coordinate_conventions(self):
        with self.assertRaises(SystemExit):
            main(["correction-class", "--pathogenic", "A", "--corrected", "T", "--coordinate-system", "transcript"])


if __name__ == "__main__":
    unittest.main()