# Base Editing Evidence

Inspect the gap between changing a DNA base and restoring tissue function.
This is a personal hobby and learning project, developed with substantial AI
coding assistance. No owner laboratory work or source review is implied.

The tools provide an executable evidence-scope audit, a classical
nucleotide-conversion classifier and a cell-count denominator audit. The
[six source cards](data/studies.json) distinguish cell experiments, a genetic-disease
mouse model and an initial single-patient clinical report. It is a starting point for research on
somatic genome repair, stem-cell constructs and regenerative tissues.

## Three questions that stay separate

1. **What sequence change is required?** Classical ABE and CBE chemistry covers
   different transition classes, including their complementary-strand changes.
   This classification does not inspect a sequence, PAM, editing window,
   bystanders or chromatin. [CBE](https://www.nature.com/articles/nature17946),
   [ABE](https://www.nature.com/articles/nature24644).
2. **How many intended cells have an intended-only product?** Conditional editing
   among reached cells differs from coverage of the entire target population.
   Read and allele fractions cannot be silently converted into cell fractions.
3. **Did useful function recover, and persist?** DNA, RNA and structural editing
   outcomes, tissue function and clone behavior require separate observations.
   Cell-line RNA off-target findings illustrate why a DNA-only measurement has
   limited scope. [Primary RNA study](https://www.nature.com/articles/s41586-019-1161-z).

The synthetic count example reaches 500 of 1,000 cells, records intended edits
in 300, and intended-only products in 250. The conditional intended-edit rate
is 60%; intended-only coverage of the whole population is 25%. These are
constructed counts, not a predicted efficiency or threshold for benefit.

## Run

Python 3.11+, standard library only for the research tools:

```sh
python -m pip install -e .
baseevidence change-class A G --coordinate-system reference_forward_strand
baseevidence audit-studies data/studies.json --out artifacts/source-audit
baseevidence audit-coverage examples/coverage.json --out artifacts/count-demo
baseevidence audit-outcomes data/outcomes.json --studies data/studies.json --out artifacts/outcome-audit
PYTHONPATH=src python -m unittest discover -s tests -v
```

Each output directory must be new. Reports retain the exact input-byte SHA-256.
Duplicate JSON keys, inappropriate denominators, non-nested counts, ambiguous
bases and unstated coordinate conventions fail. Unknown stages remain `null`;
an undefined zero-denominator conditional rate is not reported as zero.

The [outcome inventory](data/outcomes.json) links each observation to an existing
source card and retains comparator design, endpoint hierarchy, independent unit,
follow-up and access scope. Its eleven domains distinguish sequence products, RNA,
organ function, clinical response, adverse events and durability. A clinical
case cannot gain independent patients from repeated visits. Missing domains
mean undocumented in this catalog; the tool does not conclude that the paper
omitted them, calculate an efficacy score or infer functional rescue.

Signal roles now distinguish benefit, harm, context and unclear observations.
A detected RNA off-target signal is not a benefit, and no detected serious
adverse events is not zero risk. The [new comparison snapshot](examples/outcome-audit-progeria/report.json)
includes progeria-model molecular, vascular and survival observations. They
remain mouse genetic-disease evidence, separate from ordinary-aging repair.
[Primary progeria report](https://pubmed.ncbi.nlm.nih.gov/33408413/).

For PowerShell source execution, set `$env:PYTHONPATH='src'` and run
`python -m baseevidence.cli ...` with the same subcommand arguments.

## Research direction

Start with a declared causal lesion and relevant functional comparator, then
separate intended sequence products, delivery coverage, organ response and
durability. A known monogenic case is a useful precedent, rather than a
demonstration that heterogeneous age-acquired mutations can be repaired.
The original CPS1 report supplies one clinical case and short initial follow-up.
[Original clinical report](https://pubmed.ncbi.nlm.nih.gov/40373211/).

Transversions and indels outside the classical ABE/CBE classifier belong in a
separate method comparison. The classifier does not assert that they cannot be
edited. [Prime-editing precedent](https://www.nature.com/articles/s41586-019-1711-4).

For dental regeneration, gene correction of a declared defect and engineering
a tooth with enamel, dentin, pulp, cementum, ligament and host integration are
distinct programs. The [ResearchDesk dental track](https://github.com/dylanstechmann/regen-workbench/tree/main/studies/dental-regeneration-2026-10-09)
keeps those outcome domains separate. Oxygen transport and cell identity are
additional construct requirements, not substitutes for genetic or functional
assessment.

See [METHODS.md](METHODS.md) for source access and reproducibility and
[REPORT.md](REPORT.md) for the first software release. No editor, guide,
clinical protocol or rejuvenation intervention is selected by this tool.
