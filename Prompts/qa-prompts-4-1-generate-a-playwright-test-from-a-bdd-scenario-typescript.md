---
id: qa-prompts-4-1-generate-a-playwright-test-from-a-bdd-scenario-typescript
name: "4.1 - Generate a Playwright Test from a BDD Scenario (TypeScript)"
folder: prompts
section: qa-prompts
summary: "Test Automation"
tags:
  - "qa-prompts"
  - "test automation"
---

# Prompt 4.1 - Generate a Playwright Test from a BDD Scenario (TypeScript)

> Category: **Test Automation**

When to use  When converting Gherkin scenarios into executable Playwright tests. Produces the page object and test file simultaneously following the Page Object Model pattern.

Expected output  Two complete TypeScript files - a Page Object class and a test spec file - ready to run after filling in real selectors.

Prompt

```
**Role:** You are a TypeScript developer with deep expertise in Playwright testing 

and the Page Object Model (POM) design pattern. You write clean, typed, maintainable 

test code.

**Context:** The application under test is [APPLICATION DESCRIPTION]. 

Technology stack: TypeScript + Playwright. 

[OPTIONAL: The application uses data-testid attributes for stable selectors. /

 The application uses [SELECTOR STRATEGY]]

**Instruction:** Convert the following Gherkin scenarios into a Playwright TypeScript 

implementation using the Page Object Model pattern. Create two files:

File 1 - Page Object ([PageName]Page.ts):

- Class with typed properties for each locator

- Methods for each user action described in the Gherkin steps

- Constructor accepts a Playwright Page object

- Use descriptive TODO comments for selectors that need to be replaced

- Use Playwright's recommended locator strategies (getByRole, getByTestId, 

  getByLabel preferred over CSS selectors)

File 2 - Test Spec ([featureName].spec.ts):

- Import and instantiate the page object

- One test() per Gherkin Scenario

- One describe() per Feature

- beforeEach() for shared setup steps

- Playwright expect() for all assertions

- Named test data constants (not inline magic values)

- Async/await throughout, no callbacks

**Input:**

Gherkin scenarios:

[PASTE GHERKIN FEATURE FILE HERE]

**Constraints:**

- All selectors that need to be filled in must use descriptive placeholders 

  formatted as: `page.getByTestId('[TODO: replace-with-actual-testid]')`

- Do not import non-existent helpers - use only @playwright/test

- TypeScript strict mode compatible (explicit types on all function signatures)

- Include `test.describe.configure({ mode: 'serial' })` only if the scenarios 

  have dependencies on each other

**Output Format:**

Output both files with clear file name headers:

// === FILE: [PageName]Page.ts ===

[Full TypeScript file]

// === FILE: [featureName].spec.ts ===

[Full TypeScript file]
```
