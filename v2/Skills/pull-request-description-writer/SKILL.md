---
name: pull-request-description-writer
description: "Use when drafting a PR description from actual changes and validation."
---

## When to Use
Use to describe a branch diff for review or draft a PR body. Do not create/open a PR unless specifically authorized; never imply CI passed from local checks.

## Required Inputs
Require base/head or actual diff, issue/acceptance criteria, PR template and repository conventions, intended reviewers/audience, deployment/migration risk, and verified test output. Inspect changes and tests directly; identify generated or out-of-scope files.

## Procedure
1. Compare base to head and map changes to requested behavior; verify title/template and links from repository, not guesses.
2. Separate shipped behavior from follow-up work.
3. Record tests/checks exactly as observed (command, result); distinguish local runs, CI status, and not-run items.
4. Surface migration, rollout, feature-flag, compatibility, privacy/security or data-loss risks and rollback plan only when relevant/evidenced.
5. Write for a reviewer: what changed, why, how to validate, and what needs attention. Check every statement against diff or supplied evidence.

## Output Contract
Return PR body with exact fields: **Summary**; **Motivation/issue**; **Changes**; **Validation** (run/result and not run); **Risk and rollout/rollback**; **Reviewer notes**; **Screenshots** only if relevant/provided. Worked example: `Summary: Adds invite-token expiry validation. Changes: rejects expired tokens before membership creation. Validation: <exact test command/result>. Risk: existing expired invites now require reissue.` Fill only verified details; omit unavailable fields or mark unknown per template.

## Quality Gate
No generic “tests pass” claim without output; no undocumented behavior or mismatched screenshots. Include all template-required sections and accurately identify migrations/breaking changes. A PR description is not a review approval. If base/head is unavailable, state scope limitation and qualify draft; do not claim the diff is fully assessed.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
