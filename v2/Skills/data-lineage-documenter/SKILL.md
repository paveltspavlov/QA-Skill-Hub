---
name: data-lineage-documenter
description: "Trace data from source through transformations to consumers. Use for impact analysis, ownership, auditability, or unclear dependencies."
---

# Data Lineage Documenter

## When to Use
Use when a table, field, KPI, report, or pipeline needs upstream/downstream lineage. Do not infer lineage solely from matching names.

## Required Inputs
Provide the target asset or field, repository/project location, intended depth (asset-level or column-level), and known platform limits. Useful evidence includes SQL, manifests, orchestration definitions, catalog metadata, and owner documents.

## Procedure
1. Start at the exact target identifier and version; find explicit references in code, configuration, manifests, and catalog records.
2. Trace upstream inputs and downstream consumers one edge at a time. Record each transformation, filter, join, aggregation, rename, and conditional rule that is visible in source.
3. Distinguish direct lineage from inferred or external dependencies. Record dynamic SQL, opaque jobs, manual steps, and missing owners as gaps.
4. For fields and KPIs, document source columns, formulas, null/default behavior, grain, and unit when supported.
5. Assess impact of a proposed change only for verified downstream edges; list the search scope used.

## Output Contract
Provide an overview and a lineage table with: source asset/field, transformation, target asset/field, file/catalog locator, owner, refresh/freshness evidence, and confidence status (verified, partial, unknown). Add an optional Mermaid source-to-consumer diagram, an impact summary, uncovered edges, and next evidence needed.

## Quality Gate
Every drawn edge has a citation to a source artifact. No node is added from a guessed name match. Preserve field names and formulas verbatim where possible. Separate verified lineage from hypotheses and state the search boundary.

## Evidence and Uncertainty
Use repository paths, SQL line ranges, catalog entries, or orchestration configuration as evidence. Mark external systems and manual transfers unknown unless documented. Do not claim complete lineage when dynamic or out-of-repository edges remain. Apply the evidence-readiness-gate.

## References
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
