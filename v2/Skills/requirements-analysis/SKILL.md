---
name: requirements-analysis
description: "Extract testable outcomes, rules, constraints, ambiguities, and traceability from requirements. Use for user stories, specifications, change requests, and acceptance criteria."
---

# Requirements Analysis

## When to Use
Use before implementation or test design to assess user stories, specifications, PBIs, change requests, UI descriptions, or acceptance criteria for clarity, completeness, consistency, and testability. Review what is supplied; do not silently add product behavior.

## Required Inputs
Collect source text and IDs/version, related flows/designs/contracts, actors and roles, domain rules, dependencies, non-functional constraints, target decision/readiness standard, and stakeholders who can resolve questions. Preserve original terminology and source locations. Missing context should remain explicit.

## Procedure
1. Extract actors, goals, triggers/preconditions, main/alternate/error flows, inputs/outputs, state changes, business constraints, permissions, dependencies, and non-functional needs.
2. Check each statement for ambiguity (“fast”, “appropriate”), incompleteness, conflict, unverifiable wording, missing boundary/error states, unclear ownership, and undefined units/conditions. Quote exact text and identify impact.
3. Rewrite criteria only as proposals: make actor, condition, observable outcome, and measurable bound explicit when agreed facts support them. Do not turn suggestions into accepted requirements.
4. Build source-to-test traceability. Identify coverage gaps for functional, usability/accessibility, performance, security, reliability, and data requirements when relevant; avoid claiming standards compliance from a checklist.
5. Ask prioritized questions whose answers change implementation, risk, or expected test outcome. Group as `Scope`, `Business rule`, `UI/flow`, `Data/integration`, `Non-functional`, `Acceptance`. Offer a readiness disposition based on unresolved blockers and state who must decide.

## Output Contract
Provide `Requirement summary`; table `ID | Source quote/location | Category | Issue or testable criterion | Impact | Proposed clarification/rewrite | Verification`; `Questions` ordered by decision impact; `Assumptions (unconfirmed)`; `Readiness: READY / NEEDS CLARIFICATION / BLOCKED` with rationale. Sample: `AC-2 | “loads quickly” line 4 | Non-functional | missing measurable timing and measurement context | cannot pass/fail | ask for percentile, device/network, and measurement window | instrumented test after owner defines target`.

## Quality Gate
Every source statement is traceable; facts and suggested rewrites are distinct; questions are specific and decision-relevant; acceptance criteria describe observable evidence; contradictions and missing cases are visible; “READY” is not used while material blockers remain.

## Evidence and Uncertainty
Use source text, linked designs/contracts, stakeholder decisions, and relevant authoritative standards only when applicable. Mark inferred requirements as proposals. Apply evidence readiness with four checks—scope clear, claims traceable, output complete, relevant verification available (25 points each). Below 75/100, ask, qualify, or abstain; no guessed confidence percentages. Critical privacy, authorization, safety, or acceptance failures block readiness regardless of score.
