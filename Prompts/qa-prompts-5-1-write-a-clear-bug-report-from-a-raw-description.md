---
id: qa-prompts-5-1-write-a-clear-bug-report-from-a-raw-description
name: "5.1 - Write a Clear Bug Report from a Raw Description"
folder: prompts
section: qa-prompts
summary: "Defect Management"
tags:
  - "qa-prompts"
  - "defect management"
---

# Prompt 5.1 - Write a Clear Bug Report from a Raw Description

> Category: **Defect Management**

When to use  When you've found a bug and need to write it up quickly but properly. Turn rough notes into a professional, developer-ready defect report.

Expected output  A complete, structured bug report with all required fields, written in clear language that a developer can act on immediately.

Prompt

```
**Role:** You are a QA engineer writing defect reports. You write bug reports that 

are specific, reproducible, professional, and give developers everything they need 

to investigate without asking follow-up questions.

**Context:** The system is [SYSTEM DESCRIPTION]. Defects are tracked in 

[JIRA / AZURE DEVOPS / GITHUB ISSUES / etc.].

**Instruction:** Convert the raw bug description below into a complete, well-structured 

defect report. A good bug report is: specific (not "it doesn't work"), reproducible 

(clear steps anyone can follow), informative (includes all relevant context), 

and impactful (explains what business function is affected).

Fill in all sections. If information is missing from the raw notes, flag it 

with [NEEDS INFO] so the reporter can fill it in.

**Input:**

Raw bug description:

[PASTE YOUR ROUGH NOTES OR DESCRIPTION HERE - can be conversational or very rough]

**Constraints:**

- Steps to reproduce must be specific enough that a developer with no context can 

  follow them

- Expected vs. actual results must both be stated - never just "it's broken"

- Include any relevant environment information (browser, OS, version, data state)

- Severity and Priority are separate: Severity = how bad is the defect; 

  Priority = how urgently should it be fixed

**Output Format:**

**Bug Report**

**Title:** [Clear, specific, searchable title - max 80 characters]

**Severity:** [Critical / High / Medium / Low]

**Priority:** [P1 / P2 / P3 / P4]

**Feature/Module:** [Which part of the system]

**Environment:** [Browser, OS, app version, test environment]

**Reproducibility:** [Always / Intermittent / Happened once]

**Summary:** [2-3 sentence plain-language description of the defect]

**Steps to Reproduce:**

1. [Step]

2. [Step]

...

**Expected Result:** [What should happen]

**Actual Result:** [What actually happens]

**Evidence:** [Screenshots, logs, network requests - or "[ATTACH]" placeholder]

**Test Data Used:** [What data was in the system when this occurred]

**Regression Risk:** [What other areas could be affected by this defect or its fix?]

**Notes for Developer:** [Anything else that might help - console errors, theories, 

related issues, etc.]
```
