---
name: migration-planner
description: "Use when planning a phased migration between systems, frameworks, or architectures."
---

## When to Use
Use for technology/framework/platform changes, legacy replacement, API transition, or staged coexistence. Use database-migration-generator for executable schema/data changes.

## Required Inputs
Require source and target versions/stacks, scope and inventory, constraints/deadline, users/traffic, deployment and rollback authority, coexistence limits, compatibility requirements, data/URL/auth concerns, team/operational capacity, acceptance criteria, and evidence for effort/risk estimates.

## Procedure
1. Establish current/target state and inventory dependencies, consumers, routes/data, and functionality in scope.
2. Identify compatibility breaks, traffic/SEO/auth/data-loss risks and unknowns; separate discovered facts from estimates.
3. Divide work into small phases with entry/exit checks, owner/sequence, coexistence or strangler plan, cutover criteria, observability and rollback for each phase. Avoid big-bang unless constraint justifies it.
4. Preserve feature delivery with incremental boundaries when possible; include parity and dual-read/write risks explicitly.
5. Estimate effort only as bounded ranges with stated assumptions and team basis; otherwise mark sizing unknown. Define rehearsals, backups and abort decision points.

## Output Contract
Return: **Current/target scope**; **Assumptions/dependencies**; **Risk register** (impact, likelihood basis, mitigation, owner); **Phase table** (deliverable, dependency, entry/exit criteria, validation, rollback); **Coexistence/cutover strategy**; **Effort ranges and basis or unknown**; **Decision gates**. Worked example: a UI migration can route one low-risk page to the new app, compare behavior/URLs, then expand; keep auth/session rollback explicit, do not assume shared session compatibility.

## Quality Gate
Plan preserves acceptance criteria and identifies data/identity/URL compatibility blockers before cutover. Every phase has a measurable exit condition and rollback trigger; rollback acknowledges irreversible effects. No fabricated dates, costs, throughput, SEO outcomes, or confidence. Verify relevant framework/platform migration facts against official source versions; qualify uncertain estimates.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
