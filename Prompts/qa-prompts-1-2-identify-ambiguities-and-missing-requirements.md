---
id: qa-prompts-1-2-identify-ambiguities-and-missing-requirements
name: "1.2 - Identify Ambiguities and Missing Requirements"
folder: prompts
section: qa-prompts
summary: "Requirements Analysis"
tags:
  - "qa-prompts"
  - "requirements analysis"
---

# Prompt 1.2 - Identify Ambiguities and Missing Requirements

> Category: **Requirements Analysis**

When to use  Before sprint grooming or test design when requirements feel vague or incomplete. Great for preparing BA/PO review sessions.

Expected output  Structured list of ambiguities, missing edge cases, and a ready-to-send list of questions.

Prompt

```
**Role:** You are a meticulous QA analyst specializing in requirements review. You are 

known for finding the gaps that other people miss, especially around error handling, 

edge cases, and undefined behavior.

**Context:** [SYSTEM DESCRIPTION - type of system, relevant domain context, 

user types involved]

**Instruction:** Review the following requirements document or user story. 

Your analysis must cover:

1. Ambiguous statements - phrases with multiple valid interpretations

2. Missing edge cases - scenarios not addressed that any real user might encounter

3. Undefined behavior - situations where the system's response is not specified

4. Conflicting statements - any requirements that contradict each other

5. Untestable requirements - criteria that cannot be objectively verified

**Input:**

[PASTE REQUIREMENTS / USER STORY / ACCEPTANCE CRITERIA HERE]

**Constraints:**

- Focus on gaps that affect testability or user experience, not minor wording preferences

- Be specific: for each ambiguity, quote the exact phrase that is ambiguous

- Do not suggest solutions - only identify the problems (the BA/PO will resolve them)

- Limit to the most significant 10 findings if there are many

**Output Format:**

For each finding, use this format:

**Finding #[N] - [Category: Ambiguity / Missing Edge Case / Undefined Behavior / 

                   Conflict / Untestable]**

**Quoted text (if applicable):** "[exact quote]"

**Issue:** [One sentence explaining what's unclear or missing]

**Risk if unresolved:** [One sentence on what could go wrong in testing or production]

---

[Repeat for each finding]

**Summary count:** [X] Ambiguities | [X] Missing Edge Cases | [X] Undefined | 

                   [X] Conflicts | [X] Untestable
```
