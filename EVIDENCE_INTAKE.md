# Evidence-intake checklist for a catalog tranche

This is the repeatable recipe every tranche in this repository has followed.
A tranche adds or revises source cards and outcome observations. It never adds
a guide design, editor ranking, delivery protocol, dose, or clinical
recommendation. Unknown quantities stay `null`; missing domains stay
undocumented, never zero.

## Before adding anything

1. **Select a real source.** A paper or report with an indexed identifier
   (PMID, PMCID or DOI). Do not add a citation that was not retrieved. Do not
   transcribe claims from memory.
2. **Acquire metadata through Europe PMC.** Use the packaged retrieval tool,
   not an ad-hoc script: `PYTHONPATH=src python -m baseevidence.cli
   fetch-receipt <EXT_ID> --out data/<tranche>_receipt.json --raw-dir data/raw`.
   It issues the exact-EXT_ID core query live, retains the raw response bytes
   under `data/raw/`, binds them with `response_sha256`, transcribes the
   indexed record fields into `records`, and binds that block with
   `records_sha256`. `verify-receipts` re-checks retained bytes by local hash;
   it never re-retrieves. Receipts and retained responses are append-only:
   the tool refuses to overwrite either.
3. **Write an honest receipt.** Review the tool-written receipt before
   committing: transcribed fields are mechanical, but the scope and access
   statements are yours to keep honest. Record what was accessed (indexed
   metadata, abstract, full text) and what was *not* (supplementary files,
   datasets, subscription full texts). A response hash proves which response
   was retrieved, not that the interpretation drawn from it is correct. Where
   raw response bytes are not retained by the retrieval tooling, hash the
   committed record block (`records_sha256`) and say so in `scope`.

## Study cards (`data/studies.json`)

4. Every card needs all of: `id`, `title`, `stage` (from `STAGES`), `model`,
   `target_tissue`, `intervention_class`, `source_url` (HTTPS), 
   `source_report`, `functional_scope`, `limits`, `access_level`.
5. `access_level` states exactly what was read: e.g. "Official indexed
   abstract" versus "Primary PMC full-text article page accessed;
   supplementary data not independently reviewed."
6. Scope text separates the model from what it does not establish. A new
   evidence stage requires a `STAGES` vocabulary change and test updates in
   the same commit.

## Outcome observations (`data/outcomes.json`)

7. Rows may only restate what the accessed source text supports. Abstract-only
   access supports abstract-level statements only.
8. Every row needs: `id`, `study_id` (existing card), `outcome`,
   `source_locator`, `comparison`, `comparison_design` (from `DESIGNS`),
   `endpoint_hierarchy` (from `HIERARCHIES`), `independent_unit`,
   `n_independent_units` (positive integer or null), `follow_up`, `limits`,
   `domain` (from `DOMAINS`), `status` (from `STATUSES`), and usually
   `signal_role` (from `SIGNAL_ROLES`; omitted stays unclear).
9. Denominators are explicit or absent. Never convert a read or allele
   fraction into a cell fraction, or a selected necropsy into cumulative
   incidence. `cohort_counts` are disjoint groups summing to
   `n_independent_units` only.

## Snapshot and docs

10. Regenerate the outcome snapshot with the CLI into a **new**
    `examples/outcome-audit-<tranche>/report.json` directory. Never overwrite
    an existing snapshot; earlier directories are historical records. Update
    `CURRENT_SNAPSHOT` in `tests/test_snapshots.py` in the same commit.
11. Update README card counts, add a dated `METHODS.md` acquisition paragraph
    (what was accessed, when, and what was not), and append a dated section to
    `REPORT.md` (chronological order; newest last).
12. Run `PYTHONPATH=src python -m unittest discover -s tests -v` and
    `ruff check src tests`; both must pass before committing. Update any test
    assertions that depend on catalog size.

## Standing prohibitions

- No guide RNA sequences, PAM/targetability analysis, delivery regimens,
  doses, or self-treatment instructions.
- No private patient genomes, credentials, or owner source review claims.
- No pooled efficacy/safety scores, no rescue inference, no turning "no
  detected signal" into zero risk, and no promoting animal or cell evidence
  to human validation.