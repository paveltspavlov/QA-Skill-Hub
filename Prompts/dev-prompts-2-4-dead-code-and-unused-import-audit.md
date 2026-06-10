---
id: dev-prompts-2-4-dead-code-and-unused-import-audit
name: "2.4 - Dead-Code and Unused-Import Audit"
folder: prompts
section: dev-prompts
summary: "Refactoring & Code Quality"
tags:
  - "dev-prompts"
  - "refactoring & code quality"
---

# Prompt 2.4 - Dead-Code and Unused-Import Audit

> Category: **Refactoring & Code Quality**

When to use  Before a release or when onboarding a new engineer - cleanse the module of things nobody calls.

Expected output  A report listing confirmed dead code, suspected dead code, and items to confirm manually before deletion.

Prompt

```
**Role:** You are a careful engineer who never deletes something until they are confident nobody reaches it - including dynamically.

**Context:** Stack: [STACK]. The project uses [BUILD / BUNDLE TOOL]. Entry points are [LIST]. Known dynamic callsites (reflection, string imports, config-driven wiring) are in [FILES].

**Instruction:** Audit the file(s) below for dead code.

1. For each exported symbol, classify: USED / DEAD / SUSPECT.

2. For USED: list one caller.

3. For DEAD: cite why (no callers found).

4. For SUSPECT: explain the dynamic / reflective / config-driven path that could still hit it.

5. Same treatment for unused imports.

**Input:**

[PASTE FILE(S)]

**Constraints:**

- Do not delete anything - output a report only.

- Default to SUSPECT when in doubt.

**Output Format:**

- Symbols table: Name | Kind | Verdict | Evidence

- Imports table: Module | Verdict | Evidence

- Safe-to-remove list (DEAD only)

- Confirm-manually list (SUSPECT)
```
