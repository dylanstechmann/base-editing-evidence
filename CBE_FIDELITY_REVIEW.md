# CBE fidelity source: off-target reduction, assays and denominators

This AI-assisted focused review used the actually retrieved primary
open-access (CC BY) [full
text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7335424/), retrieved via the
[Europe PMC fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7335424/fullTextXML)
and recorded in the [retrieval
receipt](data/cbe_fidelity_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's earlier
article-page access for this card. Supplementary figures were referenced in
the manuscript but not separately acquired.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Bacterial rifampin-resistance screen, Results and Fig. 1 | Untethered active APOBEC1 raised rifampin resistance 1,000-fold over the inactive E63A control and chloramphenicol resistance 10-fold; the APOBEC1–dCas9–UGI editor gave the same rifampin resistance with 250-fold higher chloramphenicol resistance; eA3A, YE1, YE2, EE, YEE, R33A and R33A+K34A variants matched the inactive-control background | A selection-based deamination propensity assay, not a mammalian mutation burden |
| HSV-TK bacterial counter-assay, Results and Fig. S4 | A second selectable gene with different cytosine contexts reproduced the rifampin trends, with a narrower dynamic range | Sequence-context effects on the main assay are small in this comparison |
| In vitro kinetics, Results | YE1–dCas9–UGI ssDNA kcat/Km 69-fold lower and APOBEC3A–dCas9–UGI 1.3-fold higher than APOBEC1–dCas9–UGI | Supports the source's catalytic-efficiency model for Cas9-independent deamination |
| Human-cell ssDNA deamination assay, Results | A3A-BE4 4.4-fold higher than BE4; YE1-BE4, YEE-BE4 and R33A+K34A-BE4 1.7-, 3.2- and 1.4-fold lower than BE4 at the twelve 5'-TC cytosines above background | A co-transfected oligonucleotide readout, not genomic DNA |
| Clonal whole-genome sequencing, Results and Fig. 3c,d | HEK293T cells treated with BE4, YE1-BE4 or a Cas9 D10A control; top ~25% GFP-positive cells sorted, single cells expanded 16 days to clones, ~77× depth, variants called by the intersection of three algorithms: BE4 produced significantly more C•G-to-T•A SNVs than the control (8.0×10⁻⁶ per bp, higher than the two previously reported values of 5×10⁻⁸ and 5.3×10⁻⁷); YE1 did not differ significantly from the nickase control | Clone counts per group are not stated in the accessed text; the sorting-and-cloning design maximizes detection sensitivity, so this rate is not directly comparable across studies |
| On-target tradeoff, Results and Fig. 3a,b | YE1-BE4 and R33A-BE4 balanced reduced off-target with robust on-target; YE2-BE4, EE-BE4, R33A+K34A-BE4 and YEE-BE4 had even lower off-target with a significant on-target decrease across six tested sites | The precision-efficiency tradeoff narrows which sites remain addressable; no variant is universally best |
| Expanded targeting scope, Results and Fig. 4 | YE1-NG, circularly permuted (CP1028) and AALN variants maintained minimized off-target in the study's assays; collectively they could in principle target ~65% of ClinVar pathogenic SNPs correctable by C•G-to-T•A edits versus 19% for the SpCas9-YE1 variant alone, covering ~80% of SNPs targetable by current-generation BE4max variants | A computed targeting-scope estimate, not measured accessibility at those sites |
| Other unwanted editing outcomes, Results | All engineered variants gave lower or comparable indels versus BE4 across tested sites; all seven named variants gave lower Cas9-dependent off-target editing at 20 GUIDE-seq-ranked sites; YE1, R33A, R33A+K34A and YEE showed decreased RNA off-target editing of three abundant transcripts | No detected increases in these other domains, not absence across all conditions |

All fold changes and rates above are source statistics, not values
recalculated here. The ABE comparator showed background-level resistance in
the bacterial assays in this study — a finding consistent with prior
whole-genome studies, not a general safety claim about every adenine base
editor (later-generation ABEs are addressed by the
[ABE8e review](ABE8E_Y149V_REVIEW.md)).

Lower measured off-target activity in these assays is not zero risk, and a
narrowed editing window changes which sites remain targetable. No editor
is selected or ranked here, and no guide or sequence design is provided.