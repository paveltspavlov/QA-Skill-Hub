---
name: elt-source-connector
description: "Design an ELT source connector around a documented API or source system. Use when ingesting new data with incremental loads, backfills, or rate limits."
---

# ELT Source Connector

## Procedure
1. Inspect source API/schema, authentication, pagination, rate limits, update semantics, data types, and permissions.
2. Define extraction state/cursor, idempotency, retry/backoff, checkpointing, late updates, deletion handling, and backfill boundaries.
3. Preserve raw source evidence where project conventions require it; make transformations and schema changes explicit.
4. Keep secrets outside code and logs. Test pagination, partial failure, duplicate delivery, rate limiting, and schema drift.
5. Document freshness, ownership, recovery, and required credentials without exposing values.

## Output
A connector design or implementation in the existing stack, plus failure/recovery tests.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
