---
name: database-schema-designer
description: "Design a relational or document schema from explicit data and access requirements. Use when adding entities, relationships, constraints, or indexes."
---

# Database Schema Designer

## Procedure
1. Extract entities, lifecycle, ownership, cardinality, query patterns, volume, retention, and privacy requirements.
2. Propose tables/collections, keys, relationships, nullability, uniqueness, checks, and indexes; state engine-specific assumptions.
3. Explain normalization or denormalization choices and how constraints protect integrity.
4. Include forward migration, backfill, rollback limits, and compatibility impacts for consumers.
5. Validate against the actual database and project migration conventions; do not assume identical enforcement across engines.

## Output
A schema sketch, relationship rationale, constraints/index plan, migration notes, and open questions.

## References
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
