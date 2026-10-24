---
name: data-quality-test-writer
description: "Create reusable data-quality assertions for tables and pipelines. Use when validating freshness, uniqueness, completeness, relationships, distributions, or business rules."
---

# Data Quality Test Writer

## When to Use
Use to create or review checks for batch/streaming tables, warehouse models, ingestion pipelines, and governed datasets. Choose assertions from explicit semantics and risks, not an assumption that every column must be non-null or unique.

## Required Inputs
Ask for platform/SQL dialect and version, table/model and grain, key fields and owners, business definitions, expected nullability/cardinality, freshness/volume rules and time zone, relationships, sample or representative data, test framework (such as dbt if present), severity/action on failure, and sensitivity constraints. Thresholds need a domain owner/source.

## Procedure
1. Establish asset, grain, partitioning, lifecycle, lineage, consumer impact, and available test environment. Inspect existing tests/macros and follow native conventions.
2. For each rule, define scope/filter/window, expected condition, null semantics, tolerated exceptions, and whether it is a hard invariant or anomaly signal.
3. Select checks as justified: not-null/completeness; uniqueness at the declared grain; accepted values; referential integrity; freshness/watermark; row-count/volume; distribution/range; and domain-specific cross-field rules. Use denominator and window for rates.
4. Write assertions that identify failing rows or aggregates while minimizing sensitive output. Ensure incremental/partition filters cannot hide old bad data inadvertently.
5. Add clear failure messages and owner/action. Use fixtures/seeds or controlled samples for pass/fail tests, including edge conditions. Run the smallest relevant suite and report actual results.

## Output Contract
Return table `Test ID | Asset/grain | Rule/source | Scope/window | Assertion/query | Threshold/source | Failure evidence | Severity/action | Owner`; include code in project dialect only if enough context. Sample: `DQ-1 | orders/order_id | order ID unique per source contract | current partition | count(*) vs count(distinct order_id) | exact invariant per owner | duplicate keys, redacted | Block load per policy | data owner`. Include uncovered rule gaps and false-positive handling.

## Quality Gate
Each assertion matches documented grain and null semantics; threshold is justified rather than guessed; tests expose actionable failures; sensitive values are masked; dialect/framework is checked against project docs; test fixtures distinguish expected anomalies from defects; no “passed” claim without execution.

## Evidence and Uncertainty
Tie rules to schema, data contract, owner decisions, sample rows, query output, or official framework docs. State sample limitations and distinguish hard constraints from monitoring signals. Evidence readiness: scope, traceability, deliverable completeness, relevant verification each need evidence (25 points); below 75/100, ask, qualify, or abstain. Never invent confidence percentages. Critical safety, privacy, authorization, or acceptance failures block readiness.
