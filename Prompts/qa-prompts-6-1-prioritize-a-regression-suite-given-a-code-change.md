---
id: qa-prompts-6-1-prioritize-a-regression-suite-given-a-code-change
name: "6.1 - Prioritize a Regression Suite Given a Code Change"
folder: prompts
section: qa-prompts
summary: "Regression & Coverage"
tags:
  - "qa-prompts"
  - "regression & coverage"
---

# Prompt 6.1 - Prioritize a Regression Suite Given a Code Change

> Category: **Regression & Coverage**

When to use  Before any release when you need to select a subset of the regression suite to run given time constraints. Produces a defensible, risk-based priority list.

Expected output  A prioritized regression run order with risk rationale, organized into must-run, should-run, and safe-to-defer buckets.

Prompt

```
**Role:** You are a QA lead with expertise in risk-based testing and regression 

strategy. You prioritize test suites based on the principle that tests closely 

related to changed code are highest priority, followed by tests for features with 

high business impact.

**Context:** [SYSTEM DESCRIPTION]. The system has the following module/service 

dependencies that are relevant to this change: [DESCRIBE KEY DEPENDENCIES].

**Instruction:** Given the code changes described below and the regression test suite 

listed, produce a prioritized regression run plan. Use this risk logic:

- MUST RUN: Tests directly covering changed code, adjacent integration points, 

  and smoke tests for critical user journeys

- SHOULD RUN: Tests for features with shared dependencies on changed modules

- SAFE TO DEFER: Tests for completely unrelated features with no shared dependencies

For each MUST RUN test, provide a one-sentence justification.

**Input:**

Code changes in this release:

[DESCRIBE CHANGES - include: what changed, why, which modules/services were touched]

Full regression test suite:

[PASTE LIST OF TEST CASES - titles are sufficient if detailed specs are not available]

Available testing time: [X hours]

Estimated time per test: [X minutes average, or provide per-test if known]

**Constraints:**

- Do not include tests you have no information to prioritize - flag them as 

  [NEEDS ANALYSIS] if you can't assess their relevance

- Consider shared dependencies and integration points, not just direct coverage

- Provide a total estimated time for each bucket (MUST RUN / SHOULD RUN / DEFER)

- Flag any test that should be run first as a smoke test (critical path validation)

**Output Format:**

## Regression Run Plan - [RELEASE NAME]

**Risk basis:** [1-2 sentence summary of what drove the prioritization]

### 🔴 MUST RUN ([X tests, ~X hours])

| # | Test Name | Justification |

|---|---|---|

### 🟡 SHOULD RUN if time allows ([X tests, ~X hours])

| # | Test Name | Dependency |

|---|---|---|

### 🟢 SAFE TO DEFER ([X tests])

[Test names only, no table needed]

### ⚪ NEEDS ANALYSIS ([X tests])

[Tests you couldn't assess - recommend manual triage]

**Recommended smoke test sequence (first 30 min):**

[Ordered list of 5-8 critical path tests to run first]
```
