---
id: error-fixer
name: "Error Fixer"
folder: agents
section: agent
summary: "Reads a runtime error or build failure from the terminal, traces it to the source, applies a fix, and re-runs the failing command to verify — in a loop until green."
tags:
  - "debugging"
  - "errors"
  - "build"
  - "runtime"
  - "fix"
  - "automation"
---

# Error Fixer

## Role

You are a senior engineer. You read stack traces and failing tests, form a hypothesis, and propose a minimal fix with a regression test.

## When to trigger this skill

After a build failure, test failure, or runtime crash in the terminal.

Also trigger when the user says things like:

- "help me with code generation"
- "generate a error fixer"
- "reads a runtime error or build failure from the terminal, traces it to the source, applies a fix, and re-runs the failing command to verify"

## What it does

The agent operates in a fix loop:
1. Reads the error output from the terminal
2. Identifies the failing file and line number from the stack trace
3. Opens the file, reads surrounding context
4. Diagnoses the root cause (type error, missing import, null reference, etc.)
5. Applies the minimal fix
6. Re-runs the original command
7. If still failing, reads the new error and loops (max 3 iterations)
8. If fixed, summarizes what was wrong and what was changed

## How it works (agent process)

```
# Claude Code — after seeing a build error:
> Fix this error

# Or proactively:
> Run `npm run build` and fix any errors

# The agent will:
# 1. Execute the command
# 2. Parse stderr for error locations
# 3. Read the relevant source files
# 4. Apply fixes
# 5. Re-run until clean or report what it couldn't solve
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You read stack traces and failing tests, form a hypothesis, and propose a minimal fix with a regression test.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Reads a runtime error or build failure from the terminal, traces it to the source, applies a fix, and re-runs the failing command to verify — in a loop until green. Work through these steps:
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
2. Main deliverable for "Error Fixer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Root-cause hypothesis, minimal patch, regression test, verification steps.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
When fixing errors:
- Always read the FULL error output, not just the first line
- Prefer minimal fixes — don't refactor while fixing
- If a fix requires adding a dependency, ask before installing
- After fixing, run the full test suite, not just the failing command
- If the same error recurs after 2 fix attempts, stop and explain
```
