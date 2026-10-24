# ABE8e-Y149V source: off-target signals, variant screen and mouse rescue

This AI-assisted focused review used the actually retrieved primary
open-access [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13225742/)
(open access as indexed by Europe PMC), retrieved via the [Europe PMC
fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13225742/fullTextXML)
and recorded in the [retrieval
receipt](data/abe8e_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's earlier
article-page access for this card. Supplementary data were referenced in
the manuscript but not separately acquired. Guide sequences and dose
values are omitted per this catalog's charter.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| GOTI at the Tyr locus, Results and Fig. 2A–F | n ≥ 3 embryos per group, ~50× WGS, three variant callers, with the non-edited blastomere of the same embryo as reference: ABE8e averaged 371 SNVs per embryo (>28-fold over the 13-SNV Cre control); BE3 225; ABE7.10, ABE7.10F148A, ABEmax, miniABEmax, YE1-BE3-FNLS and Cas9 groups 12–21, not significantly different from control; ABE8e conversions were 94% A-to-G/T-to-C at TA contexts; no off-target site shared between ABE8e embryos and no overlap with predicted guide-dependent sites | An embryo assay with an embryo-internal reference; not a human somatic-tissue mutation estimate. The abstract's "~30-fold" rounds the Results' ">28-fold" — retained unreconciled |
| GOTI replication, Results and Fig. 2G–L | Three further guides: on-target 85.8% (Dmd), 73.6% (Fah), 91.3% (PCSK9); SNVs 279, 343 and 387 per embryo respectively, 21- to 30-fold over Cre controls; 91–95% A-to-G/T-to-C; no detected off-target cytosine deamination | Replicates the guide-independent signal across targets |
| Saturation-mutagenesis screen, Results and Fig. 3 | 152 single-residue and 6 double-residue variants at eight TadA8e sites, screened in the 102-sgRNA HEK293T library; Y149V: 42.4% average A5 efficiency, window A3–A7, lowest bystander and C editing; S109F 42.3%; D147K 53.1% with a still-broad window (A2–A9) | Screen-level performance in engineered cells; window narrowing is a tradeoff, not a universal improvement |
| Endogenous loci, Results and Fig. 4 | 15 endogenous sites: Y149V 63.7% (A5) and 68.3% (A6), comparable to ABE8e (61.6%, 69.2%), with a narrower window (A4–A8 vs typically A3–A10); at 14 Cas-OFFinder-predicted sites for two guides, Y149V maximum off-target ≤1.3% versus ABE8e 6.3% | Engineered HEK293T targets, not patient cells |
| GOTI variant comparison, Results and Fig. 5A–C | PCSK9 guide: Y149V 24 SNVs per embryo; ABE8eV82G 296, ABE8eK20A/R21A 175, ABE8eV106W 110, ABE9 37; all variants >80% on-target except ABE9; a further Tyr GOTI showed Y149V at Cre-control background | Relative ordering among these tested variants in this assay |
| Transcriptome-wide RNA SNVs, Results and Fig. 5D–F | ABE8e 8,795 average RNA SNVs versus 1,463 in vector controls; ABE8eV82G 12,894; ABE8eK20A/R21A 4,790; ABE8eV106W 2,444; Y149V and ABE9 showed no significant increase, with no UA-motif enrichment, confirmed at two additional on-target sites | A cell-culture transcriptome assay; no significant increase is not absence of RNA editing |
| Disease-locus precision, Results and Fig. 7 | HBG1/HBG2 promoters: Y149V perfect-read fractions 5.3-fold and 8.1-fold higher than ABE8e; four pathogenic SNPs integrated as 158-bp segments: perfect reads POLG 77.7% vs 39.8%, SCN1A 26.7% vs 4.7%, MYH7 74.4% vs 62.5%, COL7A1 78.1% vs 67.9% | Integrated segments, not patient loci; perfect-read fractions are sequence-product metrics |
| HTI initial cohort, Results and Fig. S9 | Dual AAV8 split-intein delivery into Fah-deficient mice kept on disease-suppressing medication for 2 weeks: Y149V 35.8% versus ABE8e 35.5% average on-target, with markedly lower bystander, C and indel outcomes for Y149V | Comparable initial editing efficiency before any selection |
| HTI withdrawal cohort, Results and Fig. 8 | After medication withdrawal, saline-injected control mice lost an average 20% body weight by day 32 and were euthanized; Y149V-treated mice were phenotypically indistinguishable from wild type with normal weight gain; day-30 liver Hpd A6 editing averaged 69.0% with negligible bystander or indel outcomes; HPD-negative hepatocyte patches; AST, ALT and bilirubin restored to levels comparable to wild-type and medicated references | Mouse counts per group are not stated in the accessed text. Editing an upstream pathway gene bypasses the metabolic defect — it does not repair the causal Fah mutation — and post-selection liver allele fractions do not equal initial cell coverage |

All values above are source statistics; none were recalculated here. The
observed ABE8e embryo SNV signal is itself a harm-domain finding this
catalog preserves; Y149V's lower counts in the same assays are comparative
results in those conditions, not a general safety demonstration. This
mouse metabolic-disease rescue is not ordinary-aging repair, and no
editor choice, guide design or dosing protocol is provided here.