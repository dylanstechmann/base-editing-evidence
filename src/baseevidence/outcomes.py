"""Audit source-linked outcome coverage without ranking editors or inferring rescue."""

from baseevidence.audit import load, validate_studies

DOMAINS = {"dna_product", "rna_outcomes", "structural_dna", "delivery", "molecular_function",
           "tissue_function", "clinical_function", "adverse_events", "durability", "clonal_behavior"}
STATUSES = {"source_reports_signal", "source_reports_no_signal", "source_reports_mixed", "not_assessed_in_review"}
DESIGNS = {"between_groups", "within_subject", "uncontrolled_case", "no_comparator", "not_stated"}
HIERARCHIES = {"primary", "secondary", "post_hoc", "exploratory", "not_stated"}


def audit_outcomes(document, studies):
    """Source catalog membership binds stage/model; observation text needs review.

    Missing rows mean undocumented in this catalog, never unmeasured in the paper.
    No source acquisition, causal inference or biological validation is performed.
    """
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        raise ValueError("Outcome schema_version must be integer 1")
    sources = {study["id"]: study for study in studies}
    rows = document.get("observations")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Nonempty outcome observations required")
    ids, qualified = set(), []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Outcome observation must be an object")  # noqa: TRY004 -- malformed external data is a CLI validation error
        for field in ("id", "study_id", "outcome", "source_locator", "comparison", "independent_unit", "follow_up", "limits"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Outcome observation needs {field}")
        if row["id"] in ids or row["study_id"] not in sources:
            raise ValueError("Outcome IDs must be unique and study IDs must exist")
        ids.add(row["id"])
        for field, allowed in (("domain", DOMAINS), ("status", STATUSES),
                               ("comparison_design", DESIGNS), ("endpoint_hierarchy", HIERARCHIES)):
            if row.get(field) not in allowed:
                raise ValueError(f"Outcome observation needs known {field}")
        count = row.get("n_independent_units")
        if count is not None and (type(count) is not int or count < 1):
            raise ValueError("n_independent_units must be a positive integer or null")
        source = sources[row["study_id"]]
        if source["stage"] == "human_case" and count not in (None, 1):
            raise ValueError("A single-patient case cannot acquire independent units from visits or assays")
        if any(key in row for key in ("stage", "model", "source_url")):
            raise ValueError("Stage, model and URL come from the source catalog, not outcome overrides")
        qualified.append({**row, "stage": source["stage"], "model": source["model"],
                          "source_url": source["source_url"], "access_level": source["access_level"]})
    documented = {key: sorted({row["domain"] for row in qualified if row["study_id"] == key
                              and row["status"] != "not_assessed_in_review"}) for key in sources}
    return {"schema_version": 1, "status": "source_linked_outcome_inventory",
            "observations": qualified,
            "documented_domains_by_study": documented,
            "undocumented_domains_in_catalog": {key: sorted(DOMAINS - set(domains)) for key, domains in documented.items()},
            "functional_rescue_inferred": False, "causal_effect_estimated": False,
            "limits": ["Observation text and declared hierarchy are not authenticated by schema validation.",
                       "Undocumented domains are gaps in this catalog, not proof the source omitted an assay.",
                       "No combined efficacy, safety or evidence-quality score is calculated.",
                       "Molecular changes, organ function, clinical response and durable clonal outcomes stay distinct."]}


def outcome_report(outcome_path, study_path):
    document, digest = load(outcome_path)
    catalog, source_digest = load(study_path)
    return {**audit_outcomes(document, validate_studies(catalog)),
            "outcomes_sha256": digest, "study_catalog_sha256": source_digest}
