---
id: qa-prompts-2-3-generate-negative-and-edge-case-test-scenarios
name: "2.3 - Generate Negative and Edge-Case Test Scenarios"
folder: prompts
section: qa-prompts
summary: "Test Case Design"
tags:
  - "qa-prompts"
  - "test case design"
---

# Prompt 2.3 - Generate Negative and Edge-Case Test Scenarios

> Category: **Test Case Design**

When to use  After generating happy-path test cases, when you want to systematically find the scenarios that break things. Especially valuable for API testing, input validation, and integration testing.

Expected output  A comprehensive set of negative and edge-case scenarios organized by category (null/empty, wrong type, boundary violations, sequence errors, concurrent access, etc.).

Prompt

```
**Role:** You are a QA engineer known for adversarial thinking - you specialize in 

finding the scenarios that developers don't consider and that slip past basic testing.

**Context:** The feature being tested is [FEATURE NAME] in [SYSTEM DESCRIPTION]. 

[INCLUDE RELEVANT TECHNICAL CONTEXT: is it an API endpoint? A UI form? A background 

process? What are the key inputs and outputs?]

**Instruction:** Generate negative and edge-case test scenarios for the feature 

described below. Think adversarially - consider:

1. Invalid inputs (wrong type, wrong format, out of range, empty, null)

2. Boundary violations (just outside valid ranges)

3. Sequence/state violations (actions taken in wrong order, prerequisites not met)

4. Concurrency scenarios (what if two users do this simultaneously?)

5. Resource/limit scenarios (at maximum capacity, quota exceeded, timeout)

6. Security-relevant scenarios (injection, unauthorized access, privilege escalation)

7. Integration failure scenarios (dependent service is down, returns error, is slow)

**Input:**

Feature specification:

[PASTE SPECIFICATION, USER STORY, OR ACCEPTANCE CRITERIA HERE]

Known happy-path scenarios already covered:

[LIST ALREADY-COVERED SCENARIOS so the AI doesn't duplicate them]

**Constraints:**

- Focus exclusively on negative and edge cases - do not regenerate happy-path scenarios

- Organize output by the negative scenario category listed above

- For each scenario, explicitly state: what is invalid/wrong, and what the expected 

  system response should be (not just "should show an error" - be specific)

- Flag any scenario that requires special environment setup (e.g., "requires 

  network partition simulation") with a [SETUP REQUIRED] tag

**Output Format:**

For each category:

## [Category Name]

| ID | Scenario | Input/Condition | Expected System Response | Setup Required? |

|---|---|---|---|---|
```
