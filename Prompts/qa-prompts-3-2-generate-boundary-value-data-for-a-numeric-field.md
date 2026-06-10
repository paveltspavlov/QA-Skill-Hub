---
id: qa-prompts-3-2-generate-boundary-value-data-for-a-numeric-field
name: "3.2 - Generate Boundary Value Data for a Numeric Field"
folder: prompts
section: qa-prompts
summary: "Test Data Generation"
tags:
  - "qa-prompts"
  - "test data generation"
---

# Prompt 3.2 - Generate Boundary Value Data for a Numeric Field

> Category: **Test Data Generation**

When to use  When writing input validation tests for any numeric field. Produces a complete dataset covering all boundaries with labeled expected behaviors.

Expected output  A structured test data set covering all critical numeric boundaries, formatted for direct use in parameterized tests.

Prompt

```
**Role:** You are a QA engineer generating systematic boundary value test data 

using equivalence partitioning and boundary value analysis techniques.

**Context:** The system is [SYSTEM DESCRIPTION]. The numeric field being tested is 

[FIELD NAME] in the [FEATURE/FORM/API] with the following specification:

[FIELD SPECIFICATION]

**Instruction:** Generate a complete boundary value test dataset for this field. 

Cover:

1. The exact minimum valid value

2. One step below the minimum (just invalid)

3. One step above the minimum (well within valid range)

4. A typical valid mid-range value

5. One step below the maximum (well within valid range)

6. The exact maximum valid value

7. One step above the maximum (just invalid)

8. Zero (if not already covered)

9. Negative values (if applicable)

10. Non-numeric inputs (null, empty string, alphabetic, special characters)

11. Very large numbers (integer overflow range)

12. Decimal precision edge cases (if applicable)

**Input:**

Field name: [FIELD NAME]

Data type: [integer / decimal / currency / etc.]

Minimum valid value: [VALUE]

Maximum valid value: [VALUE]

Required decimal places: [e.g., "exactly 2" or "0 to 4" or "none"]

Is the field mandatory: [Yes/No]

Any other validation rules: [LIST ANY ADDITIONAL RULES]

**Constraints:**

- Use the exact increment appropriate for the data type 

  (integers: ±1; currency: ±0.01; percentages: ±0.1)

- For each value, specify the exact expected system response (not just "valid" or "invalid")

- Include the error message text if specified in requirements

**Output Format:**

Markdown table:

| Test # | Input Value | Type | Expected Validity | Expected System Response | Notes |

|---|---|---|---|---|---|

Then: TypeScript/JavaScript array format for use in parameterized tests:

const [FIELDNAME]TestData = [

  { input: [VALUE], valid: true, expectedMessage: null },

  { input: [VALUE], valid: false, expectedMessage: "[ERROR MESSAGE]" },

  ...

];
```
