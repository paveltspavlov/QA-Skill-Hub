---
id: qa-prompts-2-5-generate-risk-based-test-priorities
name: "2.5 - Generate Risk-Based Test Priorities"
folder: prompts
section: qa-prompts
summary: "Test Case Design"
tags:
  - "qa-prompts"
  - "test case design"
---

# Prompt 2.5 - Generate Risk-Based Test Priorities

> Category: **Test Case Design**

When to use  During sprint planning or release preparation when time is limited and you need a defensible, documented rationale for which tests to focus on.

Expected output  A risk-scored, prioritized test list with rationale, suitable for sharing with a release manager or stakeholder.

Prompt

```
**Role:** You are a QA lead responsible for risk-based test planning. You assess 

testing priorities based on probability of failure and impact of failure, and you 

communicate your reasoning clearly to non-technical stakeholders.

**Context:** [SYSTEM DESCRIPTION]. The upcoming release includes these changes:

[DESCRIBE THE CODE CHANGES, NEW FEATURES, OR BUG FIXES IN THIS RELEASE]

Available testing time: [X hours / X sprint days].

**Instruction:** Review the test cases or test areas listed below. 

Prioritize them using a risk-based approach:

Risk = Probability of Failure × Impact of Failure

Factors that increase probability of failure:

- Changed or new code in this area

- Complex logic

- Recent bug history

- Integration points with other systems

Factors that increase impact:

- Core user journeys

- Revenue-affecting features

- Data integrity

- Security or compliance

**Input:**

Test cases or test areas:

[PASTE LIST OF TEST CASES OR TEST AREAS]

**Constraints:**

- Assign each item a Risk Rating: CRITICAL / HIGH / MEDIUM / LOW

- Provide a one-sentence justification for each rating

- Identify the top 20% that should always run regardless of time constraints (the 

  "smoke + risk-critical" set)

- Identify the bottom 20% that are safe to defer if time runs out

- Do not factor in test execution time - focus purely on risk

**Output Format:**

## Risk-Based Test Priority Report

**Release:** [RELEASE NAME/DATE]

**Prepared by:** QA | **Date:** [DATE]

| Priority Rank | Test Case/Area | Risk Rating | Justification | Run Group |

|---|---|---|---|---|

[CRITICAL items first, then HIGH, MEDIUM, LOW]

**Must-Run Set (top 20%):** [List test IDs]

**Safe-to-Defer Set (bottom 20%):** [List test IDs]

**Risk Assumptions:** [Note any assumptions made about the code changes]
```
