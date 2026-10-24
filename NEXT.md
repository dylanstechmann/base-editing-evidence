# Recorded open work and access limits — as of v0.3.0

This file preserves the session-end state for future AI-assisted tranches.
Working conventions and the tranche recipe live in AGENTS.md and
EVIDENCE_INTAKE.md; this file records what remains open, not how to work.

## Current state (2026-10-24, tag v0.3.0)

- 23 source cards across 7 stages: human_cells 7, animal 7, plant 3,
  human_cohort 2, human_case 1, human_trial 3.
- All 11 outcome domains have at least one source-reported observation,
  including delivery and durability (PCSK9 nonhuman-primate cards).
- 41 unit tests, Ruff clean, 11 provenance receipts all passing
  `baseevidence verify-receipts`. Current snapshot:
  examples/outcome-audit-beacon/report.json.

## Open tranches, in rough value order

1. Full-text deep reviews of existing cards (the PROGERIA_REVIEW.md
   pattern): access primary full texts, refine limits and denominators.
2. Re-review of the two NEJM/abstract-limited cards (CPS1, clonal
   hematopoiesis) if full texts become accessible.

## Standing access limits (not gaps in diligence)

- Every card added on 2026-10-24 is abstract-level: full texts were not
  accessed and cards say so in their access_level field.
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