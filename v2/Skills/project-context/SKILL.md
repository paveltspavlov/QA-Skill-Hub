---
name: project-context
description: "Use when building a concise, evidence-linked map of an unfamiliar repository, or when deciding where project context belongs. Inspect `.copilot/` and `.vscode/` when present; follow the convention already used by the repository and avoid duplicate or conflicting context files."
---

## When to Use
Use before a substantial code task when architecture, entry points, conventions, or tests are unclear; refresh stale context after structural changes. Do not substitute assumptions for source inspection.

## Required Inputs
Require repository root, task/domain focus, target branches or working-tree scope, any onboarding docs, and desired context size. Use only accessible files and respect secrets, generated files, vendored code, and user modifications.

## Procedure
1. Read repo guidance and inventory top-level structure, package/build manifests, entry points, tests, config, and README/design docs relevant to task.
2. Trace one or two concrete execution paths from entry point through modules, data/API boundaries and test coverage; avoid exhaustive codebase summaries.
3. Record languages/frameworks and versions from manifests, scripts and lockfiles, distinguishing declared vs installed.
4. Map conventions, critical files, commands and dependencies with paths; verify commands from project config rather than guessing.
5. Note gaps, contradictions, stale docs, untested flows and uninspected areas. Re-check any map used for consequential change against current file contents.

## Output Contract
Return: **Repository identity/branch/status**; **Task scope**; **Stack/version evidence**; **Relevant file map** (path and role); **Execution/data flow**; **Conventions**; **Available checks** (command source); **Unknown/uninspected areas**. Cite paths and line/symbol names where practical; keep unrelated modules out.

## Quality Gate
All claims trace to inspected files or command output; do not infer deployment topology or runtime state from a package manifest. Preserve current user changes and never expose secret values. A context map is a navigation aid, not proof that all code was audited. State inspection limits and revalidate before implementation.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
