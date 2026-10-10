# Editor precision and recovered function

This is a focused comparison of four primary studies added on 2026-10-09,
read alongside the repository's single-patient CPS1 report and progeria mouse
review. It is not a systematic review or an editor-selection guide. Its purpose
is to show which experimental questions each paper answers and which remain
open.

| Evidence | Model and precision readouts | Function measured | What the result does not establish |
|---|---|---|---|
| [Doman et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7335424/) | Engineered CBEs were compared in bacterial screens, human-cell assays and WGS validation. Selected variants showed about 10–100-fold lower Cas9-independent DNA off-target editing and about 5–50-fold lower guide-dependent activity in the reported assays, while retaining roughly 50–90% of BE4max average on-target editing. | Molecular editing performance only. | No repaired tissue, organism-level function or clinical outcome. The ranges span different constructs and assays; they are not universal editor properties or a safety guarantee. |
| [Sheriff et al., 2022, COL7A1/RDEB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9666996/) | One patient's primary fibroblasts; the reported 94.6% is a bulk mutant-allele correction/read fraction. A three-dimensional human skin equivalent was matured for 20 days. Selected predicted DNA off-target sites and RNA outcomes were assessed. | Restored COL7A1 RNA and type VII collagen protein; collagen VII localized at the dermal–epidermal junction in the engineered construct. | The allele fraction is not the fraction of corrected cells. The construct does not measure wound healing or skin mechanics in a person, and selected off-target assays do not prove genome-wide or long-term safety. |
| [Kabra et al., 2023, KCNJ13/LCA16](https://www.jci.org/articles/view/171356) | Patient-derived cells, iPSC-derived retinal pigment epithelium (RPE), and a localized RPE-targeted mouse model. Mouse RPE editing was 9.5% ± 5.0% or 16.8% ± 7.9% in groups of four eyes. Some cell settings had detectable on-target bystanders or indels; selected off-target panels were tested. | Kir7.1 channel function in patient iPSC-RPE and retinal ERG c-wave recovery with preserved OCT structure in an engineered mouse model, followed through 10 weeks. | This is an inherited single-gene retinal-disease model, not a human vision result. RPE allele fractions are not edited-cell coverage. The paper notes unresolved per-cell allele combinations; limited off-target panels cannot rule out every unintended edit. |
| [Sun et al., 2026, ABE8e-Y149V](https://pmc.ncbi.nlm.nih.gov/articles/PMC13225742/) | A 102-target cell library, endogenous targets, four disease-associated sequences installed in HEK293T cells, embryo GOTI WGS, transcriptome assays and hereditary tyrosinemia type I (HTI) mice. ABE8e averaged 371 SNVs/embryo versus 13 in Cre controls in one GOTI comparison; Y149V narrowed the editing window and had markedly fewer off-target SNVs in the study's tests. At four disease-associated cell targets, its perfect-read fraction was higher than ABE8e, but those were engineered HEK293T cells. | Short-term liver and weight outcomes in HTI mice after editing **Hpd**, an upstream pathway gene. This bypassed the Fah defect; it did not repair the causal mutation. | Embryo WGS is not a human somatic-tissue mutation estimate. Engineered target segments are not patient cells. Selection of edited hepatocytes may influence liver allele fractions. Mouse disease rescue is not evidence of ordinary-aging benefit. |
| [Koblan et al., 2021, progeria](https://pmc.ncbi.nlm.nih.gov/articles/PMC7872200/) | In vivo ABE in a genetic-disease mouse model; the separate repository review records survival cohorts, vascular pathology, selected necropsies and vector-integration findings. | Vascular histopathology and survival in the mouse disease model. | Hutchinson-Gilford progeria is a causal monogenic syndrome, not a model of the many distributed changes in typical human aging. The source's selected tumor and integration findings do not establish a causal tumor risk. |
| [Musunuru et al., 2025, CPS1](https://pubmed.ncbi.nlm.nih.gov/40373211/) | One infant in an initial single-patient report, with seven weeks of reported follow-up. | Clinical protein tolerance and nitrogen-scavenger medication response. | One uncontrolled monogenic-disease case does not establish durability, comparative safety, organ-general delivery or rejuvenation. |

The studies cannot be ranked by one “precision” percentage. For a declared
target, useful evidence should keep at least these quantities separate:

1. Desired base conversion and the fraction of reads with the intended-only
   product.
2. Bystander substitutions and indels at the intended site.
3. Guide-dependent off-target DNA edits and guide-independent genome-wide DNA
   changes.
4. RNA changes, structural DNA outcomes and cell-level allele combinations.
5. The fraction and identity of target cells reached in the relevant tissue.
6. Recovered cell, organ or clinical function, plus durability and clonal
   behavior.

A cleaner product at a few tested loci does not establish tissue function;
recovered function in one disease model does not settle genome-wide risk or
durability. ABE8e-Y149V is a promising example of improving a particular
efficiency/precision tradeoff in the reported models, not a generally “best”
editor. A narrower editing window can reduce unwanted neighboring edits while
also changing which sequence contexts remain addressable. Delivery remains a
separate determinant of cell coverage.

For regenerative-medicine work, correcting a defined pathogenic variant could
help a disease-specific cell product or tissue construct. It does not by itself
create a bioidentical tooth, periodontal ligament or gum: lineage identity,
architecture, vascularization, mechanical integration and host function still
need their own evidence. The [ResearchDesk dental track](https://github.com/dylanstechmann/regen-workbench/tree/main/studies/dental-regeneration-2026-10-09)
keeps those requirements separate.

No guide, sequence-specific editor design, delivery protocol, clinical
intervention or rejuvenation claim is provided here.
