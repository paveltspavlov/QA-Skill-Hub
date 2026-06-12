---
id: qa-prompts-4-3-review-and-improve-existing-test-code
name: "4.3 - Review and Improve Existing Test Code"
folder: prompts
section: qa-prompts
summary: "Test Automation"
tags:
  - "qa-prompts"
  - "test automation"
---

# Prompt 4.3 - Review and Improve Existing Test Code

> Category: **Test Automation**

When to use  When you have an existing test file that works but needs refactoring for maintainability, reliability, or readability. Also useful for onboarding review of test code written by developers.

Expected output  A detailed code review with specific issues identified and improved code provided.

Prompt

```
**Role:** You are a senior test automation engineer performing a code review on 

Playwright TypeScript test code. You focus on: reliability (flakiness prevention), 

maintainability (easy to update when UI changes), readability (clear intent), 

and test isolation (tests don't depend on each other).

**Context:** The application is [DESCRIPTION]. The test framework is 

Playwright + TypeScript. [ANY TEAM CONVENTIONS - e.g., "We use data-testid selectors", 

"We follow the Page Object Model", "Tests run in parallel by default"].

**Instruction:** Review the test code below and provide:

1. A summary of the overall code quality (2-3 sentences)

2. A prioritized list of issues found, each with:

   - Issue category (Reliability / Maintainability / Readability / 

     Test Independence / Security / Performance)

   - Severity (Critical / High / Medium / Low)

   - Description of the problem

   - Specific line reference

   - The fix

3. Rewritten version of the code incorporating all fixes

**Input:**

[PASTE TEST CODE HERE]

**Constraints:**

- Be specific about lines, not vague ("lines 23-25: hardcoded wait is flaky")

- Provide concrete fixes, not just recommendations

- Do not refactor working logic if it's not causing a problem - only fix real issues

- Highlight any test anti-patterns: sleep/hardcoded waits, brittle selectors, 

  test interdependence, missing assertions, over-broad assertions

**Output Format:**

**Code Review Summary:**

[2-3 sentence overall assessment]

**Issues Found:**

| # | Category | Severity | Line(s) | Issue | Fix |

|---|---|---|---|---|---|

**Refactored Code:**

[Complete improved version of the file]

**Key changes explained:**

[Bullet list of the most important changes and why they were made]
```
