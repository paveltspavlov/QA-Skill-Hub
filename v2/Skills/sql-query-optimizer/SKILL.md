---
name: sql-query-optimizer
description: "Improve a slow SQL query without changing its result semantics. Use when actual query plans or performance evidence are available."
---

# SQL Query Optimizer

## Procedure
1. Capture the query, schema/indexes, representative parameters, row volumes, database/version, and baseline timings.
2. Inspect the query plan and statistics before rewriting; identify scans, joins, cardinality errors, sorts, and repeated work.
3. Propose one semantic-preserving change at a time, such as predicate changes, projection reduction, join rewrite, or justified indexing.
4. Compare results and query plans under representative conditions. Measure before/after; do not promise speedups without evidence.
5. Document trade-offs in write cost, storage, portability, and parameter sensitivity.

## Output
An optimized query or ranked recommendations with plan evidence and equivalence checks.

## References
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
