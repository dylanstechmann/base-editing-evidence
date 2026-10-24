# Macaque PCSK9 source: delivery, durability and denominators

This AI-assisted focused review used the actually retrieved primary
open-access (CC BY) [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8352781/),
retrieved via the [Europe PMC fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8352781/fullTextXML)
and recorded in the [retrieval
receipt](data/macaque_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's earlier
abstract-only access for this card. Dose-level values are omitted per this
catalog's charter; two ascending intravenous dose levels are described
qualitatively. Supplementary files were referenced in the manuscript but
not separately acquired or reanalyzed.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Macaque on-target liver editing, Results and Fig. 4f | 12 cynomolgus macaques, four groups of three (two dose levels, single or repeat); six biopsies per animal across four liver lobes at Day-29 necropsy; single-dose editing 2.03 ± 0.85% and 27.6 ± 5.87%, indels up to 0.27% | Allele-fraction editing in biopsies, not edited-cell coverage; dose-level groups are source-assigned, not randomized comparator arms |
| Repeat dosing, Results and Fig. 4f | Repeat dose at a 2-week interval: 3.31 ± 1.73% and 24.14 ± 1.52% after repeat dosing versus 2.03 ± 0.85% and 27.6 ± 5.87% after single dosing | Negative finding preserved: re-dosing did not increase editing in macaques |
| Humoral immune response, Results and Fig. 4i,j | Serum ELISA versus Day −1 baseline: SpCas9- and TadA-specific IgG detected at Day 29 in both repeat-dose groups; single-dose groups showed only minor, statistically nonsignificant increases | A detected macaque humoral response, not a human immunogenicity estimate or a dosing recommendation |
| Blood biomarkers, Results and Fig. 4g,h | High-dose groups versus baseline (Day −12 and Day −1): PCSK9 reduced 26% (single-dose group) and 39% (repeat-dose group), LDL reduced 9% and 19% | The accessed abstract states 32% and 14%; the full-text Results state per-group values. Both are retained as source statistics, not reconciled or recomputed here |
| Organ distribution, Results and Fig. 4k | Nine organs examined in high-dose animals: editing below 1% in eight; spleen 6.1 ± 2.7% (single) and 12.4 ± 7.8% (repeat) | Detected extrahepatic spleen editing is a biodistribution observation, not a toxicity endpoint; eight examined organs do not establish absence across all tissues |
| Mouse RNA off-targets, Results and Fig. 2c | Transcriptome-wide A-to-G transitions: about 44 (LNP) and 20 (AAV) on average in vivo versus more than 11,000 in transfected HEK293T cells; not detectable at Day 17; in vivo ABE expression 3–4 orders of magnitude lower | Dose- and expression-dependent source observations, not universal absence of RNA off-target deamination |
| Mouse genomic-DNA off-targets, Results and Fig. 3a–d | Whole-genome sequencing of ex vivo expanded hepatocyte clones: untreated n = 3, LNP-treated n = 6, AAV-treated n = 6; no increased A-to-G burden and no enriched TadA trinucleotide signature; CIRCLE-seq/CHANGE-seq top candidate sites not elevated | Selected clones and candidate sites, not whole-genome absence across all conditions |
| Tumor-sensitized mice, Results and Fig. 3e,f | Liver-specific Trp53-deleted mice with about 1 year of AAV ABE expression: no enhanced hepatocellular carcinoma formation | Sensitized-model context, not a general oncogenic-safety demonstration |
| Tolerability, Results and Figs. 1h–i, 4b–e | Macaques: transient transaminase and cytokine elevations resolved by 7 d and 24 h; Day-29 liver histology showed sporadic, very mild lobular mixed cell infiltration; no animal excluded. Mice: transient transaminase increase after LNP delivery, otherwise asymptomatic | Qualitative tolerability in 12 macaques, not human safety; no dose values are reproduced here |

The source reports specific statistical tests and P values in figure
legends; those are source statistics, not results recalculated here.

In mice, AAV-delivered (but not LNP-delivered) ABE induced detectable
anti-SpCas9 and anti-TadA antibodies in the source's ELISA (Fig. 1f) — a
retained contrast between sustained and transient editor expression.

The re-dosing and biomarker observations stay separate: an absent editing
increase after repeat dosing is not explained by, and does not exclude, the
detected IgG response; the source itself frames its T-cell speculation as a
hypothesis. The abstract-level and Results-level biomarker percentages
differ in aggregation and both remain source statistics. No delivery route,
dose or schedule is recommended by this review, and this single-organ
(liver), single-route precedent in 12 macaques establishes neither
whole-body adult delivery nor durable human safety.

The optional `cohort_counts` declarations on this study's outcome rows
record **disjoint groups of the same independent unit** (four dosing
groups of three macaques; the high-dose single- and repeat-dose groups for
the candidate-site and organ-panel rows). They check arithmetic, not
source truth or independence.