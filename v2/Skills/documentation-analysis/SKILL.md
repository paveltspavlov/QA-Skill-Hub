---
name: documentation-analysis
description: "Use when auditing documentation for accuracy, coverage, and actionable gaps."
---

## When to Use
Use to review project docs, API references, migration notes, onboarding guides, or compare documentation to source behavior.

## Required Inputs
Require document paths/version, intended audience, scope/questions, source-of-truth code/config/spec, release/version context, and desired output format. Identify whether review includes external links, generated docs, or only repository content.

## Procedure
1. Read relevant docs and inspect their linked code, config, API spec, and tests; establish the source-of-truth and version.
2. Extract concrete claims, steps, prerequisites, examples, names, and promised behavior.
3. Verify each material claim against current repository evidence or official version-matched docs; mark unsupported claims instead of assuming.
4. Find omissions that would block the stated audience/task, contradictory instructions, stale paths/versions, and examples that fail under the documented setup.
5. If edits are requested, make minimal targeted changes, preserve authoritative generated content, then run doc lint/build/link/example checks that exist.

## Output Contract
Return: **Scope/source versions**; **Findings table** (severity, document location, claim or gap, evidence, recommended correction); **Coverage checklist** for the requested task; **Edits made** if authorized; **Verification** (exact checks). Cite paths/anchors and nearby lines where available.

## Quality Gate
Every finding points to an actual passage or task-critical omission and a checkable source; separate factual errors from style suggestions. Do not infer intended behavior from prose alone when code contradicts it. Confirm links/examples where tools allow; label unverified external or version-specific details. Do not fabricate missing sections, citations, or build results.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
