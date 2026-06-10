---
id: dev-prompts-2-1-refactor-a-function-for-readability-without-changing-behaviour
name: "2.1 - Refactor a Function for Readability without Changing Behaviour"
folder: prompts
section: dev-prompts
summary: "Refactoring & Code Quality"
tags:
  - "dev-prompts"
  - "refactoring & code quality"
---

# Prompt 2.1 - Refactor a Function for Readability without Changing Behaviour

> Category: **Refactoring & Code Quality**

When to use  When a function works but nobody wants to touch it - mixed concerns, nested conditionals, unclear names.

Expected output  A refactored function + a diff of behavioural guarantees (what stayed the same) + a list of small follow-up cleanups.

Prompt

```
**Role:** You are a senior engineer who refactors carefully. You value behavioural preservation above all.

**Context:** The codebase is [LANGUAGE/FRAMEWORK]. The function is in [FILE/MODULE] and is called from [CALLERS - name 2-3]. Test coverage around it is [NONE / THIN / GOOD].

**Instruction:** Refactor the function below for readability without changing observable behaviour.

1. List the responsibilities currently bundled in the function.

2. Propose a target shape (function signatures + 1-line purpose each).

3. Produce the refactored code.

4. Produce a "Behavioural guarantees preserved" checklist - input/output shapes, side effects, order of operations.

5. List follow-up cleanups as a separate "Later" list, not mixed into the main refactor.

**Input:**

Current function:

[PASTE CODE]

**Constraints:**

- No new dependencies.

- No API changes visible to callers - same signature or a thin wrapper.

- If you spot a latent bug, call it out in a "Spotted while refactoring" note - do not silently fix it.

**Output Format:**

- Responsibilities list

- Target shape

- Refactored code (full)

- Behavioural guarantees preserved (bullet list)

- Later list

- Spotted while refactoring (if any)
```
