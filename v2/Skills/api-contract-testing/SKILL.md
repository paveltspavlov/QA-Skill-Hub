---
name: api-contract-testing
description: "Create tests for HTTP API behavior from an OpenAPI document or explicit contract. Use when validating endpoints, schemas, errors, authentication, and compatibility."
---

# API Contract Testing

## When to Use
Use to derive or implement contract tests for HTTP APIs from OpenAPI or an explicit interface contract; assess provider/consumer compatibility; or expose undocumented behavior before release. Include versioning where relevant.

## Required Inputs
Obtain the exact contract and version, in-scope operations, server/implementation versions if known, test framework and existing patterns, auth roles/scopes, test environment and credentials handling, and permission for calls. Identify whether expected behavior is contract-derived or needs product-owner clarification.

## Procedure
1. Parse each operation: method/path, path/query/header/cookie parameters, requiredness, serialization, request body, response codes/headers/body schemas, security requirements, examples, deprecation, and references. Verify against the OpenAPI version and official specification; do not silently repair invalid source.
2. Build equivalence classes and boundary cases only from declared schema constraints: required/absent, null where permitted, types/formats, lengths/ranges, enums, arrays/objects, and additional properties. Separate schema validation from business-rule testing.
3. Cover documented success and error responses, authn/authz by role, malformed inputs, content negotiation, and pagination/idempotency/retry only where specified. List undocumented semantics as questions rather than expected results.
4. Implement in repository-native tools. Isolate data; avoid destructive or unapproved live calls. Keep secrets outside test output. Prefer provider verification and consumer expectations appropriate to available infrastructure.
5. Run unit/mock contract checks, then authorized integration checks if available. Validate response status, headers, schema, and side effects separately; a passing mock is not proof of deployed behavior.

## Output Contract
Provide operation coverage table `Operation | Contract source/version | Valid cases | Negative/boundary cases | Auth cases | Response/error oracle | Tests/status`; then test cases `ID | Preconditions | Request | Expected status/headers/body | Assertion | Requirement/schema pointer`. Report uncovered operations and ambiguous rules. Example: `POST /widgets | spec v3.1 | valid required fields | missing name; max/max+1 only if max declared | viewer denied only if defined | documented 201 schema / declared error | schema validation`.

## Quality Gate
Every in-scope operation is listed; outputs map to explicit contract rules; nullable/optional distinctions are preserved; test data is safe; test result and generated code are not conflated; failures include request/response evidence with secrets redacted. Cite official OpenAPI documentation for consequential syntax/version claims.

## Evidence and Uncertainty
Use contract fragments, operation IDs, schema pointers, test output, and authoritative docs. Mark unspecified behavior “open question.” Apply evidence readiness across scope, traceable claims, complete output, and relevant verification (25 points each); below 75/100, ask, qualify, or abstain. Do not invent confidence percentages. Critical authorization, privacy, safety, or acceptance failures block readiness.
