# Recorded open work and access limits — as of v0.3.0

This file preserves the session-end state for future AI-assisted tranches.
Working conventions and the tranche recipe live in AGENTS.md and
EVIDENCE_INTAKE.md; this file records what remains open, not how to work.

## Current state (2026-10-24, tag v0.3.0)

- 23 source cards across 7 stages: human_cells 7, animal 7, plant 3,
  human_cohort 2, human_case 1, human_trial 3.
- All 11 outcome domains have at least one source-reported observation,
  including delivery and durability (PCSK9 nonhuman-primate cards).
- 41 unit tests, Ruff clean, 12 provenance receipts all passing
  `baseevidence verify-receipts`. Current snapshot:
  examples/outcome-audit-macaque-review/report.json.

## Open tranches, in rough value order

1. Full-text deep reviews of the remaining open-access cards (the
   PROGERIA_REVIEW.md and MACAQUE_REVIEW.md pattern). The 2026-10-24
   accessibility probe (exact identifier queries, title-verified) found
   open PMC full texts for: col7a1-rdeb-2022 (PMC9666996),
   kcnj13-retina-2023 (PMC10541187), cbe-fidelity-2020 (PMC7335424),
   abe8e-y149v-2026 (PMC13225742), car-t-pik3cd-2026 (PMC12948676),
   cbe-2016 (PMC4873371), abe-2017 (PMC5726555) and prime-2019
   (PMC6907044).

## Standing access limits (not gaps in diligence)

- Every card added on 2026-10-24 is abstract-level: full texts were not
  accessed and cards say so in their access_level field.
- Exception: pcsk9-macaques-2021 is full-text reviewed (2026-10-24,
  MACAQUE_REVIEW.md); its per-animal denominators are source-stated.
- The NEJM re-review tranche closed 2026-10-24 by live test: both NEJM
  records (cps1-case-2025, clonal-hematopoiesis-2014) are present in
  Europe PMC but non-open, and fullTextXML requests return HTTP 500.
  rna-offtargets-2019 and stemcell-mutation-accumulation-2016 are
  likewise present but non-open in Europe PMC.
- Per-animal, per-donor and per-cohort denominators stay null wherever
  the accessed abstracts do not state them.
- The delivery/durability precedent is liver-targeted LNP editing in
  nonhuman primates: one organ, one route, one disease context. No card
  establishes whole-body adult delivery, durable human safety, or
  enhancement use.
- The three 2026 human trial cards are open-label phase 1/1-2 biomarker
  and interim safety results in patients; no card here establishes
  cardiovascular outcomes, sickle-cell cure, multi-year safety or
  healthy-adult use.