---
name: git-workflow-automator
description: "Use when designing or changing Git, CI, hook, and release conventions."
---

## When to Use
Use for a requested branching strategy, repository hooks, CI workflow, PR template or release policy. Do not push, tag, alter remote protection, or enable automation without explicit authorization.

## Required Inputs
Require provider and repo settings, team/release cadence, protected branches, review and approval rules, CI platform, build/test/deploy stages, permissions/secrets model, compliance constraints, and desired artifacts. Inspect existing workflows and repository settings when accessible.

## Procedure
1. Inventory current branch, CI, release scripts, hooks, templates and permissions. Separate local files from remote settings that are not visible.
2. Clarify workflow goals and failure/recovery expectations; choose trunk-based, GitFlow or another policy only from requirements.
3. Design minimal workflow files with least-privilege token permissions, pinned/verified actions or tools per project policy, explicit triggers, concurrency/cancellation and protected deployment gates as appropriate. Never place credentials in source.
4. Document branch lifecycle, review, failed checks, release/tag ownership and rollback. Generate hooks/templates only if requested.
5. Run YAML/schema lint, local dry-run or CI validation available; inspect permission scope and test condition logic. Apply remote changes only after explicit approval, then read back settings if tool access permits.

## Output Contract
Return: **Policy goals/assumptions**; **Branch/release diagram or table**; **Workflow/hook/template files**; **Permission/secrets map**; **Failure/recovery path**; **Validation results**; **Remote actions not performed/authorized**.

## Quality Gate
Triggers and permissions enforce rather than assume policy; workflows cannot deploy from untrusted events with secrets. No made-up branch protection, team size, or platform behavior. Distinguish proposed policy, committed YAML, and actual remote settings. Verify third-party workflow/action syntax in official docs matching versions; no push/tag or remote mutation without approval.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
