---
name: e2e-test-architecture
description: "Architect maintainable end-to-end test suites from critical user journeys. Use when defining browser flows, fixtures, data, and CI execution."
---

# E2E Test Architecture

## When to Use
Use when designing a browser/system-level suite from user journeys, selecting stable test boundaries, planning fixtures and test data, or migrating an unreliable E2E suite. Do not use E2E tests as a substitute for unit or API contract coverage.

## Required Inputs
Request journeys and acceptance criteria with source IDs; application/framework and existing test runner; user roles and auth constraints; environment URLs/configuration; data setup/cleanup options; external dependency strategy; browser/device scope; CI runtime and parallelism constraints; and reporting needs. Inspect repository conventions before proposing file layout or selectors.

## Procedure
1. Break journeys into observable steps, success/error states, business impact, and downstream side effects. Prioritize a small critical path set and map lower-level checks to unit/API tests.
2. Design architecture around domain-level page/component helpers, readable specs, fixtures, and explicit lifecycle. Prefer user-facing role/name/label locators; use stable test IDs only where semantics do not provide a suitable contract. Avoid brittle CSS/XPath and hidden selector chains.
3. Specify deterministic state: isolated accounts/records per worker or test, API/database seeding only through authorized test interfaces, unique run identifiers, cleanup even on failure, and reset strategy. Never rely on test ordering or shared mutable accounts.
4. Define authentication/session handling consistent with the runner's documented model, secrets management, and account isolation. Stub external systems only when the purpose is not integration validation; identify what stubbing excludes.
5. Plan resilience: assert conditions rather than arbitrary sleeps, control clocks/network where needed, capture traces/screenshots on failure without sensitive data, and retry only to diagnose—not mask—flakiness.
6. Design CI shards, browser coverage, tags, artifacts, and cleanup. Verify runner APIs and configuration in the selected framework's official documentation.

## Output Contract
Produce `E2E Architecture: <feature>` with: journey-to-requirement table `Journey ID | Requirement | Steps | Risk | Observable oracle | Test level`; file tree; fixture/data/auth strategy; locator policy; CI/execution plan; risks and unverified scope. Sample row: `J-02 | AC-4 | sign in → create draft → submit | High | confirmation state plus persisted record via test API | E2E submit; API persistence check`—expected behavior must come from AC-4, not assumption.

## Quality Gate
Each critical journey has traceability and an observable oracle; tests are independent, deterministic, clean up data, and avoid production side effects; secrets are not embedded; retries do not conceal instability; each abstraction earns its maintenance cost; framework-specific code is checked against official docs.

## Evidence and Uncertainty
Ground journeys in requirements, repository code/config, test data interfaces, and actual run artifacts. Separate proposed design from tests executed and pass/fail observations. Use the evidence-readiness gate: scope, claim traceability, output completeness, and relevant verification each need observable support (25 points); below 75/100, ask, qualify, or abstain. Never guess confidence percentages. Critical authorization, privacy, safety, or acceptance failures cannot be averaged away.
