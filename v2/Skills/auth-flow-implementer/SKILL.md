---
name: auth-flow-implementer
description: "Use when implementing or changing authentication and access-control flows."
---

## When to Use
Use for registration, sign-in/out, sessions/tokens, OAuth/OIDC integration, account recovery, or authorization middleware. Treat credential/session and account-linking changes as security-critical.

## Required Inputs
Require framework and identity provider, existing user/session model, login identifiers, token/session lifecycle, redirect/callback URIs, account-link policy, roles/permissions, recovery/verification requirements, threat constraints, secrets configuration path, and tests. Never request real secrets; inspect references/config keys only.

## Procedure
1. Inspect current auth library/version, routes, cookie/token settings, identity schema, middleware, deployment proxy/TLS assumptions, and tests.
2. Diagram trust boundaries and lifecycle: registration/email verification if required, credential/provider validation, account creation/linking, session issuance/refresh rotation/revocation, logout, password recovery, authorization, and failure responses. Clarify identity proof and account-link rules before changing them.
3. Reuse maintained project auth primitives; never invent cryptography or store raw passwords/tokens. Enforce least privilege, secure cookie flags where cookies are used, CSRF protections where relevant, redirect allowlists, and safe error/rate-limit behavior consistent with verified docs.
4. Implement one flow at a time with migrations/config examples free of secrets; include frontend auth context/protected routes only if requested and aligned to the existing client.
5. Test allow/deny, expiration/revocation, invalid callback/state, account collision, recovery abuse boundaries, and session fixation/replay concerns applicable to the chosen design.

## Output Contract
Return: **Flow and trust-boundary summary**; **Policy decisions** (identity, session/token, linking, roles); **Changed files/config keys**; **Migration/rollout and recovery**; **Security-sensitive assumptions/questions**; **Tests/checks run**. Include source code only for the requested stack and known behavior. Mark any unresolved authorization policy as blocking.

## Quality Gate
Critical authorization and identity decisions are explicit and reviewed against the installed library’s official security documentation. No secret values, home-grown password/token crypto, permissive redirect fallback, or privilege escalation path. Tests prove denied as well as successful access. Do not claim production readiness or compliance based on code inspection alone.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
