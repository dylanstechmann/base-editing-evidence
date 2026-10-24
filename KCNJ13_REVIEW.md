# KCNJ13/LCA16 source: channel rescue, retinal function and denominators

This AI-assisted focused review used the actually retrieved primary
open-access [full text](https://www.jci.org/articles/view/171356) (CC BY
as indexed by Europe PMC), retrieved via the [Europe PMC fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10541187/fullTextXML)
and recorded in the [retrieval
receipt](data/kcnj13_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's
earlier article-page access for this card. Guide sequences and delivery
dose values are omitted per this catalog's charter; the two tested
subretinal delivery amounts are described qualitatively. Supplemental data
were referenced in the manuscript but not separately acquired.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| HEK engineered line, Results and Fig. 1D,E | ABE8e mRNA 53.0% ± 1.4% versus ribonucleoprotein 31.4% ± 3.4% correction of the GFP-tagged W53X construct; indels 4.2% ± 1.6% (mRNA) versus 1.0% ± 0.4% (RNP) | An engineered overexpression line, not patient cells or endogenous loci |
| HEK automated patch clamp, Results and Fig. 2 | Restored Kir7.1 currents in 80% of edited cells (n = 60); 20% (n = 15) mutant-like; wild-type reference current –45.0 ± 11.3 pA (n = 62); untreated mutant –9.7 ± 1.3 pA (n = 40) | Explicit cell-level functional denominators within an engineered model |
| Patient fibroblasts (nanocapsule delivery), Results and Fig. 3 | Endogenous W53X site correction 52.3% ± 0.1% (Results) versus "47%" in the accessed abstract; bystanders rare (0.3%, 0.1%, 0.3% and 0.1% at the four stated positions); indels 2.7% ± 0.4%; unwanted substitutions 6.5% ± 1.4% (treated) versus 2.6% ± 0.1% (untreated); ABE7.10max 14.9% ± 1.7% | Abstract and Results values differ; both are retained as source statistics without reconciliation. Bystanders included silent and missense changes at low frequency |
| Patient iPSC-RPE editing, Results and Fig. 4B,C | 17.8% ± 1.5% editing of the mutant nucleotide; indels 0.7% (treated) versus 0.01% (untreated); bystander substitutions 2.9% ± 0.4% versus 1.8% ± 0.1% | A patient-cell allele fraction, not a corrected-cell fraction |
| Patient iPSC-RPE manual patch clamp, Results and Fig. 4D,E | 13 clamped cells from the edited pool: 5 of 13 showed rescued Kir7.1 currents, 4 of 13 showed no recovery (mutant-like), 4 of 13 showed intermediate responses | An explicit small-cell-count functional denominator. The source's per-cell genotype explanations are hypotheses; allele combinations per cell were not resolved |
| Knockin mouse generation, Results and Fig. 5 | 5 of 6 sequenced newborn mice carried the alteration on one allele; homozygous W53X/W53X animals were lethal on postnatal day 1; heterozygote ERG c-wave 455.9 ± 18.7 μV versus wild-type 504.5 ± 33.4 μV (P = 0.54, not significant) | A species difference the source itself notes: at least one normal Kcnj13 allele is required for murine survival |
| LCA16 model establishment, Results | The wild-type allele was disrupted in RPE by subretinal Cas9 delivery: c-wave amplitude 515.5 ± 9.5 μV before to 234.2 ± 14.9 μV at 6 weeks (P = 0.001), a 54% decrease | An engineered disease model, not human LCA16 |
| In vivo editing, Results and Fig. 6C–E | Two tested subretinal delivery amounts: 16.8% ± 7.9% and 9.5% ± 5.0% RPE editing, n = 4 eyes per amount; no other A>G substitutions reported at or around the protospacer; indels not significantly increased over placebo-treated mice | Dose amounts omitted per charter. Four eyes per amount; whether eyes cluster within animals is not stated in the accessed text |
| Mouse fibroblasts (heterozygous), Results | 14.5% increase in wild-type reads, which the source infers to mean about 29% of cells received an edit | A source-stated inference from allele reads to a cell fraction; kept distinct from measured cell counts |
| ERG rescue follow-up, Results and Fig. 6F–K | Full-field ERG at weeks 2, 6 and 10; week 2 normalized c-wave 0.8 ± 0.1 (nontargeting-guide control) versus 0.9 ± 0.2 (targeted), P = 0.9, indistinguishable; week 10 0.7 ± 0.1 versus 1.6 ± 0.1, P = 0.01, an about-55% amplitude increase; OCT structure intact; multifocal ERG waveforms localized near injection sites | Group sizes per ERG condition are not stated in the accessed text. Localized delivery with localized recovery, not whole-retina coverage |
| Off-target analysis, Results | Cas-OFFinder enumeration: 2,727 potential sites (most with 4 mismatches and a bulge: 2,004 RNA-bulge and 512 DNA-bulge configurations); none with 2 or fewer mismatches and no bulge; 9 candidate sites deep-sequenced in edited cells: no significant off-target except one intergenic locus (about 4-fold substitutions; rs139941105, minor allele frequency 0.01) | Computational enumeration plus selected-site testing, not genome-wide absence; a detected intergenic change is retained, not omitted |
| Nanocapsule immunogenicity probe, Results | CD8 and Iba1 expression increased in virally transduced RPE cells but not in nanocapsule-exposed cells (qPCR screen) | An in vitro cytokine screen, not an in vivo or human immunogenicity estimate |

All values above are source statistics; none were recalculated here. The
control condition in the functional follow-up was the same editor
delivered with a nontargeting guide.

This study establishes cell- and organ-level functional rescue in patient
iPSC-RPE and an engineered localized mouse model. It does not establish
human vision outcomes, whole-retina editing coverage, resolved per-cell
allele combinations, genome-wide safety or any clinical result. No guide
sequence, delivery protocol or treatment recommendation is provided here.