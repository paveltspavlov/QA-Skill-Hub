---
id: qa-prompts-6-2-identify-gaps-in-test-coverage
name: "6.2 - Identify Gaps in Test Coverage"
folder: prompts
section: qa-prompts
summary: "Regression & Coverage"
tags:
  - "qa-prompts"
  - "regression & coverage"
---

# Prompt 6.2 - Identify Gaps in Test Coverage

> Category: **Regression & Coverage**

When to use  After test design is complete, to check whether all requirements have corresponding test coverage and identify what's been missed.

Expected output  A requirements-to-test traceability matrix with gaps highlighted and a prioritized list of missing test cases to write.

Prompt

```
**Role:** You are a QA analyst performing a test coverage gap analysis to ensure 

complete requirements traceability before a release.

**Context:** The system is [SYSTEM DESCRIPTION]. The upcoming release covers 

[FEATURE/MODULE NAME].

**Instruction:** Compare the requirements list against the existing test cases. 

Identify:

1. Requirements with NO test coverage

2. Requirements with PARTIAL coverage (some but not all conditions tested)

3. Requirements with GOOD coverage (all main conditions and key edge cases covered)

4. Test cases that don't map to any requirement (orphaned tests - may indicate 

   outdated tests or undocumented requirements)

For each gap (no coverage or partial coverage), generate a one-line description 

of the test case(s) needed to close the gap.

**Input:**

Requirements list:

[PASTE REQUIREMENTS - numbered list works best]

Existing test cases:

[PASTE TEST CASE TITLES AND/OR DESCRIPTIONS]

**Constraints:**

- Map each test case to the requirement(s) it addresses - some tests cover multiple requirements

- For "Partial Coverage" items, be specific about what aspect is missing 

  (e.g., "negative case missing," "boundary values not tested," "error state not covered")

- Prioritize gaps by risk - which missing coverage is most likely to let a production 

  bug through?

**Output Format:**

## Test Coverage Gap Analysis - [FEATURE NAME]

### Coverage Summary

| Status | Count | % of Requirements |

|---|---|---|

| Good Coverage | | |

| Partial Coverage | | |

| No Coverage | | |

| Orphaned Tests | | |

### Traceability Matrix

| Req # | Requirement | Mapped Tests | Coverage Status | Gap Description |

|---|---|---|---|---|

### Gaps to Address - Prioritized

| Priority | Requirement # | Missing Coverage | Suggested Test Case Title |

|---|---|---|---|

### Orphaned Tests (no requirement mapping)

[List test names and note: update requirement mapping OR archive the test]
```
