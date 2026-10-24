---
name: api-client-generator
description: "Use when a frontend or service needs a typed client for a documented API."
---

## When to Use
Use to create or update a client from an OpenAPI document, repository routes, or another explicit API contract. Do not infer endpoints from UI labels or backend assumptions.

## Required Inputs
Require the contract source and version, target language/framework, client location, installed HTTP/query libraries, auth and error conventions, and desired scope (types, transport, hooks, mocks). Identify pagination, cancellation, retries, and code-generation constraints if applicable; ask when any changes client behavior.

## Procedure
1. Inspect contract and repo patterns; note operation IDs, methods, path/query/header parameters, request/response schemas, nullability, status codes, auth, pagination, and errors.
2. Compare contract to existing client and list drift; do not silently widen types or repair ambiguous schemas.
3. Map each operation to a method and exported types. Generate only requested layers: transport wrapper, query/mutation integration, test mocks, barrel exports. Keep auth refresh, retries, timeout, and serialization aligned with observed project behavior; retries must not replay non-idempotent writes unless contract and client policy explicitly allow it.
4. Add focused contract tests for representative success/error, serialization, and cancellation/pagination when in scope.
5. Run generator, formatter, typecheck, and relevant tests that exist; inspect the diff for missing or extra operations.

## Output Contract
Return: **Contract source/version**; **Operation map** (operation, method/path, inputs, result/error types, auth); **Files changed/generated**; **Compatibility decisions/assumptions**; **Verification** (exact commands and results, or not run). Include client implementation and tests when asked. Example map row: `listTeams | GET /teams | page: number | TeamPage | bearer | 401/5xx`, only if supported by source.

## Quality Gate
Every contract operation in scope appears once with accurate parameter optionality and response nullability. No invented server fields, auth behavior, status codes, or default retries. Types compile against installed versions; mocks reflect—not replace—the source of truth. Keep generated diffs limited and reproducible; document unresolved contract drift rather than choosing a shape.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
