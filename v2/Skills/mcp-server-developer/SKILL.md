---
name: mcp-server-developer
description: "Use when implementing an MCP server exposing defined tools or resources."
---

## When to Use
Use to build or extend an MCP server against a specified SDK/protocol and host. Do not choose write capabilities, remote auth, or data exposure without explicit authorization.

## Required Inputs
Require target language/runtime, SDK and protocol version, server purpose, tools/resources/prompts and schemas, underlying services, transport (stdio/HTTP), identity/access model, data sensitivity, deployment target, package policy, and test/inspector availability.

## Procedure
1. Inspect current official MCP spec and SDK docs for the named versions; define capability inventory and least-privilege boundary.
2. Design each tool around one user intent, with constrained input schema and descriptions that state when to call, effects and limitations. Define resources/prompts separately.
3. Implement handlers as adapters to existing business logic; validate inputs, authorize every operation, bound output, handle cancellation/errors structurally, and avoid leaking internals. For stdio, reserve stdout for protocol and log to stderr; for network transports, apply documented authentication and transport protections.
4. Pin dependencies per project policy and provide host config with secret placeholders.
5. Test initialize/capability discovery, schema validity, each tool success/error, authorization, malformed input and transport behavior; run Inspector only if available and report exact version/results.

## Output Contract
Return: **Capability plan**; **File tree/dependencies**; **Protocol/SDK versions and sources**; **Tool/resource contracts**; **Transport/auth/config**; **Implementation**; **Inspector or test plan/results**; **Known limits**. Example tool spec: `search_orders` has read-only effect, tenant-scoped query and bounded results—only if underlying service supports it.

## Quality Gate
Every capability has verified source semantics and authorization. Mutating or destructive tools are visibly described and protected according to user policy; never assume confirmation flags or error field shapes without spec verification. No stdout logging on stdio; no raw exception/secret leakage. Do not invent protocol versions or claim Inspector validation without running it.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
