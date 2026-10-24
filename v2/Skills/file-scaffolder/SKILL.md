---
name: file-scaffolder
description: "Use when creating a small, conventional set of project files from explicit requirements."
---

## When to Use
Use for a new module, component, service, feature folder, or test/doc scaffold when the repository already defines conventions. Do not scaffold an entire application without an agreed structure.

## Required Inputs
Require purpose, exact target directory/name, language/framework, expected files and responsibilities, export/import policy, dependency constraints, generation/template command if any, and overwrite policy. Inspect repo structure, instructions, adjacent examples and ignore rules.

## Procedure
1. Inventory existing files and templates; detect name collisions and uncommitted edits.
2. Derive the minimal file tree from nearby patterns and requested behavior; distinguish required files from optional tests/docs/config. Ask before replacing existing files or introducing dependencies.
3. Create files with accurate imports, types, error paths and TODOs only for genuinely unspecified behavior; no placeholder functions that appear complete.
4. Update barrel/config/registration files only when required by repository conventions; avoid duplicate registrations.
5. Run formatter, type/lint checks and focused tests; check imports resolve and list created files.

## Output Contract
Return: **Purpose**; **File tree** with each path and role; **Files created/modified**; **Conventions followed/deviations**; **Verification**. A compact example tree may look like `feature/{index,service,service.test}.ts` only when those names match repository patterns.

## Quality Gate
Do not overwrite, create near-duplicate, or generate files outside the approved scope. No invented API, package, export convention, or test runner. All imports resolve; scaffold compiles or incomplete placeholders are clearly marked. Confirm the final diff contains only intended files and no secrets or environment-specific paths.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
