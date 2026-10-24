---
name: test-oracle-creator
description: "Define evidence-based expected results and pass/fail criteria from requirements and business rules. Use when test cases lack a clear oracle."
---

# Test Oracle Creator

## When to Use
Use when a test scenario exists but expected results, tolerances, state changes, or pass/fail logic are unclear. This skill translates an authoritative rule into observable evidence; it does not invent product behavior or business values.

## Required Inputs
Request requirement/business-rule source and version, scenario steps and inputs, relevant data model/state, exact calculations/rounding, API/UI contract, side effects, error semantics, and owners for unresolved decisions. For qualitative outputs, obtain evaluator rubric and acceptable variation. Ask before defining a consequential threshold.

## Procedure
1. Extract rules with source line/ID and conditions; classify outcome type: exact value, set/enum, range, pattern/schema, state/side effect, invariant, or human rubric.
2. Derive expected result step by step. For calculations, show formula, order, rounding, units, and boundary treatment exactly as stated. Recompute only from known rules; no hidden assumptions.
3. Define evidence method per outcome: assertion/query/event/log/screenshot or blinded human evaluation. Distinguish system output from downstream state and avoid checking only presentation when persistence matters.
4. Address valid, invalid, boundary, missing, conflicting, retry, and state-dependent cases only where rules support them. Specify tolerance from source, not habit. For nondeterministic/AI behavior, use a rubric with criteria, examples, adjudication, and agreed thresholds; do not claim deterministic exact-match unless warranted.
5. Turn undefined or contradictory rules into prioritized questions. Mark affected oracle `Needs Decision`; do not disguise uncertainty with a provisional expected value.

## Output Contract
Use `Test Oracle: <scenario>` and table `Rule/source | Inputs/precondition | Step | Expected result | Evidence method | Pass/fail rule | Status (Defined/Needs Decision)`. Add `End-to-end invariants`, `Unresolved decisions`, `Assumptions explicitly approved`. Sample: supplied rule “base $100; 10% discount; round to cents” ⇒ `$100 × (1−0.10) = $90.00`; assert exact amount only if rounding/currency semantics confirm cents. No financial amount in this sample is a user-specific expected result.

## Quality Gate
Each oracle traces to a rule; arithmetic/units are independently checked; state and side effects are included; pass/fail is binary or rubric-defined and reproducible; tolerances are source-backed; gaps are visible. Never fabricate expected values to complete a table.

## Evidence and Uncertainty
Cite the rule, data, code, and observed verification; label calculation assumptions and human judgment separately. Apply four readiness checks—scope clear, claims traceable, contract complete, relevant verification—25 points each. Below 75/100, ask, qualify, or abstain. No guessed confidence percentages. Critical safety, privacy, authorization, or acceptance failures block readiness regardless of score.
