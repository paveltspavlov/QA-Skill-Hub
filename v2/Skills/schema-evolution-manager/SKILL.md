---
name: schema-evolution-manager
description: "Plan compatible schema changes across producers and consumers. Use for database, API, event, or warehouse schema changes and version migrations."
---

# Schema Evolution Manager

## When to Use
Use when fields, types, semantics, keys, or versions change across independently deployed producers and consumers. Do not claim compatibility from schema shape alone.

## Required Inputs
Current and target schemas, versions, producer/consumer inventory, compatibility policy, deployment order, data volume, backfill needs, retention, owners, and rollback constraints.

## Procedure
1. Compare fields and semantics; classify additions, optionality changes, type changes, renames, removals, and meaning changes.
2. Map each change to known consumers and wire/storage compatibility rules for the actual platform and versions.
3. Plan expand → migrate/backfill → verify consumers → switch → contract/deprecate when independent deployment requires it.
4. Define compatibility tests for old/new producer-consumer pairs, data reconciliation, monitoring, rollback or forward-fix, and deprecation communication.
5. Delay removals until telemetry or owner confirmation supports safe retirement; mark unknown consumers as unresolved.

## Output Contract
Return a compatibility matrix (change, old/new schema, affected consumers, compatibility status, evidence, mitigation), phased migration checklist with owners/exit conditions, tests, data validation/reconciliation queries if supported, rollback limitations, and open questions.

## Quality Gate
No breaking change is hidden as additive. Backfills and consumer migrations have measurable exit conditions. Rollback claims reflect actual data reversibility. Unknown consumers are not treated as unaffected.

## Evidence and Uncertainty
Use actual manifests, schemas, repository references, and platform documentation for compatibility claims. Ask when consumer inventory or semantic ownership is incomplete. Apply the evidence-readiness-gate.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
