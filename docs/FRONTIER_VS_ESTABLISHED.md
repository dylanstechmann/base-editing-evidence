# Frontier versus established evidence

**Date:** 2026-11-27

This note separates reproducible repository checks from unresolved biological and clinical questions. “Established” here describes the current catalog and software audit, not independent confirmation of every underlying source.

## Established: reproducible catalog and software audit

- `PYTHONPATH=src python3 -m unittest discover -s tests -v` passes all **51 tests**.
- With the LF-designated catalogs, `PYTHONPATH=src python3 -B -m baseevidence.cli audit-outcomes data/outcomes.json --studies data/studies.json --out fresh-full` creates `fresh-full/report.json` at **101,772 bytes** with SHA-256 `9ef4b8c0d76a35b5249c55808414abcee38bf5e5fadb85073395cb50582f29c6`. The committed reproducible snapshot is byte-identical; earlier snapshots remain historical.
- The adverse-events domain review covers 23 catalogued studies: **16 have `no_catalog_row`**, while **seven have recorded outcomes**. A missing row means only that this catalog has no adverse-events observation for that study. It is not a zero count, a source-reported absence of signal, or a negative biological finding. Recorded `source_reports_no_signal` rows remain distinct source-scoped observations.

## Frontier and not established

- **Source completeness:** the catalog is not shown to be exhaustive. Source access limits, unreviewed reports, incomplete extraction and later publications can leave gaps.
- **Absence-of-signal interpretation:** no detected signal in a particular assay, population or follow-up interval does not establish zero risk, universal absence or long-term safety.
- **Editor safety and efficacy:** the audit does not identify a safe or effective editor, rank editors clinically, establish comparative efficacy or support treatment decisions.
- **Functional outcomes:** sequence products and molecular measurements do not by themselves establish tissue-level functional rescue, durable benefit or improved clinical outcomes.
- **Laboratory and clinical validation:** passing software tests and reproducing a report provide no laboratory replication, functional experiment, clinical validation or owner review of the source claims.

## Update when evidence changes

Revisit this note whenever the catalogs, source access, reviewed evidence, implementation or tests change. Generate a new snapshot rather than overwriting historical reports; rerun the full tests and audit before updating counts or byte pins. Keep missing catalog rows, explicit review gaps and source-reported absence of signal separate, and state any new laboratory, clinical or independent source review explicitly rather than inferring it from software results.
