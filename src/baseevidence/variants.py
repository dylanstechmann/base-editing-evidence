"""Classify declared single-base variant batches without guide design or clinical use."""

import re

from baseevidence.audit import load
from baseevidence.correction import correction

ORIGINS = {"published_source", "synthetic_example"}
PUBLISHED_REFERENCE = re.compile(r"^(https://\S+|10\.\d{4,9}/\S+|PMID[: ]*\d+)$")
UNACCEPTABLE_KEYS = {"guide_sequence", "guide_rna", "pam", "protospacer", "editing_window",
                     "target_sequence", "genome_position", "chromosome", "position",
                     "delivery", "dose", "efficiency", "off_target", "stage", "model"}


def variant_batch(document):
    """Classify each declared pathogenic-to-corrected single-base direction.

    Only declared published or synthetic rows are accepted. The audit checks
    declared data and classification consistency; it performs no targetability,
    pathogenicity, efficiency or clinical inference, and unknowns stay unknown.
    """
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        raise ValueError("Batch schema_version must be integer 1")
    rows = document.get("declared_variants")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Nonempty declared_variants list required")
    ids, classified = set(), []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Declared variant must be an object")  # noqa: TRY004 -- malformed external data is a CLI validation error
        for field in ("id", "pathogenic_base", "corrected_base", "coordinate_system", "source_reference"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Declared variant needs {field}")
        if row["id"] in ids:
            raise ValueError("Declared variant IDs must be unique")
        ids.add(row["id"])
        origin = row.get("origin")
        if origin not in ORIGINS:
            raise ValueError("origin must declare published_source or synthetic_example; personal or private genomes are not accepted")
        if origin == "published_source" and not PUBLISHED_REFERENCE.match(row["source_reference"]):
            raise ValueError("published_source needs an HTTPS, DOI or PMID source_reference; free text is not a verifiable citation")
        unacceptable = sorted(UNACCEPTABLE_KEYS & set(row))
        if unacceptable:
            raise ValueError(f"Targetability, delivery or scope fields are not accepted: {', '.join(unacceptable)}")
        report = correction(row["pathogenic_base"], row["corrected_base"], coordinate_system=row["coordinate_system"])
        classified.append({"id": row["id"], "origin": origin, "source_reference": row["source_reference"], **report})
    by_direction = {}
    for variant in classified:
        direction = variant["classical_chemistry_direction"] or "outside_classical_chemistry"
        by_direction[direction] = by_direction.get(direction, 0) + 1
    return {"schema_version": 1, "status": "declared_variant_batch_classified_not_designed",
            "variants": classified,
            "counts": {"variants": len(classified),
                       "within_classical_chemistry": sum(v["within_classical_chemistry"] for v in classified),
                       "transversions": sum(v["change_type"] == "transversion" for v in classified),
                       "no_sequence_change": sum(v["change_type"] == "no_sequence_change" for v in classified)},
            "counts_by_direction": dict(sorted(by_direction.items())),
            "guide_design_provided": False, "clinical_protocol_provided": False,
            "limits": ["Each row is a declared direction, not a designed target, and origin declarations are not authenticated.",
                       "A published_source reference is a citation-location pattern, not source authentication.",
                       "No pathogenicity inference, efficiency estimate, off-target assessment or delivery claim is performed.",
                       "A transversion row is classified outside both classical classes; it is not asserted uneditable.",
                       "No dose, protocol, personal-genome or self-treatment guidance is or can be derived from this audit."]}


def variant_batch_report(path):
    document, digest = load(path)
    return {**variant_batch(document), "input_sha256": digest}