import io
import json
import unittest
from contextlib import redirect_stdout

from baseevidence.audit import STAGES
from baseevidence.cli import main
from baseevidence.outcomes import DESIGNS, DOMAINS, HIERARCHIES, SIGNAL_ROLES, STATUSES


class SchemaExportChecks(unittest.TestCase):
    def test_schema_export_matches_module_vocabularies(self):
        """The export lists controlled vocabularies for external pre-validation.

        An exported vocabulary is a declaration of accepted values, not
        validation of any submitted document and not an interpretation of it.
        """
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.assertEqual(main(["schema"]), 0)
        exported = json.loads(buffer.getvalue())
        self.assertEqual(exported["schema_version"], 1)
        self.assertEqual(exported["status"], "vocabulary_export_not_validation")
        self.assertEqual(exported["study_stages"], sorted(STAGES))
        self.assertEqual(exported["outcome_domains"], sorted(DOMAINS))
        self.assertEqual(exported["signal_roles"], sorted(SIGNAL_ROLES))
        self.assertEqual(exported["observation_statuses"], sorted(STATUSES))
        self.assertEqual(exported["comparison_designs"], sorted(DESIGNS))
        self.assertEqual(exported["endpoint_hierarchies"], sorted(HIERARCHIES))


if __name__ == "__main__":
    unittest.main()