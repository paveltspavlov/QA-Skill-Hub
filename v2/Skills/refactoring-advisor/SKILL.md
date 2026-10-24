---
name: refactoring-advisor
description: "Use when identifying and prioritizing safe refactoring opportunities."
---

## When to Use
Use for code-quality review, technical-debt triage, or a behavior-preserving cleanup plan. Do not refactor by default when user requests analysis only.

## Required Inputs
Require target paths/scope, current behavior and known pain, constraints, tests/coverage, change-risk tolerance, performance or maintenance evidence, and permission to edit. Inspect current implementation and repository-specific conventions.

## Procedure
1. Read requested code plus direct callers/tests; establish behavior and observable seams.
2. Describe concrete smells with path and symbol/line evidence, not style preferences. Trace duplication, state ownership, coupling, branching, error handling or change propagation.
3. Prioritize by user impact, frequency/evidence, risk and effort; use qualitative labels unless project-defined metrics support numbers.
4. Recommend behavior-preserving transformations in small sequence, with characterization tests first where behavior is implicit. Show before/after for the highest-value change only if source supports it.
5. If authorized to edit, perform one reversible step at a time, run focused regression tests and inspect diff; stop on behavior ambiguity.

## Output Contract
Return: **Scope**; **Findings** table (path/symbol, evidence, impact, risk); **Prioritized actions** with rationale; **Safe sequence**; **Tests needed**; **Changes and verification** if edits authorized. Provide a short before/after illustration for a specific inspected case, not a generic invented code sample.

## Quality Gate
Every finding is evidence-based and actionable; avoid arbitrary thresholds such as “too many lines” without repository context. Separate readability preference from correctness/performance risk. Preserve behavior and public contracts; never assert a performance improvement without profiling. If tests are absent, identify the unguarded behavior and propose checks before broad rewrite.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
