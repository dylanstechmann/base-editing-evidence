# Methods and evidence scope

The five cases were selected as contrasting primary precedents: CBE chemistry,
ABE chemistry, an RNA adverse-outcome assay, prime editing and an original
single-patient base-editing report. This is a focused selection, not a systematic
review or a claim of the latest complete clinical evidence.

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
