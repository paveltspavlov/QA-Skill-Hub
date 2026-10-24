---
name: api-contract-testing
description: "Create tests for HTTP API behavior from an OpenAPI document or explicit contract. Use when validating endpoints, schemas, errors, authentication, and compatibility."
---

# API Contract Testing

## Procedure
1. Inspect the supplied OpenAPI document or written contract and identify version, servers, operations, parameters, request/response schemas, security schemes, and examples.
2. For each in-scope operation, design checks for required and optional inputs, valid/invalid values, boundary values, response schema, status/error behavior, and authorization rules stated by the contract.
3. Identify ambiguous or missing semantics (for example idempotency, pagination, retries, or error shape) as questions; do not invent expectations.
4. Generate tests using the repository’s existing language, client, test framework, and conventions. Avoid unapproved live calls and destructive test data.
5. Verify schema and behavior separately. A schema-valid response does not prove business behavior; a passing mock does not prove a live service.
6. Report operation coverage, evidence, limitations, and commands actually run.

## Output
An operation-to-test matrix, test cases or code in the existing stack, uncovered contract gaps, and verification results.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
