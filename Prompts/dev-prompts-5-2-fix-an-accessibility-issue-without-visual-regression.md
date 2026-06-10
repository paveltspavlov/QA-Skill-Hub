---
id: dev-prompts-5-2-fix-an-accessibility-issue-without-visual-regression
name: "5.2 - Fix an Accessibility Issue Without Visual Regression"
folder: prompts
section: dev-prompts
summary: "Frontend & UX Implementation"
tags:
  - "dev-prompts"
  - "frontend & ux implementation"
---

# Prompt 5.2 - Fix an Accessibility Issue Without Visual Regression

> Category: **Frontend & UX Implementation**

When to use  When an audit flagged an issue (contrast, focus, semantics) and you need to fix it without changing the visuals product has signed off on.

Expected output  The minimal code change + explanation of the rule it satisfies + a quick manual-verification script.

Prompt

```
**Role:** You are a frontend engineer with a working knowledge of WCAG, ARIA, and the practical difference between decorative and meaningful elements.

**Context:** Framework: [STACK]. The audit tool was [AXE / LIGHTHOUSE / MANUAL]. Visual design is considered final.

**Instruction:** Fix the accessibility issue below without introducing a visual regression.

1. Restate the rule the issue violates in one sentence.

2. Propose the smallest fix.

3. Verify the visual output is unchanged - describe what a reviewer would check.

4. Write a short manual verification script (click here, tab here, screen reader should say X).

**Input:**

Issue:

[PASTE AUDIT OUTPUT]

Current component:

[PASTE]

**Constraints:**

- Don't reach for ARIA if native semantics work.

- Don't hide content with `display: none` to "fix contrast".

- Preserve the existing DOM structure where possible.

**Output Format:**

- Rule (one sentence)

- Fix (diff)

- Visual-parity statement

- Manual verification steps
```
