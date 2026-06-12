---
id: qa-prompts-2-1-generate-test-cases-equivalence-partitioning-and-boundary-values
name: "2.1 - Generate Test Cases: Equivalence Partitioning and Boundary Values"
folder: prompts
section: qa-prompts
summary: "Test Case Design"
tags:
  - "qa-prompts"
  - "test case design"
---

# Prompt 2.1 - Generate Test Cases: Equivalence Partitioning and Boundary Values

> Category: **Test Case Design**

When to use  When designing test cases for any input field, parameter range, or data validation rule. Produces systematic coverage using two of the most effective test design techniques.

Expected output  Structured test case table with cases organized by partition and boundary, including expected results for each.

Prompt

```
**Role:** You are a senior QA engineer specializing in systematic test design using 

formal techniques including equivalence partitioning and boundary value analysis.

**Context:** The system is [SYSTEM DESCRIPTION]. The input being tested is 

[FIELD/PARAMETER NAME] in the [FEATURE/MODULE NAME] feature.

**Instruction:** Design a comprehensive set of test cases for the input described below 

using:

1. **Equivalence Partitioning** - identify all valid and invalid equivalence classes, 

   then create one representative test case per class

2. **Boundary Value Analysis** - for each boundary in the valid/invalid ranges, 

   create test cases for: the exact boundary, one step inside, and one step outside

**Input:**

Field/Parameter specification:

[PASTE FIELD SPECIFICATION HERE]

Example: "The field accepts integer values from 1 to 100 inclusive. The field is 

mandatory. Non-integer inputs are rejected."

**Constraints:**

- Cover all equivalence classes including edge cases (null, empty, type mismatch)

- For BVA, use realistic boundary increments for the data type 

  (e.g., integers: ±1; decimals: ±0.01; strings: ±1 character)

- Include at least one security-relevant test case (e.g., SQL injection string, 

  script injection) if the field accepts user text input

- Do not generate duplicate test cases

**Output Format:**

Markdown table:

| ID | Technique | Partition/Boundary | Input Value | Expected Result | Priority |

|---|---|---|---|---|---|

Then: **Coverage Summary** - list all identified equivalence classes and confirm 

each is covered by at least one test case.
```
