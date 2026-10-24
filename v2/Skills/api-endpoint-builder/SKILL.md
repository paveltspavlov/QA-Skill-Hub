---
name: api-endpoint-builder
description: "Implement or draft an HTTP API endpoint from an explicit contract using the repository's existing framework and conventions. Use when a route, handler, or operation is requested."
---

# API Endpoint Builder

## Procedure
1. Read the API contract, framework patterns, validation, authorization, error handling, and tests before coding.
2. Map the operation to request/response schemas, status codes, access rules, and side effects. Ask about undocumented behavior that blocks correctness.
3. Implement the smallest endpoint consistent with the project. Validate inputs and avoid exposing internal errors or sensitive data.
4. Add contract and behavior tests using the existing stack; include invalid-input and authorization cases.
5. Run relevant checks and report contract gaps or checks not run.

## Output
A focused endpoint and tests, plus a summary of contract mappings and verification.

## References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
