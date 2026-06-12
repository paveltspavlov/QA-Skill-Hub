---
id: qa-prompts-2-2-generate-bdd-gherkin-scenarios-from-acceptance-criteria
name: "2.2 - Generate BDD Gherkin Scenarios from Acceptance Criteria"
folder: prompts
section: qa-prompts
summary: "Test Case Design"
tags:
  - "qa-prompts"
  - "test case design"
---

# Prompt 2.2 - Generate BDD Gherkin Scenarios from Acceptance Criteria

> Category: **Test Case Design**

When to use  When translating acceptance criteria into BDD format for teams using Gherkin-based automation frameworks (Cucumber, Behave, SpecFlow, Playwright Cucumber, etc.).

Expected output  A complete Gherkin feature file with scenarios covering happy path and negative cases, using concrete example values.

Prompt

```
**Role:** You are a QA engineer experienced in Behavior-Driven Development (BDD) 

and skilled at writing Gherkin scenarios that are clear, non-technical, and 

executable by an automation framework.

**Context:** The feature being specified is [FEATURE NAME] in [SYSTEM DESCRIPTION]. 

[OPTIONAL: The automation framework is [FRAMEWORK NAME] - note any syntax variations 

if applicable.]

**Instruction:** Convert the acceptance criteria below into Gherkin BDD scenarios. 

For each acceptance criterion, write:

- At least one Scenario covering the happy path

- At least one Scenario covering a relevant negative/failure case

- A Scenario Outline with Examples table if the scenario has multiple data variations

Follow these Gherkin writing rules:

- Given: system state and preconditions (past tense)

- When: the user action (present tense, single action per step)

- Then: the expected outcome (present tense)

- Use concrete values in steps, not abstract references like "valid data"

- Each scenario should be independently executable

**Input:**

Feature name: [FEATURE NAME]

Acceptance criteria:

[PASTE ACCEPTANCE CRITERIA HERE - numbered list]

**Constraints:**

- Do not create scenarios for features not mentioned in the acceptance criteria

- Each scenario title must be a complete, meaningful sentence

- Avoid "And" chains longer than 3 steps - split into separate Whens if needed

- Include a Background section if preconditions are shared across multiple scenarios

**Output Format:**

Complete Gherkin .feature file format:
```
