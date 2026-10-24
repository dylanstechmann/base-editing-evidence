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

## Receipt-integrity CLI and published-reference validation — 2026-10-24

Moved the structural provenance-receipt checks into
`src/baseevidence/receipts.py`, shared by the CLI and the tests, and added
`baseevidence verify-receipts`, which validates given receipt files
(default `data/*receipt*.json`) and reports per-file pass or fail with a
nonzero exit on failures, without re-retrieving anything. Declared
`published_source` variant-batch rows now require an HTTPS URL, DOI or
PMID `source_reference`; free text is rejected as not a locatable citation.
Tests cover malformed-receipt rejection, failure reporting and the CLI exit
behavior. All unit tests and Ruff pass.

## Nonhuman-primate delivery and durability cards — 2026-10-24

Added two abstract-level nonhuman-primate cards covering the last
undocumented outcome domains (delivery and durability): the 2021 Nature
single-dose lipid-nanoparticle PCSK9 base-editing study in cynomolgus
monkeys (near-complete liver PCSK9 knockdown after one infusion; blood
PCSK9 about 90% and LDL about 60% reductions stable for at least eight
months) and the 2021 Nature Biotechnology ABE study in mouse and macaque
livers (up to 67% and 34% liver editing; plasma PCSK9/LDL reduced 95%/58%
in mice and 32%/14% in macaques; rapid mRNA clearance; no off-target
mutations found in the source's genomic-DNA testing; re-dosing did not
increase editing, possibly owing to a detected humoral immune response).
Metadata was retrieved through exact-EXT_ID Europe PMC queries and is
bound by a records-hash [receipt](data/delivery_metadata_receipt.json);
full texts were not accessed. Five outcome rows keep single-dose
delivery, eight-month biomarker stability, editing magnitude, the
no-detected-off-target statement and the re-dosing observation in
separate domains. These are one-organ, one-route nonhuman results, not
whole-body adult delivery, human safety or a dosing protocol. The current
outcome snapshot is `examples/outcome-audit-delivery/report.json`; earlier
snapshots remain historical. All unit tests and Ruff pass.

## First-in-human PCSK9 base-editing trial cards — 2026-10-24

Added the first two `human_trial` stage cards: the 2026 New England
Journal of Medicine phase 1 report of VERVE-102 (single ascending-dose
lipid-nanoparticle adenine base editing of PCSK9 in 35 adults with
heterozygous familial hypercholesterolemia or premature coronary artery
disease; no dose-limiting toxic effects; mild-to-moderate
infusion-related reactions, transient alanine-aminotransferase
elevations and one aspiration-pneumonitis event; dose-dependent mean
PCSK9 reductions from 51% to 88% and LDL cholesterol reductions from 9%
to 62%, with an absolute 78 mg per deciliter LDL reduction in the
highest-dose cohort; sustained through follow-up reaching at least one
year in 15 participants) and the 2026 Nature Medicine interim phase 1
report of YOLT-101 (6 adults; no grade 3 or higher adverse events;
transient self-limited infusion reactions and liver-enzyme elevations
most common; sustained PCSK9 and LDL cholesterol reductions of 74.4%
and 52.3% at 24 weeks in the highest-dose cohort of 3). Five outcome
rows separate biomarker reductions, one-year durability and each trial's
adverse-event reporting into distinct domains, with explicit participant
denominators where the abstracts state them. Dose-level values are
omitted to avoid reproducing a dosing protocol. Open-label phase 1
biomarker and interim safety data in patients do not establish
cardiovascular outcomes, multi-year safety, healthy-adult use or
whole-body delivery. Metadata and abstract text were retrieved through
exact-EXT_ID Europe PMC queries and bound by a records-hash
[receipt](data/human_trials_metadata_receipt.json); full texts were
not accessed. The current outcome snapshot is
`examples/outcome-audit-trials/report.json`; earlier snapshots remain
historical. All 37 unit tests and Ruff pass.

## Ex vivo HBG1/HBG2 sickle-cell trial card — 2026-10-24

