---
name: mcp-tool-designer
description: "Use when designing MCP tool names, descriptions, schemas, and examples."
---

## When to Use
Use to convert one or more user intents into discoverable, constrained MCP tool contracts before implementation.

## Required Inputs
Require user intents, underlying API/data fields and behavior, read/write/destructive effects, authorization, idempotency, error semantics, relevant MCP spec/SDK version, and expected host/model context. Unknown backend fields or actions must be clarified, not invented.

## Procedure
1. Split by distinct user intent; avoid a vague catch-all and unnecessary fragmentation.
2. Name each tool with an unambiguous action and object using project/spec-compatible identifiers.
3. Write LLM-facing description: when to call, when not to call, scope, side effects, limits, and required preconditions.
4. Define input schema from actual backend contract: requiredness, enums, formats, bounds, defaults only when safe; describe every field and reject ambiguity. Define output and stable error behavior using the chosen SDK/spec, not assumed examples.
5. Mark read/write/destructive effects and authorization/idempotency; require explicit user confirmation only where product policy and interface support it.
6. Create positive and negative prompt examples with exact valid calls; validate schemas and review discoverability.

## Output Contract
Return for each tool: **Name**; **Intent and side-effect class**; **When to call / not call**; **Input schema**; **Output/error contract**; **Authorization/idempotency**; **Worked examples** (at least 2 positive and 1 negative with expected selection); **Open questions**. Add an inventory table showing which user intent maps to which tool.

## Quality Gate
Names and schemas reflect real backend operations; field descriptions explain semantics rather than repeat type. Small closed value sets use enumerations only when supported. Destructive behavior is conspicuous; errors and confirmation rules follow actual host/product policy. Test whether examples select the intended tool without inventing tool calls unsupported by the schema.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
