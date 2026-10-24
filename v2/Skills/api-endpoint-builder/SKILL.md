---
name: api-endpoint-builder
description: "Use when implementing a REST or GraphQL operation against a repository contract."
---

## When to Use
Use for a new or changed endpoint/operation with known behavior and an identifiable framework. For schema design without behavior, clarify the contract first.

## Required Inputs
Need method/path or GraphQL operation, request and response shape, status/error semantics, authentication and authorization rules, side effects, persistence model, existing router/service/validator conventions, and applicable test commands. Identify pagination/filter/sort expectations for collections.

## Procedure
1. Inspect nearby routes, middleware, services, data models, error mapper, API spec, and tests before editing.
2. Write a behavior map: inputs and validation, access policy, domain action, persistence, response/status, errors, idempotency and side effects. For collection endpoints, capture contract-defined pagination, filtering and sorting; do not add them by habit. Resolve missing authorization or data semantics before implementation.
3. Implement the narrow route/resolver and delegate business logic consistently; validate untrusted input, scope records to the authorized principal, avoid leaking internals, and use transactions for multi-write atomicity when repository patterns require them.
4. Update contract/docs and tests: success, malformed/boundary input, unauthenticated/unauthorized, not found/conflict, and persistence failure where relevant.
5. Run focused tests, type/lint checks available; inspect changed routes and error mapping.

## Output Contract
Return: **Operation contract** (method/path or GraphQL name, inputs, outputs, status/errors, auth); **Implementation files** (handler, validator, service/storage); **Behavior and side effects**; **Tests added/updated**; **Verification**. If drafting only, label code as a proposal. Example: `POST /teams` must state creator-role behavior only if specified; do not infer it.

## Quality Gate
Route is registered in the correct router; all inputs are validated and authorization is applied at the object/action boundary. Responses match the documented schema and project error format. Tests exercise both allowed and denied paths and important invalid inputs. No secrets or raw exceptions are returned; report incomplete contract instead of inventing it.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