Added the first ex vivo `human_trial` card: the 2026 New England Journal
of Medicine phase 1-2 BEACON report of ristoglogene autogetemcel
(autologous CD34+ hematopoietic stem and progenitor cells base-edited at
the HBG1/HBG2 promoters to inhibit BCL11A binding) in 31 patients 12 to
35 years of age with sickle cell disease and at least four severe
vaso-occlusive crises in the previous two years. Five outcome rows keep
on-target edited alleles (67.4% mean at 6 months among 13 patients), the
hemoglobin switch (fetal hemoglobin above 60%, sickle hemoglobin below
40% of total hemoglobin), engraftment kinetics (neutrophils median 17.5
days, platelets 19 days), the absence of investigator-reported severe
crises after 60 days post-transfusion, and adverse-event reporting (all
31 with events, 87% grade 3 or higher, 39% serious, one death from
idiopathic pneumonia syndrome) in separate domains with explicit
denominators. Cell-dose values are omitted to avoid a dosing protocol.
Metadata and abstract text were retrieved through an exact-EXT_ID Europe
PMC query and bound by a records-hash
[receipt](data/beacon_metadata_receipt.json); the subscription full text
was not accessed. An unplanned open-label interim analysis with mean
6.6-month follow-up is not a 12-month primary-end-point, curative or
long-term-safety demonstration. The current outcome snapshot is
`examples/outcome-audit-beacon/report.json`; earlier snapshots remain
historical. All 37 unit tests and Ruff pass.

## Receipt tooling release — 2026-10-24 (v0.3.0)

Added the `baseevidence fetch-receipt` subcommand: a live exact-EXT_ID Europe
PMC core-metadata retrieval that retains the raw response bytes under
`data/raw/`, binds them with `response_sha256`, transcribes the indexed record
fields into `records`, and binds that block with `records_sha256`.
`verify-receipts` now also re-checks retained response bytes by local hash; it
still never re-retrieves or authenticates, and the ten pre-existing
records-hash receipts pass unchanged. Receipts and retained responses are
append-only — the tool refuses to overwrite an existing receipt or response.
Validated by a live re-retrieval of PMID 41931046 on 2026-10-24, committed as
[data/beacon_response_receipt.json](data/beacon_response_receipt.json) with
the response retained at `data/raw/41931046.json`. Tests are mocked and never
touch the network; the suite is now 41 unit tests, Ruff clean, 11 receipts
verified with no failures.

## Macaque delivery/durability full-text review — 2026-10-24

Upgraded the pcsk9-macaques-2021 card from abstract-level access to a
reviewed primary open-access full text (CC BY), retrieved live via the
Europe PMC fullTextXML endpoint with the raw JATS bytes retained under
`data/raw/` and bound by `response_sha256` in a new full-text receipt that
`verify-receipts` re-checks locally (12 receipts now, all passing). The
[review](MACAQUE_REVIEW.md) retains the source's per-animal denominators
(12 macaques in four groups of three; six liver biopsies per animal), the
absent editing increase after repeat dosing, the detected SpCas9/TadA IgG
in repeat-dose groups, spleen editing of 6.1-12.4% with below-1% editing
in eight other examined organs, the mouse clonal whole-genome and
tumor-sensitized observations, and the abstract-versus-Results biomarker
aggregation difference — all as source statistics, without reconciliation
and without dose values. The macaque outcome rows gained explicit
`n_independent_units` and disjoint `cohort_counts`, plus a new
organ-distribution observation row. A read-only accessibility probe of all
23 cards also closed the NEJM re-review tranche: both NEJM records are
present in Europe PMC but non-open, and live fullTextXML requests return
HTTP 500, so those full texts are not accessible to this catalog's
tooling. This tranche rotates the current outcome snapshot to
`examples/outcome-audit-macaque-review/report.json`; earlier snapshots
stay historical. All 41 unit tests and Ruff pass.

## RDEB and retina full-text reviews — 2026-10-24

Upgraded two more cards from article-page or abstract access to reviewed
open-access full texts: col7a1-rdeb-2022 and kcnj13-retina-2023, each
retrieved live via the Europe PMC fullTextXML endpoint with raw JATS bytes
retained under `data/raw/` and bound by `response_sha256` in new receipts
that `verify-receipts` re-checks locally (14 receipts, all passing). The
[RDEB review](COL7A1_REVIEW.md) retains the Sanger-versus-NGS method
difference around the 94.6% allele correction, the source's n = 1 western
blot statement, the nine-of-ten predicted off-target loci actually tested,
the 0.5%-versus-36% transcript numbers and the Discussion-versus-Results
ABE7.10 percentage difference. The [retina review](KCNJ13_REVIEW.md)
retains the 13-cell patch-clamp denominator with its 5/4/4 split, the four
eyes per delivery amount, the 5-of-6 founder and homozygous-lethality
model facts, the week-2-versus-week-10 ERG values with their source P
values, the detected intergenic off-target change and the
abstract-versus-Results 47%/52.3% fibroblast difference — all unreconciled
source statistics. Two new outcome rows were added (COL7A1 RNA outcomes
and the 13-cell iPSC-RPE channel rescue) and four rows gained stated
denominators or full-text locators; dose amounts and guide sequences are
omitted per charter. This tranche rotates the current outcome snapshot
to `examples/outcome-audit-rdeb-retina/report.json`; earlier snapshots
stay historical. All 41 unit tests and Ruff pass.

