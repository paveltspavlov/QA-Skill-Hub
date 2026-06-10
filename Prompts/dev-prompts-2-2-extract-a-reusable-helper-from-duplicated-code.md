---
id: dev-prompts-2-2-extract-a-reusable-helper-from-duplicated-code
name: "2.2 - Extract a Reusable Helper from Duplicated Code"
folder: prompts
section: dev-prompts
summary: "Refactoring & Code Quality"
tags:
  - "dev-prompts"
  - "refactoring & code quality"
---

# Prompt 2.2 - Extract a Reusable Helper from Duplicated Code

> Category: **Refactoring & Code Quality**

When to use  Two or three functions do almost the same thing and the diff is small - it's time to extract the shared bit.

Expected output  A single helper + updated call sites + a justification for the abstraction (so a reviewer can push back).

Prompt

```
**Role:** You are a senior engineer with strong opinions about premature abstraction. You only extract when the shape is clearly stable.

**Context:** Language / framework: [STACK]. The duplicated snippets are in [FILES].

**Instruction:** Given the snippets below:

1. Identify the stable shape - what is genuinely the same, and what only looks the same.

2. If (and only if) the shape is stable, extract a helper with a clear name and signature.

3. Update the call sites to use the helper.

4. If the shape is NOT stable, recommend keeping them separate and explain why.

**Input:**

Snippet A:

[PASTE]

Snippet B:

[PASTE]

Snippet C (optional):

[PASTE]

**Constraints:**

- Name the helper after the concept, not the mechanism.

- Do not swallow differences with a kitchen-sink options object - that's a signal it wasn't ready.

- Prefer pure functions where possible.

**Output Format:**

- Verdict: EXTRACT / DO NOT EXTRACT - one-line reason

- If extracting: the helper + updated call sites

- If not: suggested alternative
```
