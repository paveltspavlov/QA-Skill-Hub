---
name: debugging
description: "Use when diagnosing a reproducible software failure before changing code."
---

## When to Use
Use for errors, regressions, failing tests, hangs, unexpected output, or production incidents when investigation and cause isolation are needed.

## Required Inputs
Require exact symptom and expected behavior, reproduction steps, environment/version, relevant logs/stack trace, recent changes, failing inputs, and safe access to affected code. Redact credentials and personal data. For production impact, include blast radius and safe mitigation authority.

## Procedure
1. Preserve the original failure; reproduce with the smallest safe test and record exact command/input/output.
2. Trace from symptom to failing boundary through stack trace, logs, code path, configuration, and recent diff. Distinguish observed facts from hypotheses.
3. Form one falsifiable hypothesis at a time; run a targeted probe or regression test that can confirm or reject it. Inspect relevant official docs/repo code for version-specific behavior.
4. Identify root cause, not just the first failing line. Make the narrowest fix, add a regression test, and check nearby paths. Avoid destructive cleanup or production changes without authorization.
5. Run the repro plus focused suite; use broader checks when scope warrants and report unrun checks.

## Output Contract
Return: **Symptom and expected behavior**; **Reproduction** (environment, command, input); **Evidence/timeline**; **Hypotheses tested**; **Root cause** or “not isolated”; **Fix and regression test**; **Verification and remaining risk**.

## Quality Gate
A root-cause claim is supported by a test/probe or direct code evidence that distinguishes it from competing hypotheses. Fix reproduces the original failure before and success after when feasible. Logs do not expose secrets. If unable to reproduce, present a ranked investigation path—not a fabricated diagnosis. Report exact observations and avoid implying broader validation than performed.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
