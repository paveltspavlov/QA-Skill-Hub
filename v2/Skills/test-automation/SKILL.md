---
name: test-automation
description: "Design, implement, or improve automated tests using the repository’s existing framework. Use for unit, integration, UI, and end-to-end automation."
---

# Test Automation

## When to Use
Use when authoring, repairing, or refactoring automated tests in an existing project, from unit and service tests through browser/system tests. Also use when reviewing a change set to identify which existing tests should be updated or which focused regression tests are missing. For high-level suite architecture, define boundaries before generating many tests.

## Required Inputs
Inspect production code/requirements, test directory, runtime and framework versions, fixtures/mocks, dependency boundaries, exact test/lint commands, CI expectations, and conventions. For change-driven work, obtain the supplied diff or changed-file list and map behavior changes to existing tests before editing. Obtain real expected behavior from source requirements or implementation contracts. Ask if language/framework or target behavior cannot be established.

## Procedure
1. For a change set, inspect changed files/diff; exclude generated or vendored content, map each behavior change to existing tests, and identify gaps. Do not create tests for modified lines without an observable behavior change.
2. Choose the smallest test level that observes the intended contract. Reuse project conventions and colocate tests consistently. Use Arrange–Act–Assert or the project's equivalent with descriptive names.
3. Derive cases from behavior: successful path, invalid/missing input, boundaries and branches, dependency failure, state changes, and regression. Do not force every category if irrelevant.
4. Mock external boundaries, not the behavior under test. Prefer deterministic fixtures/factories, isolated data, injected clocks/randomness where needed, explicit cleanup, and no network dependence unless an integration test is intended.
5. Assert meaningful outcomes (returned value, state, user-visible behavior, emitted event) rather than implementation trivia. For browser tests, prefer role/name/label locators; avoid fixed sleeps and selectors coupled to incidental DOM.
6. Keep tests independent and minimize shared mutable state. Ensure async work is awaited, failures expose context, and sensitive values are not printed.
7. Run the narrow test, then relevant suite/lint when feasible. Report exact commands, exit/result, skipped tests, and environment limitations; don't imply newly generated tests passed unless run.

## Output Contract
Deliver a changed-behavior map `Changed file/behavior | Existing test | Gap | Added/updated test | Requirement/oracle`; include test file(s) or case matrix `Test ID | Requirement/source | Scenario | Setup/data | Action | Expected oracle | Isolation/cleanup`. Explain mocks/fixtures and file placement. Report `Command | Result (PASS/FAIL/BLOCKED/NOT RUN) | Evidence | Follow-up`. Example: `test_rejects_expired_token | auth contract §2 | expired token | fixed clock + signed fixture | call handler | unauthorized response, no write | isolated fake repository`.

## Quality Gate
Tests compile and follow the project's API; each assertion comes from defined behavior; success/failure/boundary cases match risk; fixture cleanup and isolation are explicit; no brittle timing or unrelated mocks; the narrow test is actually exercised or marked not run. Do not alter production code unless requested.

## Evidence and Uncertainty
Use source code, requirements, existing tests, framework docs for the installed version, and actual runner output. Flag missing oracle or environment as unresolved. Evidence readiness requires four supported checks—clear scope, claim traceability, complete output, relevant verification—25 points each; below 75/100, ask, qualify, or abstain. No invented confidence percentages. Critical safety, privacy, authorization, or acceptance failures block readiness.
