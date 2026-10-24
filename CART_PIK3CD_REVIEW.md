# CAR-adapted PIK3CD source: screen, potency and in-vivo denominators

This AI-assisted focused review used the actually retrieved primary
open-access [full
text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12948676/) (open access as
indexed by Europe PMC), retrieved via the [Europe PMC fullTextXML
endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12948676/fullTextXML)
and recorded in the [retrieval
receipt](data/cart_pik3cd_fulltext_receipt.json), which binds the retained
response bytes by `response_sha256`. It supersedes this catalog's earlier
abstract-only access for this card. Guide sequences, effector-to-target
ratios and cell-dose values are omitted per this catalog's charter.
Supplementary data were referenced in the manuscript but not separately
acquired.

| Outcome | Source comparison or denominator | Interpretation retained |
|---|---|---|
| Base-editing screen, Results and Fig. 1, Extended Data Fig. 1 | A 34-sgRNA library targeting the PIK3CD adaptor-binding domain, delivered with a CAR-coupled sgRNA vector; T cells of two healthy donors per CAR design (1928z and 19BBz) electroporated with adenine-base-editor mRNA and repetitively exposed to Nalm6 leukemia cells over 3 weeks, with edit abundances sequenced before and after; RASA2-loss control enriched as expected in 1928z, CD19-loss controls stable | A proliferative-competition screen in engineered cells; enrichment identifies context-favorable alleles, not variant potencies or clinical efficacy |
| Screen hits, Results | E81K most enriched over the 3-week assay in the BBz context; L32P most enriched after repetitive stimulations in the 28z context; editing of the substitutions typically around 30%; on-target specificity supported across donors by the source's analyses | Screen-level findings with CAR-construct-dependent directions |
| Signaling, Results and Extended Data Fig. 2 | E81K increased pAKT and downstream effector phosphorylation upon antigen exposure (basal activity similar), shown for n = 3-4 donors including T cells of four pretreated patients with cancer; exogenous p110δ cDNA overexpression impaired antitumor activity, contrasting the endogenous-edit effect | An activation-dependent signaling change, not constitutive activation |
| In-vitro potency, Results and Extended Data Figs. 2, 3 | Cytotoxicity assays with n = 9 donors (wild-type target) and n = 6 donors (antigen-low target); CD69 upregulation n = 5 donors; effector-memory enrichment n = 8 donors; expansion n = 16 donors; benefits reproduced in T cells of heavily pretreated patients with cancer (n = 4) | Explicit donor denominators; engineered-cell potency, not patient outcomes |
| Nalm6 leukemia model, Results and Fig. 2 | NSG mice with luciferase-expressing Nalm6: E81K-edited TRBC-knockout 19BBz n = 18, control n = 19, untransduced T cells n = 3; T cells from n = 4 unrelated healthy donors; significantly improved survival and long-term remissions (source Mantel–Cox test); a rechallenge experiment with n = 4 mice per group showed functional persistence | Explicit mouse-level denominators in an immunodeficient-xenograft model |
| Sh-Sy5y solid-tumor model, Results and Fig. 3 | B7H3-BBz CARs: E81K n = 11, control n = 11, untransduced n = 4 mice; T cells from two donors; improved survival | A second model with small per-group denominators |
| Safety analyses, Results and Extended Data Fig. 4 | Tumor-growth monitoring n = 12/13/3; 150-day body-weight follow-up n = 19 per group (T cells from n = 4 donors); 66-day necropsies, tissue T-cell counts and liver enzymes n = 4 per group; serum cytokines n = 5: no signs of lymphomagenesis or increased side effects, and no aberrant antigen-independent growth in long-term culture | Absence of detected signals in these assays and time windows, not zero risk; retained as stated |
| L32P in-vivo result, Results and Fig. 5 | B7H3-28z CARs in the neuroblastoma model: L32P n = 9, mock n = 9, untransduced n = 4 mice; T cells from two donors; improved survival with memory-formation benefits | The context-dependent, signaling-attenuating direction of the same screen |

All percentages, fold changes and test statistics above are source values,
not results recalculated here. The E81K edit deliberately installs an
activating signaling allele in engineered immune cells — it does not
correct a tumor-driver lesion, and the safety panels are selected assays
in xenografted mice rather than long-term human follow-up. No editor,
guide, dosing protocol or clinical recommendation is provided here.