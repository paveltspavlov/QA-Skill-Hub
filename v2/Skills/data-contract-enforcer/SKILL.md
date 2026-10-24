---
name: data-contract-enforcer
description: "Define and validate data contracts between producers and consumers. Use when schema or semantic changes can break downstream systems."
---

# Data Contract Enforcer

## Procedure
1. Identify producer, consumer, grain, schema version, compatibility policy, freshness/SLA, and ownership.
2. Specify required fields, types, nullability, allowed values, keys, and semantic expectations from requirements.
3. Add contract checks to the existing build path; distinguish schema-shape validation from data-quality assertions.
4. Classify changes for compatibility and document migration/versioning for breaking changes.
5. Validate conforming and violating samples; report consumers and assumptions.

## Output
A versioned contract, enforcement tests, compatibility notes, and owner/action map.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
