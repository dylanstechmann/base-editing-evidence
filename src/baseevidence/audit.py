"""Classify nucleotide-change chemistry and audit declared cell-count coverage."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

STAGES = {"human_cells", "animal", "human_case", "human_trial", "synthetic"}


def substitution(ref, alt, *, coordinate_system):
    """Classical ABE/CBE conversion class on a declared reference forward strand.

    Complementary changes share a chemistry class. No PAM, sequence window,
    bystander, chromatin, delivery or editor-efficiency inference is performed.
    """
    if coordinate_system != "reference_forward_strand":
        raise ValueError("Declare reference_forward_strand; transcript/strand orientation is not inferred")
    if ref not in {"A", "C", "G", "T"} or alt not in {"A", "C", "G", "T"}:
        raise ValueError("One uppercase unambiguous DNA base is required on each side")
    if ref == alt:
        return "no_sequence_change"
    if (ref, alt) in {("A", "G"), ("T", "C")}:
        return "classical_ABE_conversion_class_only"
    if (ref, alt) in {("C", "T"), ("G", "A")}:
        return "classical_CBE_conversion_class_only"
    return "outside_classical_ABE_CBE_conversion_classes"


def coverage(record):
    """Keep a same-population nested cell-count chain separate from read fractions."""
    if record.get("count_unit") != "cells" or record.get("population_binding") != "same_target_population":
        raise ValueError("Cell counts bound to the same target population are required; reads/alleles cannot substitute")
    keys = ["target_cells", "reached_cells", "intended_edited_cells", "intended_only_cells"]
    counts = [record.get(k) for k in keys]
    if type(counts[0]) is not int or counts[0] <= 0:
        raise ValueError("target_cells must be a positive integer")
    last = counts[0]
    unknown = False
    for value in counts[1:]:
        if value is None:
            unknown = True
            continue
        if type(value) is not int or value < 0 or value > last or unknown:
            raise ValueError("Known cell counts must be nested; do not fill a stage after an unknown denominator")
        last = value
    whole = {k: None if value is None else value / counts[0] for k, value in zip(keys[1:], counts[1:])}
    conditional = {keys[i] + "_given_" + keys[i-1]: None if counts[i] is None or counts[i-1] in (None, 0) else counts[i] / counts[i-1] for i in range(1, 4)}
    return {"whole_population_fractions": whole, "conditional_fractions": conditional,
            "functional_rescue_inferred": False,
            "interpretation": "Nested counts describe this declared cell population. They do not predict tissue benefit, allele correction or long-term clonal outcomes."}


def validate_studies(document):
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    studies = document.get("studies")
    if not isinstance(studies, list) or not studies:
        raise ValueError("Nonempty study list required")
    ids = set()
    for study in studies:
        key = study.get("id")
        if not isinstance(key, str) or not key.strip() or key in ids:
            raise ValueError("Unique nonempty study IDs required")
        ids.add(key)
        for field in ("title", "model", "target_tissue", "intervention_class", "source_report", "functional_scope", "limits", "access_level"):
            if not isinstance(study.get(field), str) or not study[field].strip():
                raise ValueError(f"Study needs {field}")
        if study.get("stage") not in STAGES:
            raise ValueError("Explicit known evidence stage required")
        url = urlparse(study.get("source_url", ""))
        if url.scheme != "https" or not url.netloc:
            raise ValueError("HTTPS source reference required")
    return studies


def _unique(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"Duplicate JSON key: {key}")
        obj[key] = value
    return obj


def load(path):
    raw = Path(path).read_bytes()
    document = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_unique)
    if not isinstance(document, dict):
        raise ValueError("Input must be an object")  # noqa: TRY004 -- malformed external data is a CLI validation error
    return document, hashlib.sha256(raw).hexdigest()


def study_report(path):
    document, digest = load(path)
    studies = validate_studies(document)
    return {"schema_version": 1, "status": "source_scope_audit_not_editor_or_treatment_selection",
            "source_sha256": digest, "studies": studies,
            "counts_by_stage": {stage: sum(s["stage"] == stage for s in studies) for stage in sorted(STAGES)},
            "limits": ["Source reports retain their model and follow-up scope.", "A sequence-change chemistry class does not establish targetability or safety.", "Known monogenic correction is not a model of distributed age-acquired damage.", "Missing functional or adverse-outcome measurements are not evidence of absence."]}
