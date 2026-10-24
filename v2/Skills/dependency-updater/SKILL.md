---
name: dependency-updater
description: "Use when updating a dependency with compatibility and lockfile checks."
---

## When to Use
Use for a requested package update, supported-range refresh, or dependency security/maintenance change. Never update every dependency as an implicit side effect.

## Required Inputs
Require package/manager and manifest path, package(s) and target range/version if specified, runtime/platform constraints, release policy, lockfile(s), build/test command, and whether transitive updates are in scope. Inspect installed version, semver constraints, peer dependencies, official release notes/changelog and advisories where relevant.

## Procedure
1. Identify the package manager from repository lockfiles and use its existing commands; inspect clean/dirty status.
2. Read official changelog/migration notes for the precise from/to versions and validate registry metadata; separate stable, prerelease and unsupported targets.
3. Check breaking changes, runtime/peer constraints, install scripts, native modules, license/security facts as relevant. Propose a major upgrade plan if migration risk is material; do not silently broaden scope.
4. Update only requested manifest/lockfile and necessary compatibility code. Never hand-edit generated lock metadata.
5. Run manager consistency check, tests/type/build/security checks relevant to change; inspect actual resolved versions and diff.

## Output Contract
Return: **Package/from/to**; **Source basis** (official release notes/version metadata); **Compatibility findings**; **Manifest/lockfile changes**; **Migration actions**; **Commands and results**; **Remaining risk**. If no target was specified, recommend a verified compatible range rather than silently selecting “latest.”

## Quality Gate
Resolved lockfile matches the declared intent and only intended packages change. Breaking changes and transitive shifts are disclosed; do not claim an advisory is fixed without confirming affected range and resolution. Installation and tests are not equivalent—report both separately. Do not invent version support or use stale release notes; pin claims to current official sources and repository state.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
