import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from baseevidence.cli import main
from baseevidence.outcomes import outcome_report

ROOT = Path(__file__).resolve().parents[1]


class SnapshotChecks(unittest.TestCase):
    """The designated current snapshot regenerates byte-for-byte from committed inputs.

    Earlier example snapshots are historical records of earlier inputs and are
    deliberately not regenerated or overwritten. A tranche that changes
    data/studies.json or data/outcomes.json must generate a snapshot into a NEW
    examples directory and update CURRENT_SNAPSHOT in the same commit.
    """

    CURRENT_SNAPSHOT = ROOT / "examples/outcome-audit-domain-gaps/report.json"

    def test_current_snapshot_reproduces_from_committed_inputs(self):
        generated = json.dumps(outcome_report(ROOT / "data/outcomes.json", ROOT / "data/studies.json"),
                               indent=2, allow_nan=False) + "\n"
        committed = self.CURRENT_SNAPSHOT.read_text(encoding="utf-8")
        self.assertEqual(generated, committed)

    def test_cli_regenerates_current_snapshot_byte_for_byte(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output"
            with redirect_stdout(io.StringIO()):
                exit_code = main(["audit-outcomes", str(ROOT / "data/outcomes.json"),
                                  "--studies", str(ROOT / "data/studies.json"), "--out", str(output)])
            self.assertEqual(exit_code, 0)
            self.assertEqual((output / "report.json").read_bytes(), self.CURRENT_SNAPSHOT.read_bytes())


if __name__ == "__main__":
    unittest.main()