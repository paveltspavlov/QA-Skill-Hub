---
id: qa-prompts-3-3-generate-invalid-and-edge-case-data-for-input-validation-testing
name: "3.3 - Generate Invalid and Edge-Case Data for Input Validation Testing"
folder: prompts
section: qa-prompts
summary: "Test Data Generation"
tags:
  - "qa-prompts"
  - "test data generation"
---

# Prompt 3.3 - Generate Invalid and Edge-Case Data for Input Validation Testing

> Category: **Test Data Generation**

When to use  When testing any user input field for security vulnerabilities, encoding issues, injection attacks, and unexpected input handling.

Expected output  A comprehensive set of malicious, malformed, and edge-case inputs organized by attack/issue type.

Prompt

```
**Role:** You are a QA security tester and input validation specialist. You generate 

adversarial test data to find vulnerabilities in input handling.

**Context:** The system is [SYSTEM DESCRIPTION]. The input field(s) being tested:

[FIELD DESCRIPTION - e.g., "a free-text search field", "a username field", 

"an address input", "a JSON body parameter"]

**Instruction:** Generate a comprehensive set of invalid and edge-case test inputs 

for the field(s) described. Cover these attack and edge-case categories:

1. **SQL Injection** - common SQL injection patterns

2. **XSS (Cross-Site Scripting)** - script injection attempts

3. **Path Traversal** - directory traversal sequences

4. **Command Injection** - shell command sequences

5. **Encoding edge cases** - Unicode, UTF-8 edge cases, null bytes, emoji

6. **Length extremes** - empty string, single character, maximum length, 

   maximum+1 length, very long string (10,000+ chars)

7. **Whitespace** - leading/trailing spaces, tab characters, newlines, 

   non-breaking spaces

8. **Special characters** - quotes, brackets, angle brackets, backslashes

9. **Type confusion** - numeric input in text field, boolean strings, arrays

**Input:**

Field type: [TEXT / NUMERIC / EMAIL / URL / PHONE / etc.]

Field name: [NAME]

Any known allowed characters or formats: [DESCRIBE IF KNOWN]

Any known sanitization already in place: [DESCRIBE IF KNOWN]

**Constraints:**

- Flag inputs that are particularly high-risk with [HIGH RISK]

- Note which inputs are testing security vs. usability vs. robustness

- All inputs are for testing purposes only in a controlled test environment

- Format inputs so they can be copy-pasted directly into a test runner

**Output Format:**

| Category | Test Input | Purpose | Expected System Response | Risk Level |

|---|---|---|---|---|

Then output as a flat JSON array for use in automated parameterized tests:

["[INPUT1]", "[INPUT2]", ...]
```
