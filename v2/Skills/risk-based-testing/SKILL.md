---
name: risk-based-testing
description: "Prioritize testing by product risk, change impact, likelihood, exposure, and available time. Use for regression planning, release decisions, and constrained test windows."
---

# Risk-Based Testing

## When to Use
Use to prioritize regression, release validation, exploratory effort, or a constrained test window based on product and change risk. It supports decisions; it does not by itself certify release readiness or quantify probability.

## Required Inputs
Clarify release/change scope, decision owner and deadline, available test capacity, affected users/workflows/data, architecture/dependencies, recent changes and defects, usage/exposure evidence, severity definitions, existing tests/runtime, and acceptance criteria. If likelihood or impact scale is not defined, agree a qualitative scale before ranking.

## Procedure
1. Identify credible failure conditions from changed code, requirements, integrations, operational history, and user context. Separate known defects from potential risks.
2. Score each risk using the agreed impact and likelihood/exposure scale, with definitions and evidence. Use qualitative `Low/Medium/High` only when scales are explicitly explained; avoid arbitrary multiplication or percentages.
3. Map risks to mitigations/tests: scenario, level, oracle, data/environment, owner, execution cost, and evidence needed. Prefer checks that reduce high-impact uncertainty efficiently; account for dependency/order constraints.
4. Rank by rationale, not a bare score. Include security/privacy/safety and data-loss concerns as explicit risks. Define release gate or escalation only from authorized policy.
5. Make the time trade-off explicit: prioritized tests, deferred tests, rationale, residual risk, and a trigger to resume deferred work. Reprioritize when new evidence arrives.
6. During execution, update risk state with results and preserve failed/unrun distinctions. Do not treat test coverage percentages as risk reduction by themselves.

## Output Contract
Return a risk register `Risk ID | Failure condition | Affected asset/users | Impact | Likelihood/exposure | Evidence | Rating/rationale | Test/mitigation | Owner | Residual risk`; a business-path matrix `Path | Risk | Selected tier | Existing coverage | Gap`; and three selectable tiers. Smoke: release-blocking checks only. Core: high-risk critical paths and key error states. Full: all in-scope regression and risk-based exploration. For each tier list test IDs, dependencies, exit evidence, and duration only when the project supplied a basis. End with deferred scope, residual risks, and release caveats. Sample: `R-1 | migration drops populated field | customer data | high impact per owner scale | likelihood unquantified; schema diff present | migration test from supported prior state | High, rationale: irreversible data impact | backup+upgrade verification | DB owner | rollback unverified`.

## Quality Gate
Scales have definitions; evidence backs ratings; tests map to risks; costs and dependencies are considered; residual risks and deferred coverage are explicit; release decisions cite policy/owner and actual results. Critical risks cannot be averaged into a low aggregate score.

## Evidence and Uncertainty
Ground risk statements in requirements, change diffs, defects, usage, architecture, and test results. Label hypotheses and unknown likelihood. Apply four evidence checks—scope clarity, traceable material claims, complete deliverable, relevant verification—25 points each; below 75/100, ask, qualify, or abstain. Never guess confidence percentages. Critical safety, authorization, privacy, or acceptance failures block readiness regardless of score.
