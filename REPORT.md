# First release — 2026-10-09

The AI assistant created this independent research repository at the user's
request. It contains five scoped source cards, a classical conversion classifier,
a nested cell-count audit, exact-byte provenance, a command-line interface and
GitHub CI for Python 3.11/3.12.

The constructed 1,000-cell example demonstrates the difference between a 60%
conditional intended-edit rate and 25% whole-population intended-only coverage.
Those numbers are synthetic. Eight tests cover strand complements, unsupported
coordinate conventions, denominator distinctions, unknown-versus-zero handling,
count validity, source scopes, duplicate JSON keys and preserved existing outputs.

No biological editing experiment, new editor, patient-specific design, tissue
repair or age reversal is produced. No private patient data are used. The
research desk, organoid solver and this repo retain independent Git histories.

# Outcome inventory follow-up — 2026-10-09

Added a source-linked outcome audit with three scoped observations, explicit
comparison design, endpoint hierarchy, independent units and follow-up. The
ten-domain inventory reports catalog gaps without inferring missing source
assays, clinical rescue or an efficacy score. The original single-patient case
cannot gain independent patients from repeated visits.

All 14 unit tests passed in Docker `dev`. The CLI generated
[the example report](examples/outcome-audit/report.json) from the committed
source cards and outcome records, retaining both input hashes. New module,
CLI and tests passed Ruff. This is software/source-scope validation; no
editing experiment or new clinical follow-up was performed.

## Progeria-model and signal-role follow-up — 2026-10-09

The catalog now has six source cards. Three new observations retain molecular,
vascular and survival scope in the 2021 mouse genetic-disease model. Signal-role
indexing separates benefit, harm and measurement context; unknown roles stay
unclear. Survival is separate from clinical function and durable molecular
correction. None of those animal outcomes is promoted to ordinary-aging repair.

All 17 unit tests passed in Docker `dev`; the changed outcome module and tests
passed Ruff. The [new CLI snapshot](examples/outcome-audit-progeria/report.json)
retains exact hashes of both current inputs. The earlier example report remains
the historical snapshot from the five-card catalog. No new biological experiment,
clinical follow-up or source-review signoff by the owner is implied.

## Full-text cohort and adverse-outcome follow-up — 2026-10-09

The focused progeria review now includes ten catalog observations in total.
Separate longevity rows retain 11/12 and 10/12 treated/control mouse counts;
selected necropsies, vector integration and the negative relative-mutation-
composition assay keep their own denominators and interpretation limits.
The paper's unresolved tumor causation and analysis-specific mouse counts
remain visible. Source survival statistics were recorded, not recalculated.

Optional disjoint `cohort_counts` declarations must sum to a known independent-
unit count. They do not authorize pooling assays, repeated visits or overlapping
groups. All 19 tests passed in Docker `dev`; the changed module and tests passed
Ruff. The [current CLI report](examples/outcome-audit-fulltext/report.json)
retains the updated input hashes. Earlier reports remain historical snapshots.

## Editor precision and function comparison — 2026-10-09

Four primary-source cards now cover engineered CBE off-target reduction,
COL7A1 correction in RDEB patient cells and a skin-equivalent construct,
KCNJ13 correction with retinal function measurements in an engineered disease
model, and the ABE8e-Y149V precision and HTI mouse study. Seven outcome records
keep sequence products, protein restoration, retinal function, embryo SNVs and
mouse disease-model response separate. Exact independent-unit counts remain
unknown where the reviewed source details did not support a clean count.

The review emphasizes that allele/read fractions do not establish edited-cell
coverage, engineered tissue protein deposition is not patient-level healing,
and a short-term disease-model rescue is not ordinary-aging repair. The HTI
mouse experiment disrupted Hpd to bypass the Fah defect; it did not repair the
causal mutation. The selected primary articles and access limits are documented
in [METHODS.md](METHODS.md) and the
[comparison](EDITOR_PRECISION_FUNCTION_COMPARISON.md).

All 19 unit tests passed locally after updating the source-count assertion for
the expanded catalog. The [precision outcome snapshot](examples/outcome-audit-precision/report.json)
retains exact SHA-256 hashes of the outcome and study inputs. This tranche adds
no guide design or clinical protocol.

## Correction-direction classifier and human-use scope — 2026-10-24

Added `correction-class`, a direction-only classification of a declared
pathogenic-to-corrected single-base change against the classical ABE/CBE
conversion classes, with seven unit tests covering both classical
directions, every transversion, identical bases, ambiguous input, CLI
output and unstated coordinate conventions. A new
[correction-direction scope note](CORRECTION_SCOPE.md) maps the three most
requested goals — cancer-driver lesions, aging and appearance traits in
healthy adults — onto the evidence stages this catalog documents, citing
two pigmentation reviews verified through Europe PMC indexed metadata
only. No guide design, editor ranking, delivery protocol, dose or clinical
recommendation is produced, and the note records that healthy-adult
enhancement use is not established by any catalog card.

## Plant-stage source cards — 2026-10-24

