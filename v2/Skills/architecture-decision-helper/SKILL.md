---
name: architecture-decision-helper
description: "Use when a technical decision needs explicit options, trade-offs, and consequences."
---

## When to Use
Use for architecture boundaries, technology choices, deployment patterns, data ownership, or significant design alternatives. Do not turn an unresolved preference into a factual recommendation.

## Required Inputs
Require the decision question, current system and constraints, goals/non-goals, stakeholders/operational ownership, decision timing, and known evidence (traffic, costs, failure modes, skills). Ask for priorities where rankings change the outcome; distinguish measured values from estimates.

## Procedure
1. Reframe the decision as a question and list constraints, unknowns, and reversible choices.
2. Include the current/least-change option and at least one feasible alternative; discard options only with a reason.
3. Compare on criteria relevant to the case—fit, operational burden, security, performance evidence, cost drivers, migration/rollback, team capability, and reversibility. Score only if user-provided weights and defensible evidence exist; otherwise use qualitative trade-offs.
4. State recommendation conditionally, assumptions, risks, consequences, and signals that would change it.
5. Include rollout/migration steps and review triggers when changing an existing system. Cite repo paths or official docs for consequential technical claims.

## Output Contract
Deliver an ADR with exact fields: **Title**, **Status** (proposed/accepted only if known), **Date/decision owner** (unknown if absent), **Context**, **Constraints**, **Options considered** (benefits, costs, risks), **Decision and rationale**, **Consequences**, **Rollout/rollback**, **Evidence and assumptions**, **Revisit triggers**. Add a decision matrix only with explicit criteria.

## Quality Gate
At least one credible alternative and status quo are considered. Recommendation follows stated priorities, does not invent SLOs, benchmark results, costs, or team skills, and makes uncertainty visible. Separate evidence-backed consequences from forecast. Verify platform/library claims against repository and version-matched official docs; label untested performance claims as hypotheses.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
