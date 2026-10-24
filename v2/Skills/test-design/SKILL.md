---
name: test-design
description: "Design traceable functional and non-functional test cases from requirements, interfaces, or risks. Use before implementation, during review, or when coverage is unclear."
---

# Test Design

## When to Use
Use to derive manual or automated test cases from a feature, user story, business rule, API contract, state model, or risk. Choose techniques that fit the test basis rather than mechanically applying every method.

## Required Inputs
Collect requirement IDs/text and version, scope, actors/roles, preconditions, data types/ranges, business rules, interface/state behavior, environment, target test level, risk priorities, and any defined severity/priority scale. Identify missing expected behavior and ask the owner when the gap affects pass/fail.

## Procedure
1. Extract test conditions and observable outcomes; preserve traceability to exact source IDs/locations. Separate explicit requirement from contextual inference.
2. Select techniques: equivalence partitioning for classes expected to behave alike; boundary value analysis for ordered ranges; decision tables for combinations of conditions; state-transition tables for valid/invalid transitions; use-case testing for user workflows; experience-based cases for risks not captured in the spec.
3. Derive positive, negative, boundary, error, and interaction scenarios where relevant. For ranges, use actual declared limits; do not invent boundaries. For stateful flows, enumerate states, events, guards, and outcomes from source rules.
4. Specify preconditions, exact steps/data, expected result per step, postcondition, priority/risk rationale, and test environment. If expected behavior is unspecified or contradictory, leave it open and formulate a question rather than fabricate an oracle.
5. Review for duplicate cases, untested partitions/transitions/condition combinations, infeasible setup, and unobservable expected results. Summarize requirement coverage by mapped IDs, not a guessed percentage.

## Output Contract
Use table `Req ID/source | TC ID | Priority/rationale | Technique | Preconditions | Steps | Data | Expected result | Postcondition | Status (Ready/Needs Oracle/Blocked)`. Add `Coverage gaps`, `Questions`, and technique rationale. Example for rule “quantity 1–10 inclusive”: EP valid 1–10 / invalid <1 and >10; BVA cases 0,1,2,9,10,11, with expected outcomes taken from the rule. If the source does not specify handling of 0 or 11, mark expected outcome for confirmation.

## Quality Gate
Every test maps to source; data actually exercises its stated partition; oracle is observable and step-specific; test cases aren't redundant without reason; missing or contradictory rules are flagged; priorities use the team's scale or stated rationale. Verify the table covers all supplied requirements before claiming full mapping.

## Evidence and Uncertainty
Trace tests to user-provided requirements, schemas, designs, or code; mark assumptions and ask when they alter expected outcomes. Apply four evidence checks—scope clear, claims traceable, output complete, relevant verification performed or disclosed—25 points each. Below 75/100, ask, qualify, or abstain; never guess confidence percentages. Critical privacy, authorization, safety, or acceptance failures cannot be averaged away.
