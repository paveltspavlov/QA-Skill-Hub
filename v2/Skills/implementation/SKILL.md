---
name: implementation
description: "Use when making a scoped code or configuration change in an existing repository."
---

## When to Use
Use when a concrete feature, bug fix, or maintenance task is requested and implementation is authorized. This is not a substitute for an architecture decision when core behavior is unresolved.

## Required Inputs
Need desired behavior and acceptance criteria, repository root/target paths, constraints, known repro for bugs, compatibility/security requirements, and permission boundaries. Discover actual language, framework, test commands and repository guidance before edits; ask if missing context could change behavior.

## Procedure
1. Read repository instructions, relevant code/tests/config and recent history only as needed; establish current behavior and working-tree changes so unrelated work remains untouched.
2. Turn request into observable acceptance checks. Trace each to an existing component or proposed file; identify open questions and blockers.
3. Implement the smallest cohesive change in local conventions. Preserve public contracts unless explicitly changing them; do not alter unrelated files, profiles, manifests, generated artifacts, or external state.
4. Add or update tests for acceptance and failure/boundary behavior. Avoid weakening tests to get a pass.
5. Run targeted tests and relevant lint/type/build checks that exist; inspect diff and working-tree status, confirm only scoped changes, and report any unrun check.

## Output Contract
Return: **Change summary**; **Files changed**; **Behavior/acceptance mapping**; **Tests/checks actually run and results**; **Assumptions or unresolved items**. Include patch/code only where useful; if blocked, give the exact missing decision and safe partial work.

## Quality Gate
Every acceptance criterion maps to implementation or explicit non-delivery. Existing user changes are preserved. No unrequested cleanup, unsafe fallback, fabricated dependency, or silent API change. Tests correspond to behavior and were executed when available; otherwise label as unverified. Review the diff for generated noise and secrets.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
