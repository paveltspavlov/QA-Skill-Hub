---
name: schema-evolution-manager
description: "Plan compatible schema changes across producers, stores, and downstream consumers. Use for database, event, API, or warehouse schema evolution."
---

# Schema Evolution Manager

## Procedure
1. Identify the current schema/version, producer and consumer inventory, compatibility policy, migration state, and owner.
2. Classify changes as additive, optionality/type change, rename, removal, or semantic change.
3. Prefer expand-migrate-contract sequencing when consumers deploy independently; add, backfill, verify, switch, and remove only after evidence.
4. Generate compatibility checks and test old/new producer-consumer combinations; document rollback constraints.
5. Do not claim compatibility without checking actual consumers and platform behavior.

## Output
A change matrix, migration sequence, compatibility tests, and consumer risks.

## References
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
