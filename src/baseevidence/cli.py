"""Console audit and provenance tools; only fetch-receipt retrieves over the network."""

import argparse
import json
from pathlib import Path

from baseevidence.audit import STAGES, coverage, load, study_report, substitution
from baseevidence.correction import correction
from baseevidence.fetch import write_receipt
from baseevidence.outcomes import DESIGNS, DOMAINS, HIERARCHIES, SIGNAL_ROLES, STATUSES, outcome_report
from baseevidence.receipts import verify_receipts
from baseevidence.variants import variant_batch_report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="command", required=True)
    change = actions.add_parser("change-class", help="Classical nucleotide conversion only, not targetability")
    change.add_argument("ref")
    change.add_argument("alt")
    change.add_argument("--coordinate-system", required=True)
    fix = actions.add_parser("correction-class", help="Declared-correction chemistry direction only, not targetability or protocol")
    fix.add_argument("--pathogenic", required=True)
    fix.add_argument("--corrected", required=True)
    fix.add_argument("--coordinate-system", required=True)
    actions.add_parser("schema", help="Controlled vocabularies only, not validation or interpretation")
    variants = actions.add_parser("audit-variant-batch", help="Classify declared variant corrections; no guide design or protocol")
    variants.add_argument("input")
    variants.add_argument("--out", required=True)
    receipts = actions.add_parser("verify-receipts", help="Structural receipt integrity, not re-retrieval or authentication")
    receipts.add_argument("paths", nargs="*", help="Receipt files; defaults to data/*receipt*.json")
    fetch = actions.add_parser("fetch-receipt", help="Live exact-EXT_ID Europe PMC retrieval; retains raw response bytes, adds no interpretation")
    fetch.add_argument("ext_id")
    fetch.add_argument("--out", required=True)
    fetch.add_argument("--raw-dir", default="data/raw")
    for command in ("audit-studies", "audit-coverage"):
        action = actions.add_parser(command)
        action.add_argument("input")
        action.add_argument("--out", required=True)
    outcomes = actions.add_parser("audit-outcomes", help="Source-linked outcome inventory; no rescue inference")
    outcomes.add_argument("input")
    outcomes.add_argument("--studies", required=True)
    outcomes.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "change-class":
            print(substitution(args.ref, args.alt, coordinate_system=args.coordinate_system))
            return 0
        if args.command == "correction-class":
            print(json.dumps(correction(args.pathogenic, args.corrected,
                                        coordinate_system=args.coordinate_system), indent=2, allow_nan=False))
            return 0
        if args.command == "schema":
            print(json.dumps({"schema_version": 1, "status": "vocabulary_export_not_validation",
                              "study_stages": sorted(STAGES), "outcome_domains": sorted(DOMAINS),
                              "signal_roles": sorted(SIGNAL_ROLES), "observation_statuses": sorted(STATUSES),
                              "comparison_designs": sorted(DESIGNS),
                              "endpoint_hierarchies": sorted(HIERARCHIES)}, indent=2, allow_nan=False))
            return 0
        if args.command == "verify-receipts":
            paths = args.paths or sorted((Path(__file__).resolve().parents[2] / "data").glob("*receipt*.json"))
            if not paths:
                raise ValueError("No receipt paths given and none found under data/")
            report = verify_receipts(paths)
            print(json.dumps(report, indent=2, allow_nan=False))
            return 0 if not report["failures"] else 1
        if args.command == "fetch-receipt":
            receipt = write_receipt(args.ext_id, Path(args.out), Path(args.raw_dir))
            print(json.dumps(receipt, indent=2, allow_nan=False))
            return 0
        if args.command == "audit-studies":
            report = study_report(args.input)
        elif args.command == "audit-outcomes":
            report = outcome_report(args.input, args.studies)
        elif args.command == "audit-variant-batch":
            report = variant_batch_report(args.input)
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
