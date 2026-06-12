---
id: qa-prompts-5-2-suggest-root-cause-hypotheses-for-a-defect
name: "5.2 - Suggest Root Cause Hypotheses for a Defect"
folder: prompts
section: qa-prompts
summary: "Defect Management"
tags:
  - "qa-prompts"
  - "defect management"
---

# Prompt 5.2 - Suggest Root Cause Hypotheses for a Defect

> Category: **Defect Management**

When to use  During defect investigation when you want to quickly generate investigation leads before diving deep. Useful for standups, triage meetings, or when handing off a defect to a developer.

Expected output  A structured list of plausible root cause hypotheses ranked by likelihood, each with a suggested investigation step.

Prompt

```
**Role:** You are a senior software engineer and QA architect with expertise in 

root cause analysis for software defects. You generate testable hypotheses, not 

guesses.

**Context:** The system architecture is [DESCRIBE RELEVANT ARCHITECTURE - 

e.g., "React frontend, Node.js API, PostgreSQL database, Redis cache"]. 

The affected feature is [FEATURE NAME].

**Instruction:** Based on the defect description below, generate a list of plausible 

root cause hypotheses. For each hypothesis:

1. State the hypothesis clearly

2. Explain the reasoning - what about the defect behavior supports this hypothesis?

3. Rank it: High / Medium / Low likelihood

4. Provide a specific investigation step to confirm or rule out this hypothesis 

   (e.g., "Check the network tab for the response payload", 

   "Add a console.log to [function X]", "Query the DB to check if [field] is set")

**Input:**

Defect title: [TITLE]

Defect description: [FULL BUG REPORT OR DESCRIPTION]

Steps to reproduce: [STEPS]

Expected vs. actual: [EXPECTED vs ACTUAL]

Environment: [ENVIRONMENT DETAILS]

Any other observations: [CONSOLE ERRORS, LOGS, TIMING NOTES, INTERMITTENCY PATTERNS]

**Constraints:**

- Generate 5-8 hypotheses covering different system layers 

  (frontend, API, database, cache, external services, configuration)

- Do not state "the code is wrong" - be specific about what part of the code 

  and what specific mechanism could be wrong

- Rank by likelihood based on the evidence in the defect description

- Investigation steps must be specific actions, not vague suggestions 

  like "investigate the code"

**Output Format:**

## Root Cause Hypotheses for: [DEFECT TITLE]

| # | Hypothesis | Likelihood | Supporting Evidence | Investigation Step |

|---|---|---|---|---|

**Recommended investigation order:** [List hypothesis numbers in the order you'd 

investigate them and why]

**If all hypotheses are ruled out:** [What would be the next investigative step 

beyond these hypotheses]
```
