# COL7A1/RDEB source: correction, safety readouts and denominators

This AI-assisted focused review used the actually retrieved primary
open-access (CC BY) [full
text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9666996/), retrieved via the
[Europe PMC fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666996/fullTextXML)
and recorded in the [retrieval
receipt](data/col7a1_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's earlier
abstract-and-article-page access for this card. Editor and guide dose
values are omitted per this catalog's charter; dose levels are described
qualitatively. Supplementary figures and materials were referenced in the
manuscript but not separately acquired.

The study edited primary fibroblasts from one person with recessive
dystrophic epidermolysis bullosa harboring the recurrent c.5047 C>T
(p.Arg1683Ter) nonsense mutation in exon 54 of COL7A1.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Bulk fibroblast allele correction, Results and Fig. 3a | NGS: 94.6% on-target correction in the bulk edited population; Sanger peak analysis (Fig. 2c) estimated near-complete reversal at c.5047 | One patient's cells; an allele/read fraction, not a corrected-cell fraction. The Sanger and NGS values differ in method and are both retained as source statistics |
| Dose dependence, Results and Fig. 4 | NGS: correction/bystander at c.5052 for the three tested editor-and-guide amounts: 94.2%/75.5%, 91.6%/49.2%, 45.9%/20.1%; ABE7.10 10.8% with bystander below 5% | Dose amounts omitted per charter. The Discussion cites 12.4% for ABE7.10 where the Results state 10.8% — an internal source difference retained unreconciled |
| RNA restoration and transcriptome, Results and Fig. 3c,d | Mutated uracil at c.5047 in COL7A1 transcripts: 0.5% after treatment versus 36% without; the source attributes the sub-50% untreated value to nonsense-mediated decay. RNA-seq: no significant transcriptome-wide A-to-I increase; 443 differentially expressed genes with no cancer- or metabolic-pathway discrepancies | Transcriptome-level observations in one patient's cells, not whole-transcriptome absence of RNA effects |
| Off-target DNA, Results and Fig. 3b | CRISPOR/CFD-ranked top ten predicted off-target loci; nine tested (six genes, three intergenic): 1% or fewer G•C reads at positions where A•T is expected; one locus untestable owing to primer design | Selected predicted loci, not genome-wide assessment; no detected off-target editing is not zero risk |
| Protein restoration, Results and western blots | Restored COL7A1 mRNA and C7 protein; the source states n = 1 biological replicate for the blots, with full blots in supplementary figures not acquired here | Single-replicate qualitative protein evidence |
| 3D skin equivalents, Results and Fig. 5 | Fibroblasts plus healthy control keratinocytes, 20-day maturation: C7 restored at the dermal–epidermal junction; C7 intensity (normalized to cell number) significantly increased versus untreated and not significantly different from wild-type HSEs; K14 control showed no untreated-versus-treated difference | The number of independent constructs per condition is not stated in the accessed text; construct quantification is not human wound-healing or skin-mechanics evidence |

All percentages above are source statistics, not values recalculated
here. The bystander edit at c.5052 was silent (asparagine-to-asparagine)
in the source's coding analysis. The source's own stated future work —
whole-genome sequencing and oncogene panel screening before clinical
translation — is retained as the source's plan, not a result.

This one-patient, cell-and-construct study establishes molecular
restoration in a culture model. It does not establish corrected-cell
fractions, genome-wide or long-term safety, wound healing in a person, or
any clinical outcome. No guide sequence, dose protocol or treatment
recommendation is provided here.