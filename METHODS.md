# Methods and evidence scope

The five cases were selected as contrasting primary precedents: CBE chemistry,
ABE chemistry, an RNA adverse-outcome assay, prime editing and an original
single-patient base-editing report. This is a focused selection, not a systematic
review or a claim of the latest complete clinical evidence.

A subsequent sixth card adds the 2021 primary progeria-model study. The assistant
accessed its official indexed abstract and retrieved exact-DOI Europe PMC core
metadata through Regen Workbench. [The new receipt](data/progeria_metadata_receipt.json)
identifies that real retrieval. Its molecular, vascular and survival rows retain
animal scope; independent-unit counts and endpoint hierarchy remain unaudited
in this abstract-limited catalog. No delivery regimen or editing design is supplied.

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
