---
id: qa-prompts-6-3-suggest-which-tests-to-skip-given-time-constraints-risk-based
name: "6.3 - Suggest Which Tests to Skip Given Time Constraints (Risk-Based)"
folder: prompts
section: qa-prompts
summary: "Regression & Coverage"
tags:
  - "qa-prompts"
  - "regression & coverage"
---

# Prompt 6.3 - Suggest Which Tests to Skip Given Time Constraints (Risk-Based)

> Category: **Regression & Coverage**

When to use  When you have a fixed deadline and a test suite that's too large to complete in full. Produces a documented, defensible deferral decision for stakeholder sign-off.

Expected output  A risk-based deferral recommendation with explicit assumptions, residual risk statement, and stakeholder sign-off template.

Prompt

```
**Role:** You are a QA lead responsible for release quality decisions. You make 

defensible, risk-based recommendations about which tests to defer when time is 

constrained, and you communicate the residual risk clearly to stakeholders.

**Context:** [SYSTEM DESCRIPTION]. 

Release date: [DATE]. 

Available testing time remaining: [X hours].

Total estimated test execution time: [Y hours].

**Instruction:** Given the test suite and time constraint below, recommend which tests 

to defer to the next release cycle. Your recommendation must:

1. Protect the critical user journeys (revenue-affecting, security-related, data integrity)

2. Ensure smoke/sanity tests are always included in the run set

3. Clearly state the residual risk of each deferral

4. Be presented in a format suitable for stakeholder sign-off

Use this deferral framework:

- NEVER defer: tests covering changed code, P1 user journeys, security, data integrity

- SAFE TO DEFER: tests for unchanged low-risk features, duplicate coverage, 

  cosmetic/usability tests

- CONDITIONAL DEFER: tests that could be deferred if a specific condition is met 

  (e.g., "defer if zero defects found in adjacent area during smoke test")

**Input:**

Test suite to decide on:

[PASTE TEST CASE LIST WITH ESTIMATED DURATIONS IF KNOWN]

Business context:

[DESCRIBE: which features are most business-critical, which were recently changed, 

any known high-risk areas, any customer-facing commitments]

**Constraints:**

- Explicitly state all assumptions (e.g., "Assuming no code changes to the payments 

  module since last full regression")

- Do not recommend deferring more than 40% of the suite without flagging it as 

  high risk

- Provide the residual risk for EVERY deferred test, not just a summary

- Include a stakeholder communication template

**Output Format:**

## Test Deferral Recommendation - [RELEASE NAME/DATE]

**Prepared by:** QA Lead | **Approved by:** [REQUIRES SIGN-OFF FROM: ______]

### Run Set (Proceed with these - [X tests, ~X hours])

[List]

### Deferred Tests ([X tests - RESIDUAL RISK: HIGH/MEDIUM/LOW])

| Test | Risk of Deferral | Condition for Re-inclusion | Owner |

|---|---|---|---|

### Assumptions

[Numbered list of all assumptions this recommendation depends on]

### Residual Risk Statement

[2-3 sentence plain-language summary of what could slip through with this deferral plan]

### Stakeholder Sign-Off Template

[Ready-to-send message to release manager/PO summarizing the deferral decision 

and requesting sign-off]
```
