# Foundational methods papers: chemistry, product profiles and denominators

This AI-assisted focused review used the actually retrieved primary
open-access full texts of the three foundational methods cards — the
original cytosine base editor
([PMC4873371](https://pmc.ncbi.nlm.nih.gov/articles/PMC4873371/)), the
original adenine base editor
([PMC5726555](https://pmc.ncbi.nlm.nih.gov/articles/PMC5726555/)) and the
prime-editing report
([PMC6907074](https://pmc.ncbi.nlm.nih.gov/articles/PMC6907074/)) — each
retrieved via the Europe PMC fullTextXML endpoint and recorded in
retrieval receipts ([CBE 2016](data/cbe2016_fulltext_receipt.json), [ABE
2017](data/abe2017_fulltext_receipt.json), [Prime
2019](data/prime2019_fulltext_receipt.json)) that bind the retained
bytes by `response_sha256`. These reviews supersede the cards' earlier
abstract-level access. Guide sequences and transfection/dose values are
omitted per charter; supplementary files were not separately acquired.

## Cytosine base editing (2016)

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Editor development | Four deaminases tested; the rAPOBEC1-dCas9 fusion, plus a uracil-glycosylase inhibitor (second generation) and a Cas9 nickase targeting the unedited strand (third generation) | Chemistry lineage; no guide design is provided here |
| On-target correction | Four transformed human and murine cell lines, with permanent correction of about 15-75% of total cellular DNA (abstract); in an APOE4-mimic astrocyte model, third-generation editing exceeded 50% with 4.6-6.1% indels, versus 0.1-0.3% correction and 26-40% indels for the Cas9-plus-donor comparison; in a TP53 Tyr163Cys cancer line, 3.3-7.6% correction with at most 0.7% indels versus below 0.1% correction and 6.1-8.0% indels | Cell-line disease-model corrections, not tissue repair or clinical outcomes |
| Product profile | Second-generation editors: typically below 0.1% indels; third-generation: typically at or below 1% | Product-profile choices with explicit tradeoffs |
| Off-target profile, Extended Data Fig. 7 | Non-target C-to-T and G-to-A rates at 2,500 distinct cytosines/guanines surrounding six on-target and 34 off-target loci (14,700,000 reads from about 1.8 million cells); no evident mutation increase within 50 bp of protospacer ends versus untreated controls | A selected-loci readout, not genome-wide sequencing; no-detected is not zero risk |

## Adenine base editing (2017)

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Evolution ladder, Results and Fig. 3 | Directed-evolution generations with six-locus average editing of 11±2.9%, then 14±2.4%, then 29±2.6% (best site 65±4.2%, worst 8.3±0.67%, with a stated YAC context preference); a later generation averaged 16±5.8%; seventh-generation editors reach about 50% in human cells with product purity typically at or above 99.9% and indels typically at or below 0.1% (abstract) | Mean±SD of three biological replicates, 5 days post-transfection without enrichment; values are target- and context-dependent |
| HDR comparison, Results | Against a Cas9-nuclease-mediated HDR method: ABE7.10 target-mutation frequencies of 10-35% after 48 hours and 55-68% after 120 hours, with a more-than-1,000-fold product-selectivity difference | An in-cell comparison with one then-current HDR method, not a general ranking |
| Off-target profile, Results and Fig. 5c | GUIDE-seq-defined top-12 Cas9 off-target loci for three guides: Cas9 nuclease modified 9 of 12 (average 14% indels); ABE7 variants showed at least 0.2% editing at only 4 of 12 (average 1.3%); no apparent editing outside on- or off-target protospacers; the source itself notes no comprehensive ABE off-target profiling method then existed | The comparison assumes ABE off-targets coincide with Cas9 off-targets — a source-stated assumption, retained |

## Prime editing (2019)

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| System and variants, Results | A Cas9 H840A nickase fused to a reverse transcriptase with a prime-editing guide RNA; an engineered reverse-transcriptase pentamutant (PE2) improved point-mutation efficiency 1.6- to 5.1-fold over PE1 (with a 6.8-fold intermediate step), and nicking the non-edited strand (PE3) improved editing further | A complementary search-and-replace approach, recorded separately from base editing |
| Scope, Results | More than 175 edits in human cells: all 12 point-mutation types plus targeted insertions and deletions, in four human cell lines and primary post-mitotic mouse cortical neurons with varying efficiencies | A cell-level capability survey, not a therapy |
| Disease-model corrections, Results | Corrections of the primary genetic causes of sickle cell disease (HBB transversion) and Tay-Sachs disease (HEXA deletion) and installation of a protective PRNP transversion in human cells, with higher or similar efficiency and fewer byproducts than HDR and complementary strengths versus base editing | In-cell disease-model edits; complementary rather than superior to base editing |
| Off-target profile, Results | Much lower off-target editing than Cas9 nuclease at known Cas9 off-target sites; the up-to-89%-correctable figure is an in-principle computed estimate | Known-site comparisons, not genome-wide profiling; the computed estimate is not measured accessibility |

All values above are source statistics, not results recalculated here.
These three papers establish editing chemistry and cell-level outcomes;
none establishes tissue repair, delivery, durability or clinical safety.
Prime editing remains recorded separately from base editing in this
catalog. No guide, sequence design, dose or protocol is provided here.