## CBE fidelity and ABE8e-Y149V full-text reviews — 2026-10-24

Upgraded two more cards to reviewed open-access full texts:
cbe-fidelity-2020 (10.1038/s41587-020-0414-6) and abe8e-y149v-2026
(10.1093/procel/pwag006), each retrieved live via the Europe PMC fullTextXML
endpoint with raw JATS bytes retained under `data/raw/` and bound by
`response_sha256` in new receipts (16 receipts, all passing). The [CBE
fidelity review](CBE_FIDELITY_REVIEW.md) retains the multi-assay structure
(rifampin and HSV-TK bacterial screens, in-vitro kinetics with a 69-fold
ssDNA kcat/Km difference, the 1.7- to 4.4-fold ssDNA-assay comparisons and
the clonal WGS design with its 8.0×10⁻⁶-per-bp BE4 rate and
clone counts not stated), the on-target tradeoff across six sites and the
computed 65%-of-ClinVar scope estimate. The [ABE8e-Y149V
review](ABE8E_Y149V_REVIEW.md) retains the GOTI denominators (n ≥ 3
embryos per group, 371-versus-13 SNVs with the abstract's ~30-fold rounding
preserved unreconciled), the 152-variant screen, the Y149V 24-SNV GOTI and
8,795-versus-1,463 RNA-SNV comparisons, the disease-locus perfect-read
fractions, and the HTI cohorts including the 20%-weight-loss saline control
endpoint with unstated animal counts. Three new outcome rows were added
(clonal WGS validation, Y149V GOTI background, ABE8e RNA off-target signal)
and three rows gained full-text locators; no editor is ranked or selected.
This tranche rotates the current outcome snapshot to
`examples/outcome-audit-fidelity-abe8e/report.json`; earlier snapshots stay
historical. All 41 unit tests and Ruff pass.

## CAR-adapted PIK3CD full-text review — 2026-10-24

Upgraded the car-t-pik3cd-2026 card from abstract-only access to a
reviewed open-access full text (10.1038/s43018-025-01099-7), retrieved
live via the Europe PMC fullTextXML endpoint with raw JATS bytes
retained under `data/raw/` and bound by `response_sha256` in a new
receipt (17 receipts, all passing). The [review](CART_PIK3CD_REVIEW.md)
retains the 34-sgRNA screen design on T cells of two donors per CAR
design, the explicit xenograft group sizes (Nalm6 18/19/3 from four
donors; Sh-Sy5y 11/11/4; B7H3-28z 9/9/4), the TRBC co-knockout, the
safety panels (150-day weight n = 19 per group, 66-day necropsies n = 4,
liver enzymes n = 4, cytokines n = 5) with no-detected-signal framing,
and the opposite-direction L32P result — all as unreconciled source
statistics without guide sequences, effector-to-target ratios or cell
doses. Two new outcome rows were added (Nalm6 survival with disjoint
cohort counts summing to 40 mice, and the safety panels as a
no-detected-signal row) and the aggregate row gained explicit
denominators. This tranche rotates the current outcome snapshot to
`examples/outcome-audit-cart-pik3cd/report.json`; earlier snapshots stay
historical. All 41 unit tests and Ruff pass.

## Foundational methods papers full-text review — 2026-10-24

Completed the open-access review tranche by upgrading the three
foundational methods cards (cbe-2016, abe-2017, prime-2019) to reviewed
open-access full texts, retrieved live via the Europe PMC fullTextXML
endpoint with raw JATS bytes retained under `data/raw/` and bound by
`response_sha256` in three new receipts (20 receipts, all passing; the
cbe-2016 record is the PMC author manuscript and its receipt says so).
The [combined review](FOUNDATIONAL_METHODS_REVIEW.md) retains the 2016
paper's 15-75% correction range across four transformed cell lines with
its indel tradeoffs and its 2,500-cytosine/guanine off-target readout
(14.7 million reads, 40 loci), the 2017 paper's evolution ladder with
mean±SD of three biological replicates, its YAC context preference
and its assumption-dependent GUIDE-seq-anchored off-target comparison
(9 of 12 loci modified by Cas9 versus 4 of 12 by ABE variants at lower
levels), and the 2019 paper's more-than-175-edit survey, 1.6- to
5.1-fold PE2 improvements and known-site off-target comparisons. Each
card gained its first outcome row (dna_product) with explicit
honest limits; prime editing stays recorded separately from base
editing. This tranche rotates the current outcome snapshot to
`examples/outcome-audit-methods-papers/report.json`; earlier snapshots
stay historical. All 41 unit tests and Ruff pass.
