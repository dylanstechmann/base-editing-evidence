import json
import unittest
from pathlib import Path

from baseevidence.outcomes import outcome_report

ROOT = Path(__file__).resolve().parents[1]


class SnapshotChecks(unittest.TestCase):
    """The designated current snapshot regenerates byte-for-byte from committed inputs.

    Earlier example snapshots are historical records of earlier inputs and are
    deliberately not regenerated or overwritten. A tranche that changes
    data/studies.json or data/outcomes.json must generate a snapshot into a NEW
    examples directory and update CURRENT_SNAPSHOT in the same commit.
    """

    CURRENT_SNAPSHOT = ROOT / "examples/outcome-audit-delivery/report.json"

    def test_current_snapshot_reproduces_from_committed_inputs(self):
        generated = json.dumps(outcome_report(ROOT / "data/outcomes.json", ROOT / "data/studies.json"),
                               indent=2, allow_nan=False) + "\n"
        committed = self.CURRENT_SNAPSHOT.read_text(encoding="utf-8")
        self.assertEqual(generated, committed)


if __name__ == "__main__":
    unittest.main()