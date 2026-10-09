"""Console audit outputs to a new directory; no network or editing execution."""

import argparse
import json
from pathlib import Path

from baseevidence.audit import coverage, load, study_report, substitution


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="command", required=True)
    change = actions.add_parser("change-class", help="Classical nucleotide conversion only, not targetability")
    change.add_argument("ref")
    change.add_argument("alt")
    change.add_argument("--coordinate-system", required=True)
    for command in ("audit-studies", "audit-coverage"):
        action = actions.add_parser(command)
        action.add_argument("input")
        action.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "change-class":
            print(substitution(args.ref, args.alt, coordinate_system=args.coordinate_system))
            return 0
        if args.command == "audit-studies":
            report = study_report(args.input)
        else:
            document, digest = load(args.input)
            if document.get("origin") != "synthetic_example":
                raise ValueError("This demonstration input must declare synthetic_example")
            report = {"schema_version": 1, "origin": document["origin"], "input_sha256": digest, "audit": coverage(document)}
        encoded = json.dumps(report, indent=2, allow_nan=False) + "\n"
        output = Path(args.out)
        output.mkdir(parents=True, exist_ok=False)
        (output / "report.json").write_text(encoded, encoding="utf-8")
        print(encoded)
        return 0
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
