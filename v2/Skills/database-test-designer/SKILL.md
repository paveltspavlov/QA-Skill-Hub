---
name: database-test-designer
description: "Design database tests for schema, migrations, constraints, transactions, concurrency, and data integrity. Use when a change reads or writes persistent data."
---

# Database Test Designer

## Procedure
1. Identify the database engine/version, schema objects, migration path, transaction boundaries, and data ownership from the project.
2. Derive tests for constraints, nullability, uniqueness, relationships, defaults, rollback, isolation, concurrency, and representative CRUD flows.
3. Use isolated data and cleanup. Test migration from supported starting states, not just a fresh database.
4. Verify cross-row rules against the actual engine; do not assume all engines enforce features identically.
5. Map each test to a requirement and describe setup, expected result, and cleanup.

## Output
A migration/data-integrity test matrix and, when requested, tests in the repository's existing framework.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
