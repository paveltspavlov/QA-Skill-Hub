---
id: qa-prompts-1-5-map-requirements-to-test-types
name: "1.5 - Map Requirements to Test Types"
folder: prompts
section: qa-prompts
summary: "Requirements Analysis"
tags:
  - "qa-prompts"
  - "requirements analysis"
---

# Prompt 1.5 - Map Requirements to Test Types

> Category: **Requirements Analysis**

When to use  During test planning to ensure the right test types are assigned to each requirement and no testing dimension is overlooked.

Expected output  A requirements-to-test-type mapping table, plus identification of any requirements that need specialized testing expertise.

Prompt

```
**Role:** You are a QA lead responsible for test planning and ensuring complete 

test coverage across all test types for a release.

**Context:** The system is [SYSTEM DESCRIPTION]. The team's testing capabilities 

include: [LIST YOUR TEAM'S TEST TYPES - e.g., functional, API testing, 

performance testing, security testing, accessibility testing, usability testing].

**Instruction:** For each requirement or feature listed below, identify which test 

types should be applied to achieve adequate coverage. For each test type you identify, 

note the priority (Must Have / Should Have / Nice to Have) and any specific concern 

that drives that test type recommendation.

**Input:**

Features or requirements to map:

[PASTE LIST HERE]

**Constraints:**

- Consider these test types at minimum: Functional, Integration, API, Performance/Load, 

  Security, Accessibility (WCAG), Usability, Data Validation, Cross-browser/device

- Add any other relevant test types for your domain

- Flag requirements that will need external specialists (e.g., penetration testers, 

  performance engineers)

- Note if any requirement has dependencies that affect the testing sequence

**Output Format:**

**Requirements to Test Type Mapping:**

| Requirement | Functional | API | Performance | Security | Accessibility | Other | Priority |

|---|---|---|---|---|---|---|---|

[One row per requirement; mark applicable cells with ✓ and add brief note]

**Specialist involvement needed:**

[List any requirements that need expertise beyond the core QA team]

**Suggested test execution sequence:**

[Brief notes on any ordering dependencies]
```
