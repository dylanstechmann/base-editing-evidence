# Methods and evidence scope

The five cases were selected as contrasting primary precedents: CBE chemistry,
ABE chemistry, an RNA adverse-outcome assay, prime editing and an original
single-patient base-editing report. This is a focused selection, not a systematic
review or a claim of the latest complete clinical evidence.

A subsequent sixth card adds the 2021 primary progeria-model study. The assistant
accessed its official indexed abstract and retrieved exact-DOI Europe PMC core
metadata through Regen Workbench. [The new receipt](data/progeria_metadata_receipt.json)
identifies that real retrieval. Its molecular, vascular and survival rows retain
animal scope. A subsequent [full-text review](PROGERIA_REVIEW.md) qualifies
the separate longevity and selected-necropsy cohort counts and adds structural
integration and adverse findings. Assay-specific genomic denominators and
endpoint hierarchy remain unresolved where stated. No delivery regimen or
editing design is supplied.

On 2026-10-09, the AI assistant accessed the primary publisher/PMC/PubMed
pages stated in each case and a bounded Europe PMC core metadata response
through Regen Workbench. The [metadata receipt](data/metadata_receipt.json)
identifies the actual retrieval and response SHA-256. Full source responses
and abstracts remain in ignored workbench literature/provenance storage; this
repository does not redistribute the source full texts. A metadata hash proves
which response was retrieved, not whether the case interpretation is correct.
The original NEJM page retrieval failed; its case is abstract-limited.

`change-class` applies a four-base lookup on the declared reference forward
strand. It labels complementary transitions with the same classical chemistry
class. It does not implement editor targeting or sequence optimization, and
does not evaluate mitochondrial or RNA editing platforms.

`correction-class` maps a declared pathogenic-to-corrected single-base
direction onto the same classical ABE/CBE conversion classes. Complementary
corrections share a direction; transversions are reported outside both
classes without selecting or designing alternative machinery; identical
bases declare no correction. Direction membership establishes no PAM,
window, bystander, efficiency, delivery or safety property.

On 2026-10-24 the [correction-direction scope note](CORRECTION_SCOPE.md)
cited two pigmentation-genetics reviews verified through Europe PMC indexed
metadata only (Manga & Loftus 2025, Ann Hum Genet; Bose et al. 2026,
Front Genet). The full texts were not reviewed, and no claims from their
contents are transcribed here.

`audit-coverage` demonstrates a declared nested count chain in the same target
cell population. Whole-population fractions share `target_cells`; conditional
fractions use the immediately preceding known stage. Counts are integers,
not read percentages or independently sampled marginal estimates. This formal
chain cannot be used where the source assays do not bind the same population.
Functional rescue remains an independent question. Only synthetic inputs are
accepted by this first CLI demonstration; the pure count audit is available
for future source-qualified intake work.

The tools validate schema and arithmetic, not source acquisition, causal variant
classification, cell-level assay truth or clinical benefit. No genomic coordinate
normalizer, ClinVar pathogenicity inference, off-target predictor, lineage
tracker or allele-to-cell deconvolution is implemented.

`audit-outcomes` binds declared observations to the validated study catalog,
retaining hashes of both inputs. Stage, model, source URL and access level come
from that catalog; observation records cannot override them. The original CPS1
abstract supports separate clinical-response and serious-adverse-event rows.
The RNA study supplies an assay-domain precedent, with independent replication
counts left unknown here. This tranche reuses those reviewed source scopes;
it makes no new claim of source acquisition or current clinical follow-up.

Endpoint hierarchy and comparisons are explicit declarations requiring human
source review. Unknown replication counts remain null. Missing or explicitly
not-assessed domains are catalog gaps, not zero effects, unperformed assays,
or failed biology. No benefit or safety score combines these different domains.

The optional `signal_role` is benefit, harm, context or unclear; omission remains
unclear. Reports index observation IDs by role and reported status without
combining them into a score. “No signal” on an adverse-event row cannot become
zero risk or a positive efficacy result. Survival is a separate eleventh domain,
and an animal survival row does not inherit human clinical validation.

Optional `cohort_counts` are declared disjoint groups of the same independent
unit, with positive integer counts summing to the known `n_independent_units`.
They are not numerator/denominator pairs, overlapping assays or repeated visits.
Validation checks declared arithmetic; it cannot authenticate independence.

On 2026-10-09, this catalog added four focused primary-source comparisons:
engineered CBE off-target assays, ABE8e correction in COL7A1/RDEB patient cells
and a 3D skin-equivalent model, KCNJ13 editing in patient-derived retinal cells
and a targeted mouse model, and the ABE8e-Y149V study spanning cell, embryo and
hereditary-tyrosinemia mouse assays. The assistant accessed the primary PMC or
JCI article pages online. Supplementary material was not independently
reviewed or retained in this repository, and source percentages/statistics were
transcribed rather than recalculated. The new
[comparison](EDITOR_PRECISION_FUNCTION_COMPARISON.md) and
[precision audit snapshot](examples/outcome-audit-precision/report.json)
preserve model and endpoint boundaries. Counts remain null where the
source-specific independent-unit denominator was not audited here; a read or
allele fraction is not converted into edited-cell coverage.