Added a `plant` evidence stage and two abstract-level crop-plant cards: the
2017 Cas9-cytidine-deaminase fusion study reporting targeted C-to-T
conversion in rice, wheat and maize protoplasts and regenerated plants, and
the 2019 rice whole-genome study reporting genome-wide C-to-T-enriched
off-target variants for BE3 and HF1-BE3, but not ABE, including without
single-guide RNA. Metadata was retrieved through exact-EXT_ID Europe PMC
queries and is bound by a records-hash
[receipt](data/plant_metadata_receipt.json); full texts were not accessed.
Two outcome rows keep on-target conversion (context) and genome-wide
off-target findings (harm) in separate domains, and independent-unit
counts stay unknown where the accessed abstracts do not state them. The
current outcome snapshot is `examples/outcome-audit-plants/report.json`;
the precision snapshot remains the historical record of the earlier
catalog. All 29 unit tests and Ruff pass. No guide design, agronomic,
ecological or deployment claim is added.

## Vocabulary export — 2026-10-24

Added `baseevidence schema`, which prints the controlled vocabularies
(`study_stages`, outcome `domains`, `signal_roles`, observation `statuses`,
`comparison_designs` and `endpoint_hierarchies`) plus a schema version and
a `vocabulary_export_not_validation` status marker, so external intake
tooling can pre-validate declared fields before submission. The export
declares accepted values; it validates no document and interprets nothing.
One new unit test asserts the export matches the module constants. All 30
unit tests and Ruff pass.

## Cancer-model source cards — 2026-10-24

Added two abstract-level cancer-model cards: the 2026 Nature Biotechnology
inducible split base-editor study (small-molecule-controllable split
engineered base editors enabling in vivo cancer functional-genomics
screens, with reduced cellular toxicity and an Adar1 tiling screen) and
the 2026 Nature Cancer CAR-adapted PIK3CD study (E81K enhancing 4-1BBz CAR
T-cell persistence and in vivo efficacy; L32P improving 28z CAR T-cell
memory). Metadata was retrieved through exact-EXT_ID Europe PMC queries
and is bound by a records-hash [receipt](data/cancer_metadata_receipt.json);
full texts were not accessed. Two outcome rows keep screen-level mutagenesis
findings (context) and preclinical engineered-cell potency (benefit) in
separate domains, with unknown denominators where the accessed abstracts
do not state them. The current outcome snapshot is
`examples/outcome-audit-cancer/report.json`; earlier snapshots remain
historical. All 30 unit tests and Ruff pass. No tumor-lesion-correction,
dosing or clinical claim is added.

## Declared-variant batch intake — 2026-10-24

Added `audit-variant-batch`, an in-silico batch classifier for declared
pathogenic-to-corrected single-base directions, with a synthetic example
input (`examples/variant_batch.json`). Rows must declare `published_source`
or `synthetic_example` origin plus a source reference; personal-genome rows
and targetability, guide, delivery, dose or scope fields are rejected with
explicit errors. Reports tally classical chemistry directions,
transversions and no-change rows without pathogenicity, efficiency,
off-target or protocol inference. Four new unit tests cover counts, origin
and field rejection, duplicate/malformed rows and CLI directory behavior.
All 34 unit tests and Ruff pass.

## Aging-damage context cards — 2026-10-24

Added a `human_cohort` evidence stage and two abstract-level observational
aging cards: the 2014 age-related clonal hematopoiesis study (17,182-person
cohort; detectable blood mutations rising from 9.5% at 70-79 to 18.4% at
90-108 years; mostly DNMT3A/TET2/ASXL1; source-reported hazard ratios for
hematologic cancer, all-cause mortality, coronary heart disease and ischemic
stroke) and the 2016 tissue-specific adult-stem-cell mutation accumulation
study (approximately 40 novel mutations per year across donors aged 3 to 87;
tissue-specific spectra; low inter-individual variation). Metadata was
retrieved through exact-EXT_ID Europe PMC queries and is bound by a
records-hash [receipt](data/aging_metadata_receipt.json); full texts were
not accessed. Four outcome rows keep clone prevalence (context), adverse
associations (harm), mortality association (harm) and stem-cell mutation
rates (context) in separate domains, with person denominators stated only
where the accessed abstract states them. These cards quantify distributed
age-acquired damage; they are not editing precedents, targetable lesion
lists or rejuvenation results. The current outcome snapshot is
`examples/outcome-audit-aging/report.json`; earlier snapshots remain
historical. All 34 unit tests and Ruff pass.

## Appearance-trait editing precedents — 2026-10-24

Added two abstract-level appearance-trait editing cards plus a receipt that
also binds the two pigmentation-genetics review citations of the
correction-direction scope note: the 2025 Stem Cell Research study
correcting the low-penetrance albinism-associated TYR c.1205G>A variant
with CRISPR-Cas9 in a patient-derived iPSC line (human cells; the declared
correction direction, variant A to reference G on the forward strand, falls
in this catalog's classical ABE conversion class, though the source used
CRISPR-Cas9) and the 2021 Methods in Molecular Biology rice
cytidine-deaminase base-editing methods chapter for grain-size and
seed-coat-color trait loci (plant). Metadata was retrieved through
exact-EXT_ID Europe PMC queries and is bound by a records-hash
[receipt](data/pigmentation_metadata_receipt.json); full texts were not
accessed. Three outcome rows keep the TYR correction (dna_product),
multi-lineage differentiation capacity (molecular_function) and the rice
protocol presentation (dna_product) in separate domains, all as context,
with unknown denominators where the accessed abstracts do not state them.
Neither card supports appearance modification in a healthy adult; the
catalog is now eighteen source cards. The current outcome snapshot is
`examples/outcome-audit-pigmentation/report.json`; earlier snapshots
remain historical. All 34 unit tests and Ruff pass.
