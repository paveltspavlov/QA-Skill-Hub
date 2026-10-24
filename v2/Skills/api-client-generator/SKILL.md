---
name: api-client-generator
description: "Generate a typed or structured client from an OpenAPI document or verified API contract. Use when application code needs to call documented endpoints."
---

# API Client Generator

## Procedure
1. Inspect the API description, version, auth scheme, project language, HTTP client, and generation conventions.
2. Map operations, parameters, request/response schemas, errors, and pagination into the target client's types and methods.
3. Preserve the contract; do not add undocumented endpoints or infer response shapes.
4. Handle transport errors, API errors, timeouts, and cancellation using project patterns.
5. Add representative client tests and run generation/type validation when available.

## Output
A client matching the documented API and an operation-to-method/type map.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
