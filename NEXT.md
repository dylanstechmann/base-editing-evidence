# Recorded open work and access limits — as of v0.3.0

This file preserves the session-end state for future AI-assisted tranches.
Working conventions and the tranche recipe live in AGENTS.md and
EVIDENCE_INTAKE.md; this file records what remains open, not how to work.

## Current state (2026-10-24, tag v0.3.0)

- 23 source cards across 7 stages: human_cells 7, animal 7, plant 3,
  human_cohort 2, human_case 1, human_trial 3.
- All 11 outcome domains have at least one source-reported observation,
  including delivery and durability (PCSK9 nonhuman-primate cards).
- 41 unit tests, Ruff clean, 20 provenance receipts all passing
  `baseevidence verify-receipts`. Current snapshot:
  examples/outcome-audit-methods-papers/report.json.

## Open tranches, in rough value order

1. None remain in the full-text-review category: all ten cards with
   open-access full texts are full-text reviewed as of 2026-10-24
   (PROGERIA_REVIEW.md, MACAQUE_REVIEW.md, COL7A1_REVIEW.md,
   KCNJ13_REVIEW.md, CBE_FIDELITY_REVIEW.md, ABE8E_Y149V_REVIEW.md,
   CART_PIK3CD_REVIEW.md and FOUNDATIONAL_METHODS_REVIEW.md). Candidate
   next tranches: new source cards using `fetch-receipt`, or re-probing
   access for the non-open records.

## Standing access limits (not gaps in diligence)

- Every card added on 2026-10-24 is abstract-level: full texts were not
  accessed and cards say so in their access_level field.
- All ten cards with open-access full texts (progeria, pcsk9-macaques,
  col7a1-rdeb, kcnj13-retina, cbe-fidelity, abe8e-y149v, car-t-pik3cd,
  cbe-2016, abe-2017 and prime-2019) are full-text reviewed as of
  2026-10-24; their stated denominators are source-stated.
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