This is a small, question-driven sample, not a systematic review. The 2026
ABE8e-Y149V paper's mouse result edits Hpd to bypass the Fah-associated disease
pathway; it does not correct the causal Fah mutation. RDEB and KCNJ13 findings
remain disease-specific cell, engineered-tissue and animal-model evidence.
The progeria mouse model and the original one-patient CPS1 report remain
separate from ordinary-aging or rejuvenation evidence. No editor is ranked and
no clinical or molecular intervention is proposed.

On 2026-10-24, the catalog added a `plant` evidence stage with two
crop-plant cards: the 2017 rice/wheat/maize cytosine-base-editor study and
the 2019 rice whole-genome off-target study. The assistant accessed exact
EXT_ID Europe PMC REST responses online and transcribed indexed metadata;
raw response bytes were not retained by the retrieval tooling, so the
[receipt](data/plant_metadata_receipt.json) binds the committed record
block with a records SHA-256 rather than an unretained response. Full texts
and supplementary materials were not accessed, and abstract-level statements
are not extended beyond the accessed text. Plant on-target conversion and
genome-wide off-target findings remain separate outcome domains, and no
agronomic, ecological or human claim is derived.

On 2026-10-24, the catalog added two abstract-level cancer-model cards:
the 2026 inducible split base-editor functional-genomics study and the
2026 CAR-adapted PIK3CD allelic-reprogramming study. The assistant accessed
exact EXT_ID Europe PMC REST responses online and transcribed indexed
metadata; raw response bytes were not retained, so the
[receipt](data/cancer_metadata_receipt.json) binds the committed record
block with a records SHA-256. Full texts were not accessed, and
abstract-level statements are not extended. Both cards record base editors
used as research tools on tumor models or engineered immune cells; neither
supports a tumor-lesion-correction, dosing or clinical claim.

`audit-variant-batch` classifies declared single-base correction
directions for in-silico intake only. Each row must declare its origin as
`published_source` or `synthetic_example` with a source reference;
personal-genome rows and any targetability, guide, delivery, dose or
scope-override fields are rejected. Reports tally directions and change
types; no pathogenicity inference, efficiency or off-target estimate, and
no guide design is performed.

`verify-receipts` runs the structural provenance-receipt checks shared with
the test suite against given receipt files, defaulting to
`data/*receipt*.json`. It verifies declared HTTPS Europe PMC REST retrieval
URLs, 64-hex digests, ISO timestamps, record identifiers and records-hash
binding, and reports per-file pass or fail without re-retrieving anything.
It does not authenticate record-to-card binding or source truth. Declared
`published_source` batch rows now require an HTTPS, DOI or PMID
`source_reference`; free-text citations are rejected as not locatable.

On 2026-10-24, the catalog added two nonhuman-primate delivery and
durability cards: the 2021 Nature single-dose lipid-nanoparticle PCSK9
base-editing study in cynomolgus monkeys and the 2021 Nature Biotechnology
ABE study in mouse and macaque livers reporting editing magnitudes, rapid
mRNA clearance, no detected genomic-DNA off-target mutations in its
testing, and a re-dosing humoral immune observation. The assistant accessed
exact EXT_ID Europe PMC REST responses online and transcribed indexed
metadata; raw response bytes were not retained, so the
[receipt](data/delivery_metadata_receipt.json) binds the committed record
block with a records SHA-256. Full texts were not accessed. Editing
percentages and biomarker reductions are source statistics, not
recalculated here; nonhuman-primate liver delivery for one route and
disease context is not human validation or a dosing protocol.

On 2026-10-24, the catalog added a `human_cohort` evidence stage with two
abstract-level observational aging cards: the 2014 age-related clonal
hematopoiesis cohort study and the 2016 tissue-specific adult-stem-cell
mutation accumulation study. The assistant accessed exact EXT_ID Europe
PMC REST responses online and transcribed indexed metadata; raw response
bytes were not retained, so the [receipt](data/aging_metadata_receipt.json)
binds the committed record block with a records SHA-256. Full texts were
not accessed, and abstract-level statements are not extended. Hazard ratios
and prevalence percentages are source statistics, not recalculated here.
These cards describe distributed age-acquired damage; they provide no
editing intervention, targetable lesion list or rejuvenation claim.

On 2026-10-24, the catalog added two appearance-trait editing cards bound
by the same [pigmentation metadata receipt](data/pigmentation_metadata_receipt.json)
that now also binds the two pigmentation-genetics review citations of the
correction-direction scope note: the 2025 patient-derived TYR iPSC
correction study and the 2021 rice seed-coat-color cytidine base-editing
methods chapter. The assistant accessed exact EXT_ID Europe PMC REST
responses online and transcribed indexed metadata; raw response bytes were
not retained, so the receipt binds the committed record block with a
records SHA-256. Full texts were not accessed. The TYR source used
CRISPR-Cas9 rather than a base editor, and its abstract reports no editing
efficiency or pigment-phenotype outcome in a person. Neither card supports
appearance modification in a healthy adult.
