---
name: elt-source-connector
description: "Design or implement an ELT connector from a documented source. Use for API/database ingestion, incremental loads, backfills, or schema drift."
---

# ELT Source Connector

## When to Use
Use when onboarding a data source or improving extraction reliability. Do not select a connector framework or assume full reload is safe without project evidence.

## Required Inputs
Source API/spec or database, authentication method (never the secret itself), endpoint and version, pagination, rate limits, update/delete semantics, expected volume, freshness, destination, retention, and existing ingestion framework.

## Procedure
1. Verify source operations and permissions from an official specification or supplied source documentation.
2. Define extraction unit, cursor/watermark, stable identity, idempotency, checkpointing, retries/backoff, timeout, and partial-failure recovery.
3. Specify initial load, incremental updates, late-arriving changes, deletes, backfill windows, schema drift, and duplicate handling.
4. Preserve raw source values and ingestion metadata when project policy requires it; keep credentials in approved secret storage and out of code/logs.
5. Add tests for pagination, rate limiting, duplicate delivery, partial failure, cursor resume, schema changes, and deletion behavior.

## Output Contract
Return a connector specification or patch with: source/version; permissions; extraction state; request/response schema; pagination and rate-limit behavior; incremental/backfill plan; idempotency/retry policy; raw and transformed fields; observability/alerts; test matrix; and recovery/runbook. Include field-to-source mapping and unknowns.

## Quality Gate
The design can resume after interruption without data loss or uncontrolled duplication. All state transitions are testable. Secrets are never emitted. No unsupported freshness or delivery guarantee is claimed.

## Evidence and Uncertainty
Cite the exact API/schema/version and repository patterns used. Mark undocumented deletion/update semantics as unresolved and ask before coding destructive sync behavior. Apply the evidence-readiness-gate.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
