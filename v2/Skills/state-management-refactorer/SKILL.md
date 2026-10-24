---
name: state-management-refactorer
description: "Use when simplifying state ownership, duplicated values, or UI state flow."
---

## When to Use
Use for tangled React state, deep prop passing, duplicated state logic, or migration between state patterns. Use only measured profiling evidence for performance claims.

## Required Inputs
Require components and callers in scope, current state behavior, shared/local ownership, side effects, persistence/cache needs, framework/library versions, existing tests, and whether a new state library is allowed. Identify derived values and synchronization requirements.

## Procedure
1. Trace each state value from owner through writers/readers; map derived values, server/cache state, URL/form state and side effects separately.
2. Identify duplicate sources of truth, stale synchronization, prop chains and repeated transition logic; cite paths/symbols.
3. Choose the smallest project-consistent change: compute derivable data, extract a hook for reusable logic, lift state only to common owner, or introduce reducer/store only when transitions/sharing justify it. Never migrate libraries without approval and compatibility analysis.
4. Preserve loading/error/optimistic/undo behavior and effect cleanup. Add behavior tests before restructuring; use profiler only if claiming render/performance gains.
5. Refactor incrementally and run affected component tests/typecheck; inspect consumer API changes.

## Output Contract
Return: **Current state-flow map**; **Identified sources of truth**; **Target ownership and rationale**; **Migration steps/files**; **Behavior-preservation tests**; **Verification/performance evidence**. Example: derive `total` from `items` rather than maintaining both only if no independent edit path for `total` exists.

## Quality Gate
Each value has an explicit owner and update path; no stale duplicate or accidental effect loop is introduced. Shared state remains correctly scoped and external synchronization is tested. Use installed library docs for version-specific APIs. Do not claim fewer re-renders or better performance absent a comparable profile.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
