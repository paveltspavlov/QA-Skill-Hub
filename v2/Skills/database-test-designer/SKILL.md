---
name: database-test-designer
description: "Design database tests for schema, migrations, constraints, transactions, concurrency, and data integrity. Use when a change reads or writes persistent data."
---

# Database Test Designer

## When to Use
Use when changes affect schemas, migrations, SQL/ORM persistence, transactional workflows, constraints, or concurrent access. Cover relational or non-relational behavior only with the engine/version identified; do not assume equivalent semantics across engines.

## Required Inputs
Obtain database engine/version, schema and migration scripts, supported starting states, transaction/isolation configuration, ORM/driver, data volume and ownership, business invariants, test framework, safe disposable environment, backup/rollback policy, and permission for test execution. Never run migration or destructive checks on production.

## Procedure
1. Map tables/collections, keys, constraints, defaults, triggers, relationships, transactions, and the application's read/write paths from code and DDL.
2. Derive cases for valid CRUD; null/type/range/unique/FK/check violations; defaults; cascades/restrict behavior; duplicate/reordered requests; atomicity/rollback; concurrent conflicting writes; and indexes only when query behavior is in scope.
3. Test migrations from each supported prior state with representative data and relevant constraints. Check upgrade path, preserved values, rollback/recovery plan, and repeatability. Do not assume down migration is lossless; state what must be confirmed.
4. Build isolated fixtures and deterministic cleanup. Test expected failure class/state using the actual engine; treat ORM validation and database enforcement as different layers.
5. Define concurrency schedule and invariant rather than guessing isolation results; check engine/version official docs for consequential semantics. Include seed/cleanup commands only after validation in disposable environment.

## Output Contract
Provide matrix `ID | Requirement/object | Setup/state | Operation | Expected DB/app result | Evidence/assertion | Cleanup`; group as constraint, migration, transaction, concurrency, and query plan. Example: `DB-04 | order unique(external_id) | two sessions; same key | concurrent insert | exactly one committed if invariant/constraint is declared | row count + losing transaction error | rollback test rows`—adapt expected result to actual DDL/contract.

## Quality Gate
Each expectation traces to DDL, app contract, or domain invariant; migration covers real prior state; engine-specific behavior isn't generalized; test data is isolated; rollback/cleanup are safe; expected state and error are verifiable; only actual runs are described as executed.

## Evidence and Uncertainty
Cite DDL, migration version, code, engine/version, test output, and official database docs. Mark unsupported engine behavior or missing invariant as a question. Evidence gate checks scope, claim traceability, complete output, and relevant verification (25 each); below 75/100, ask, qualify, or abstain. No guessed confidence percentages. Critical authorization, privacy, safety, or acceptance failures cannot be averaged away.
