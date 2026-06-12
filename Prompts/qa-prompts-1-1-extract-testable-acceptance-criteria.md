---
id: qa-prompts-1-1-extract-testable-acceptance-criteria
name: "1.1 - Extract Testable Acceptance Criteria"
folder: prompts
section: qa-prompts
summary: "Requirements Analysis"
tags:
  - "qa-prompts"
  - "requirements analysis"
---

# Prompt 1.1 - Extract Testable Acceptance Criteria

> Category: **Requirements Analysis**

When to use  At the start of any feature, before writing a single test case. Turns vague stories into concrete testable conditions.

Expected output  Numbered list of acceptance criteria, separated into explicit (stated) and implied (assumed).

Prompt

```
**Role:** You are a senior QA analyst with 10 years of experience translating business 

requirements into testable acceptance criteria for enterprise software.

**Context:** The system is [BRIEF SYSTEM DESCRIPTION - e.g., "a B2B SaaS order management 

platform used by logistics companies"]. The feature being analyzed is [FEATURE NAME].

**Instruction:** Analyze the user story below and extract all acceptance criteria. 

Think step by step:

1. First, identify criteria explicitly stated in the story

2. Then, identify criteria that are implied (any reasonable QA would assume these 

   must be true even if not stated)

3. For each criterion, note which test types apply: Functional / Boundary / 

   Negative / Security / Performance / Usability

**Input:**

User Story: [PASTE USER STORY HERE]

**Constraints:**

- Do not invent features or rules not present or reasonably implied by the story

- Flag any criterion that requires clarification before it can be tested (mark with ⚠️)

- Keep each criterion to one sentence - atomic and independently testable

**Output Format:**

**Explicit Acceptance Criteria:**

[Numbered list]

**Implied Acceptance Criteria:**

[Numbered list, each marked with [IMPLIED]]

**Criteria Requiring Clarification:**

[List items marked ⚠️ with a brief note on what's unclear]

**Test Type Mapping:**

[Table: Criterion # | Test Types]
```
