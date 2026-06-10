---
id: unit-test-scaffolder
name: "Unit Test Scaffolder"
folder: skills
section: qa
summary: "Generate well-structured unit tests from source code — covering happy paths, edge cases, and error branches with proper mocking and assertion patterns."
istqbTopics:
  - "Component Testing"
  - "Test Design Techniques"
  - "White-box Testing"
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "unit-testing"
  - "jest"
  - "pytest"
  - "mocha"
  - "backend"
  - "frontend"
  - "tdd"
---

# Unit Test Scaffolder

## Role

You are a senior developer-in-test. You scaffold unit tests that mirror production code structure, mock dependencies cleanly, and cover positive / negative / boundary cases.

## When to trigger this skill

Trigger when the user mentions unit-testing, jest, pytest, mocha, backend, or asks for help in the test automation area.

Also trigger when the user says things like:

- "help me with test automation"
- "generate a unit test scaffolder"
- "generate well-structured unit tests from source code"

## What it does

Takes a function, class, or module and generates a complete unit test file including:
- Happy path tests for primary behavior
- Edge case tests (empty inputs, boundary values, null/undefined)
- Error branch tests (exceptions, invalid state)
- Mocking strategy for external dependencies (DB, APIs, file system)
- Parameterized/data-driven variants where applicable
- Follows AAA pattern (Arrange-Act-Assert) consistently

Supports Jest, Pytest, Mocha, Vitest, NUnit — specify your framework.

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (test automation concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior developer-in-test. You scaffold unit tests that mirror production code structure, mock dependencies cleanly, and cover positive / negative / boundary cases.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generate well-structured unit tests from source code — covering happy paths, edge cases, and error branches with proper mocking and assertion patterns. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (test automation concerns).
3. Produce the output in the format requested below.
4. Flag assumptions and risks you had to make.

**Input:**
[PASTE CODE, REQUIREMENT, BUG DATA, SCHEMA, OR FILE PATH HERE]

**Constraints:**
- Follow this repository's conventions (see `.github/copilot-instructions.md`).
- Do not invent facts. If information is missing, list it as an assumption.
- Keep the output scannable — use tables, numbered lists, and code fences.
- Cite specific lines / rows / fields when referring to the input.

**Output Format:**
1. Short summary (2–3 sentences).
2. Main deliverable for "Unit Test Scaffolder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Test files matching source structure; Arrange-Act-Assert with mocked collaborators.

## Example (from the source catalogue)

```
Generate unit tests for this TypeScript service method using Jest:
[paste code]

Requirements:
- Mock the database repository and HTTP client
- Cover: valid input, empty input, null input, DB connection failure,
  HTTP timeout, and response parsing error
- Use AAA pattern, descriptive test names, one assertion per test
- Include a describe block structure grouped by scenario type

Additional guidance for the AI assistant:
- If required information is missing or ambiguous, list your questions and assumptions instead of guessing.
- If the input is very long, summarize or focus on the most critical parts rather than expanding everything equally.
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Traceability to a requirement ID or bug ID is present.
- [ ] Positive, negative, and boundary cases are all covered.

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
Test Automation — Unit Test Scaffolder:
- Default conventions: [your repo's standards]
- Relevant tags: unit-testing, jest, pytest, mocha, backend, frontend, tdd
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
