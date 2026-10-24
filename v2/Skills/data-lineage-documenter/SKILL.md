---
name: data-lineage-documenter
description: "Trace and document data lineage from source to transformation, model, and consumer. Use when impact analysis or ownership is unclear."
---

# Data Lineage Documenter

## Procedure
1. Start from the requested table, field, report, or pipeline and inspect SQL, configuration, manifests, and dependency metadata.
2. Trace upstream inputs and downstream consumers using explicit references; do not infer from matching names alone.
3. Record transformations, filters, joins, schedules, owners, and freshness only when supported by source artifacts.
4. Mark gaps where lineage is dynamic, external, or unavailable and identify the next evidence needed.
5. Present a readable graph or source → transformation → output table with file/line links.

## Output
A lineage map, impact summary, evidence links, and unknown edges.

## References
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
