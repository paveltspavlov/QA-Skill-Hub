---
name: migration-planner
description: "Plan a staged technology or data migration with compatibility, validation, rollback, and cutover steps. Use when a system, framework, or schema must move safely."
---

# Migration Planner

## Procedure
1. Record source/target versions, inventory, dependencies, consumers, service constraints, and desired end state.
2. Identify incompatible changes, deprecations, conversions, and parallel-run requirements from version-specific sources.
3. Design phases with entry/exit checks, observability, ownership, and a safe rollback or forward-fix path.
4. Include data reconciliation and compatibility tests for producers and consumers.
5. Flag irreversible steps and unknowns; do not invent downtime, cost, or compatibility guarantees.

## Output
A phased plan, verification matrix, rollback strategy, and decision list.

## References
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
