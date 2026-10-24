---
name: form-builder
description: "Use when building a form from explicit fields, constraints, and submission behavior."
---

## When to Use
Use for data-entry, settings, signup, checkout, or multi-step workflows. Do not impose a form library or wizard threshold without project evidence.

## Required Inputs
Require field names/labels/types, requiredness, validation rules and source, conditional dependencies, defaults, submission endpoint/payload, server errors, success/cancel behavior, form library/design system, accessibility/browser requirements, and test conventions.

## Procedure
1. Inspect existing form components, field primitives, validation schema, API contract and installed library versions.
2. Map field → label/help/error, type, constraints, visibility dependencies and payload mapping; resolve client/server mismatch rather than guessing rules.
3. Implement schema and UI using project conventions. Keep validation understandable; preserve user input on recoverable server errors, disable/guard duplicate submission appropriately, and expose loading/success/failure states. For multi-step flow, define progress, back navigation, state persistence and per-step/final validation.
4. Ensure labels, descriptions, field error associations, keyboard/focus behavior, group semantics and status announcements; do not rely only on color.
5. Test required/optional, valid/invalid/boundary, conditional, server failure, submit duplication and navigation; run type/lint and accessibility checks available.

## Output Contract
Return: **Field/validation matrix**; **Form component/schema**; **Payload mapping**; **Interaction and error states**; **Files changed**; **Tests and checks**. If constraints are unknown, list blocking questions and offer a provisional skeleton without asserting validation correctness.

## Quality Gate
UI constraints align with backend/domain rules and avoid silently truncating/transforming user input. Accessible labels and errors are programmatically related. Conditional visibility does not accidentally submit stale hidden values unless contract requires it. Verify library behavior against installed docs; report manual assistive-technology checks separately from automated tests.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
