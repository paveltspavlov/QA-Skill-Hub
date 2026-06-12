---
id: test-writer-on-change
name: "Test Writer on Change"
folder: agents
section: agent
roles:
  - "qa"
summary: "Watches for code changes and automatically generates or updates unit tests for modified functions — maintaining coverage without manual test writing."
tags:
  - "testing"
  - "unit-tests"
  - "automation"
  - "tdd"
  - "coverage"
---

# Test Writer on Change

## Role

You are a senior developer-in-test. When code changes, you produce the matching tests so coverage keeps pace with delivery.

## When to trigger this skill

After modifying a function or adding new code. Can be run as a pre-commit hook behavior.

Also trigger when the user says things like:

- "help me with code generation"
- "generate a test writer on change"
- "watches for code changes and automatically generates or updates unit tests for modified functions"

## What it does

After you modify or create source code, the agent:
- Detects which functions/methods were changed (via git diff)
- Checks if corresponding tests exist and whether they cover the new behavior
- Generates new test cases for added code paths
- Updates existing tests if function signatures or behavior changed
- Follows your project's test patterns (AAA, describe/it nesting, fixture style)
- Runs the new tests to verify they pass
- Reports coverage delta: "Added 3 tests, branch coverage +12% for this file"

## How it works (agent process)

```
# Claude Code:
> Write tests for the functions I changed in this branch

# The agent will:
# 1. Run `git diff main --name-only` to find changed files
# 2. For each changed file, parse the diff to find modified functions
# 3. Read existing test files for those functions
# 4. Generate missing test cases matching project conventions
# 5. Run the tests to verify they pass
# 6. Report what was added
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior developer-in-test. When code changes, you produce the matching tests so coverage keeps pace with delivery.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Watches for code changes and automatically generates or updates unit tests for modified functions — maintaining coverage without manual test writing. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (code generation concerns).
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
2. Main deliverable for "Test Writer on Change" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Matching test file with cases for added/modified behaviour, mocks, and edge cases.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Traceability to a requirement ID or bug ID is present.
- [ ] Positive, negative, and boundary cases are all covered.

## Companion repo configuration

Add to `CLAUDE.md`:
```
Test generation rules:
- Framework: Jest (frontend), Pytest (backend)
- Pattern: AAA (Arrange-Act-Assert), one assertion per test
- Naming: describe("FunctionName") > it("should [behavior] when [condition]")
- Always mock external services (DB, HTTP, file system)
- Generate edge cases: null input, empty array, boundary values
- Co-locate tests: src/services/user.service.ts → src/services/user.service.test.ts
```
