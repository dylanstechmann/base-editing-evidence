# Correction-direction scope: cancer, aging and appearance traits

This note maps three frequently proposed base-editing goals — correcting
cancer-driver lesions, repairing aging, and changing hair, eye or skin color
in healthy adults — onto the evidence categories this repository audits. It
accompanies the `correction-class` CLI command, which classifies a declared
pathogenic-to-corrected direction against the classical ABE/CBE conversion
classes. Everything here is in-silico classification and catalog scope; no
guide design, editor selection, delivery route, dose, laboratory procedure or
clinical recommendation is provided. Unknowns remain unknown.

## The chemistry-direction question

Classical base editors convert specific transition directions: CBE performs
C•G→T•A (C→T, or G→A on the opposite strand) and ABE performs A•T→G•C (A→G,
or T→C on the opposite strand). A declared single-base correction is in
exactly one of three states:

| Declared correction | Classification | What it does not establish |
|---|---|---|
| C→T or G→A | Classical CBE direction | No targetable site, PAM context or editing window |
| A→G or T→C | Classical ABE direction | No efficiency, bystander or intended-only product |
| Any transversion (A↔T, A↔C, T↔G, C↔G) | Outside both classes | Broader-change machinery is a separate comparison, not designed here |
| Identical bases | No correction declared | No change exists to classify |

Nonsense-codon examples make the boundary concrete: CAG→TAG and CGA→TGA are
G→A and C→T corrections in the classical CBE direction, while AAA→TAA would
require an A→T transversion outside both classes. Indels are outside
single-base classification altogether. Direction membership never
establishes targetability, safety or recovered function.

## Cancer-driver lesions

Cancer is typically multi-lesional and heterogeneous within one tumor. A
classified correction direction for one driver allele is not a therapeutic
program: no card in this catalog establishes editing of a somatic tumor
lesion, tumor-selective delivery, clonal-response dynamics or durable safety
in a person. Two cancer-model cards now exist in this catalog: the 2026
inducible split-editor functional-genomics screens and the 2026 CAR-adapted
PIK3CD allelic-reprogramming study. Both use base editors as research tools
on tumor models or engineered immune cells; neither is a tumor-lesion
correction in a person. The repository's disease-correction precedents
(COL7A1/RDEB, KCNJ13, ABE8e-Y149V/HTI, CPS1) remain monogenic or
bypass-strategy models.

## Aging

The progeria card in this catalog is a monogenic laminopathy model; this
repository already records that it is not a model of the distributed, mosaic
age-acquired change of ordinary aging. No single-base correction direction
addresses "aging" as a whole, and no card here claims aging reversal in any
species. Treating progeria-model results as ordinary-aging evidence would be
the scope error this tooling is built to prevent.

## Appearance traits: hair, eye and skin color

Trait pigmentation is predominantly polygenic. Two review references,
verified through Europe PMC indexed metadata on 2026-10-24 with full texts
not reviewed here, describe that architecture:

- [Manga & Loftus, 2025, Ann Hum Genet — Genetics of Skin, Hair, and Eye Color in Human Pigmentation Disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC12233148/)
- [Bose et al., 2026, Front Genet — The genetic architecture of human skin pigmentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC13446898/)

Because common trait variation aggregates many loci of small effect, there
is no single "intended" edit whose product defines success, and allele
fractions measured in one cell population cannot be converted into trait
outcomes. Changing appearance in a healthy adult is enhancement, not
correction of a declared pathogenic lesion; no regulatory-approved
base-editing indication for appearance exists in this catalog's sources, and
none is proposed here. Germline editing for such purposes is broadly
prohibited, and this repository contains no germline or reproductive
program of any kind.

The claim that "much of the technology is ready" holds only at the level this
catalog documents: editor chemistry performs in cultured cells, engineered
tissue constructs and localized animal disease models (see
[EDITOR_PRECISION_FUNCTION_COMPARISON.md](EDITOR_PRECISION_FUNCTION_COMPARISON.md)).
Whole-body somatic delivery to arbitrary adult tissues, durable multi-year
safety data in healthy humans, and enhancement applications are not
established by any card in this repository.

## Where the catalog's evidence actually lives

| Stage | Cards in this catalog | Not established |
|---|---|---|
| Cultured human cells | CBE 2016, ABE 2017, RNA off-target 2019, prime editing 2019, CBE fidelity 2020, COL7A1 2022 | Tissue function in a person; whole-genome safety |
| Animal models | Progeria 2021, KCNJ13 2023, ABE8e-Y149V 2026, cancer BE screens 2026, CAR-T PIK3CD 2026 | Ordinary aging; human clinical validation; tumor-lesion correction in a person |
| Single human case | CPS1 2025 | Comparative safety, durability, enhancement |
| Plants | Zong 2017 CBE crops; Jin 2019 rice off-targets | Human editing; agronomic or ecological outcomes; long-term field behavior |

The cell-culture and animal work the proposal anticipates is exactly the
stage of most catalog evidence; the gap is between those stages and
healthy-adult human use, which no current card crosses.

## What this repository will and will not do

It classifies declared directions, audits explicit count denominators,
keeps source scope, signal roles and negative findings separate, and
leaves unknowns as `null`. It does not design guides, rank editors for a
person, estimate off-target or efficiency values, or provide protocol,
dose or self-treatment instructions. Anyone presenting this tooling as
readiness for human enhancement use is misreading the audit.