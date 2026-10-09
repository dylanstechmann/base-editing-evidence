# Progeria source: benefit, adverse findings and denominators

This AI-assisted focused review used the actually retrieved [primary full
text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7872200/), identified in the
[retrieval receipt](data/progeria_fulltext_receipt.json). It supersedes this
catalog's earlier abstract-only access. Supplementary tables and datasets were
referenced in the manuscript but not separately acquired or reanalyzed.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Earlier-start longevity cohort, Fig. 4d | 11 treated and 12 saline mice; median 337 vs 189 days | Genetic-disease mouse survival, separate cohort |
| Later-start longevity cohort, Fig. 4e | 10 treated and 12 saline mice; median 510 vs 215 days | One treated mouse remained alive at the source report; censoring retained |
| Aortic pathology, Fig. 4a–c | Six-month histopathology and nuclei counts; wild-type reference also shown | Morphology is distinct from measured hemodynamic performance |
| Later-start treated necropsies, Results | Five liver tumors among nine deceased examined mice; one gastrointestinal necrosis, three without apparent abnormalities | Selected postmortem denominator; not cumulative incidence or causal editor-specific risk |
| Vector integration, Results | Selected treated liver/tumor tissues vs saline liver | Structural finding; causal contribution to tumors unresolved |
| Liver mutation composition, Extended Data Fig. 12 | No significant difference in the relative fraction of detected A•T-to-G•C mutations | Not equivalence, absence of every mutation, or exclusion of vector integration/RNA effects |

The source reports Mantel–Cox p<0.0001 for each survival comparison. Those are
source statistics, not results recalculated here. Median ratios are not hazard
ratios. Different treatment-start cohorts also differ in exposure context, so
they do not isolate a timing effect. No biological delivery instructions are
derived from them.

The manuscript's liver sequencing Results describe three tumor-bearing treated
mice and two saline mice; one variant-analysis Methods comparison mentions four
independent mice. This review leaves analysis-specific replication unknown
rather than converting tissue-section counts into animals. The survival and
selected-necropsy denominators are independently explicit and remain separate.

Possible contributions discussed by the source include vector integration,
the model's human RAB25 transgene, residual disease and attained age. A detected
integration finding and a negative relative-mutation-composition test cannot
resolve those alternatives. Similarly, increased organ allele correction over
time could reflect continuing editing or survival/selection of corrected
cells; it does not independently establish whole-organ intended-only cell
coverage.

This genetic-disease rescue precedent does not estimate human lifespan,
ordinary-aging reversal or dental regeneration. It does show why molecular,
vascular, survival, structural-DNA and adverse-event rows need their own
comparators, time intervals and denominators.

The optional `cohort_counts` declaration records **disjoint groups of the same
independent unit**. Positive integers must sum to the row's known
`n_independent_units`. This checks arithmetic, not source truth or independence.
Do not use it for overlapping tissue samples, repeated visits, or one numerator
and its enclosing denominator. It supplies no automatic risk estimate.
