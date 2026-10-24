---
name: sql-query-optimizer
description: "Improve a slow SQL query without changing its result semantics. Use when actual query plans or performance evidence are available."
---

# SQL Query Optimizer

## When to Use
Use to diagnose and improve a slow SQL query when query text, schema, database engine/version, and preferably an actual plan or timing are available. Do not promise speedup from stylistic rewrite or run expensive analysis against production without permission.

## Required Inputs
Collect SQL and parameter values/distribution, engine/version, schema and indexes, constraints, row counts/statistics, workload and transaction context, baseline elapsed/CPU/I/O data, actual plan (`EXPLAIN` or safe equivalent), target latency/throughput, and read/write trade-offs. Ask for representative and privacy-safe samples.

## Procedure
1. Confirm query semantics: joins, null behavior, duplicate preservation, ordering, limits, isolation, and expected outputs. Capture result sample/checksum or assertions before changing it.
2. Read actual plan with estimates and runtime metrics where safely available. Identify expensive scans, join strategy/cardinality mismatch, sort/hash spills, repeated subplans, filtering selectivity, and parameter sensitivity; separate observed bottleneck from hypothesis.
3. Propose one small change at a time: projection/predicate reduction, sargable conditions, join/subquery restructure, statistics, or index only if plan supports it. Do not assume CTEs are faster or prescribe engine-specific syntax without verification.
4. Check semantic equivalence on representative positive, null, duplicate, boundary, and empty cases. Index proposals include key order, predicate/use case, write/storage cost, lock/concurrency risk, and database-specific creation method; don't run DDL without approval.
5. Benchmark with same parameters, dataset, cache conditions, concurrency, and measurement method. Compare result equivalence and plan as well as latency; report variance/limitations and rollback.

## Output Contract
Provide `Baseline and environment`; table `Finding | Plan evidence | Change | Semantic risk | Expected trade-off`; `Rewritten query` (if justified); `Equivalence checks`; benchmark table `Run/parameters | Result equivalence | Plan change | Timing/resource evidence | Caveats`; `Rollback`. Example: `plan shows repeated scan of filtered relation | predicate/selectivity supports candidate index | possible write/storage cost | verify duplicates/nulls unchanged | timing TBD until run`.

## Quality Gate
Engine/version and plan source are explicit; rewritten SQL preserves duplicate/null/order semantics; changes are supported by measured plan evidence; index advice reflects engine docs; benchmark is controlled; no claimed improvement or execution unless measured. Review official database documentation for consequential syntax.

## Evidence and Uncertainty
Use plan text, schema/statistics, measured runs, result comparisons, and current official engine docs. Mark assumptions and untested parameter cases. Four evidence checks—scope clear, claims traceable, complete output, relevant verification—25 each; below 75/100, ask, qualify, or abstain. No guessed confidence percentages. Critical safety, authorization, privacy, or acceptance failures block readiness.
