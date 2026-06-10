---
id: qa-prompts-1-4-check-requirements-for-testability-issues
name: "1.4 - Check Requirements for Testability Issues"
folder: prompts
section: qa-prompts
summary: "Requirements Analysis"
tags:
  - "qa-prompts"
  - "requirements analysis"
---

# Prompt 1.4 - Check Requirements for Testability Issues

> Category: **Requirements Analysis**

When to use  When requirements have been written but before test planning begins. Identifies requirements that are structurally impossible to test as written.

Expected output  Testability assessment for each requirement, with specific rewrites suggested for untestable ones.

Prompt

```
**Role:** You are a QA architect reviewing a requirements document from a testability 

perspective. Your job is not to verify whether requirements are correct or complete, 

but whether each individual requirement can be objectively tested.

**Context:** [SYSTEM DESCRIPTION]

**Instruction:** Review each requirement below and assess its testability using 

these criteria:

- **Testable:** A test can objectively pass or fail this requirement

- **Partially testable:** Some parts can be tested, but aspects are subjective or vague

- **Not testable:** The requirement is too vague, subjective, or ambiguous to verify

For requirements that are not testable or only partially testable, provide:

1. The reason it's not testable

2. A suggested rewrite that makes it testable

**Input:**

Requirements:

[PASTE REQUIREMENTS LIST HERE - numbered or bulleted]

**Constraints:**

- Evaluate each requirement individually

- Be specific about which words or phrases make a requirement untestable 

  (e.g., "quickly," "user-friendly," "should work correctly")

- Suggested rewrites must be specific and measurable

**Output Format:**

| # | Requirement (abbreviated) | Testability | Issue | Suggested Rewrite |

|---|---|---|---|---|

[One row per requirement]

**Summary:**

- Testable: [X] / [Total]

- Partially testable: [X] / [Total]  

- Not testable: [X] / [Total]

**Top priority rewrites:** [List the 3 most critical rewrites needed]
```
