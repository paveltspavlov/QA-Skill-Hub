---
id: dev-prompts-2-3-reduce-cyclomatic-complexity-of-a-hotspot
name: "2.3 - Reduce Cyclomatic Complexity of a Hotspot"
folder: prompts
section: dev-prompts
summary: "Refactoring & Code Quality"
tags:
  - "dev-prompts"
  - "refactoring & code quality"
---

# Prompt 2.3 - Reduce Cyclomatic Complexity of a Hotspot

> Category: **Refactoring & Code Quality**

When to use  A function has been flagged by a linter, a code-review comment, or sheer instinct as too complex.

Expected output  A simplified version with fewer branches + a short explanation of the technique used.

Prompt

```
**Role:** You are an engineer who reaches for guard clauses, lookup tables, and polymorphism before nested if/else.

**Context:** Language: [LANG]. Framework: [FRAMEWORK]. The function is called on [HOT PATH / COLD PATH].

**Instruction:** Reduce the cyclomatic complexity of the function below while preserving behaviour.

1. Name the technique you will apply (guard clauses / table-driven / polymorphism / early return / collapsed conditionals).

2. Apply it.

3. Confirm the behaviour is preserved by describing each branch's input/output, before and after.

**Input:**

[PASTE FUNCTION]

**Constraints:**

- One technique per refactor - don't combine table-driven AND polymorphism in one pass.

- No new classes unless polymorphism is the chosen technique.

- Keep the function in the same file.

**Output Format:**

- Technique chosen + reason

- Refactored code

- Branch mapping table (Before → After)
```
