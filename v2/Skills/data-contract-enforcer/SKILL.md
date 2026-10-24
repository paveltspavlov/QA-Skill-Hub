---
name: data-contract-enforcer
description: "Define and enforce producer-consumer data contracts. Use when schemas, semantics, ownership, or compatibility need a testable agreement."
---

# Data Contract Enforcer

## When to Use
Use for API, event, warehouse, or pipeline contracts where producers and consumers deploy or change independently. Do not use a schema contract as a substitute for data-quality rules or business approval.

## Required Inputs
Request the data asset and grain, current/proposed schema, producer and known consumers, compatibility policy, versioning rules, freshness/SLA, owner, and enforcement location. Mark unknown consumers or policies as blockers when they affect compatibility.

## Procedure
1. Identify the source of truth and preserve its version, field names, and semantic definitions.
2. Specify field names, types, nullability, requiredness, keys, allowed values, units, timezone, and business meaning only when supported.
3. Separate structural schema checks from row-level quality assertions and business rules.
4. Classify the change as compatible, conditionally compatible, or breaking for each known consumer. For independent deployments, prefer expand, migrate, verify, contract.
5. Define checks for producers and consumers, representative conforming/nonconforming samples, owner, monitoring, and rollback or forward-fix limits.

## Output Contract
Return a contract record with: asset and grain; owner; version; producer/consumer list and unknowns; field table (name, type, required/nullability, meaning, constraints); semantic rules; freshness; compatibility classification; enforcement tests; migration steps; and unresolved decisions. Include a valid and invalid example row or payload when the format allows it.

## Quality Gate
Every required field has a defined type and meaning or is marked unresolved. Consumer impact is based on evidence, not naming similarity. Tests distinguish schema shape from data assertions. Breaking changes have a version/migration plan; do not call a change compatible without checking consumers.

## Evidence and Uncertainty
Cite the source schema, contract file, consumer, and test path for each material rule. Ask rather than infer undocumented semantics. If a consumer or business definition is unknown, qualify the compatibility result. Apply the evidence-readiness-gate; never invent a passing check.

## References
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
