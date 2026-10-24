# Recorded open work and access limits — as of v0.2.0

This file preserves the session-end state for future AI-assisted tranches.
Working conventions and the tranche recipe live in AGENTS.md and
EVIDENCE_INTAKE.md; this file records what remains open, not how to work.

## Current state (2026-10-24, tag v0.2.0)

- 22 source cards across 7 stages: human_cells 7, animal 7, plant 3,
  human_cohort 2, human_case 1, human_trial 2.
- All 11 outcome domains have at least one source-reported observation,
  including delivery and durability (PCSK9 nonhuman-primate cards).
- 37 unit tests, Ruff clean, 9 provenance receipts all passing
  `baseevidence verify-receipts`. Current snapshot:
  examples/outcome-audit-trials/report.json.

## Open tranches, in rough value order

1. An ex vivo `human_trial` card for the 2026 NEJM BEACON HBG1/HBG2
   promoter sickle-cell trial (PMID 41931046), a different modality from
   the two in vivo PCSK9 cards.
2. Full-text deep reviews of existing cards (the PROGERIA_REVIEW.md
   pattern): access primary full texts, refine limits and denominators.
3. Receipt tooling that retains raw response bytes, so future receipts
   can carry true response SHA-256 hashes instead of records_sha256.
4. Re-review of the two NEJM/abstract-limited cards (CPS1, clonal
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
- The two 2026 human PCSK9 trial cards are open-label phase 1 biomarker
  and interim safety results in patients; no card here establishes
  cardiovascular outcomes, multi-year safety or healthy-adult use.