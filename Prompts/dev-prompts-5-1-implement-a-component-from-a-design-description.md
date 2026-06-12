---
id: dev-prompts-5-1-implement-a-component-from-a-design-description
name: "5.1 - Implement a Component from a Design + Description"
folder: prompts
section: dev-prompts
summary: "Frontend & UX Implementation"
tags:
  - "dev-prompts"
  - "frontend & ux implementation"
---

# Prompt 5.1 - Implement a Component from a Design + Description

> Category: **Frontend & UX Implementation**

When to use  You have a design reference and a 2-paragraph description and need a working component with the boring states covered.

Expected output  Component code + all five states (default / hover / loading / empty / error) + a props table.

Prompt

```
**Role:** You are a senior frontend engineer who treats "states designers forgot" as part of the job.

**Context:** Framework: [REACT / VUE / SVELTE / OTHER]. Styling: [TAILWIND / CSS MODULES / OTHER]. Existing component library: [DESIGN SYSTEM IF ANY]. Accessibility target: WCAG 2.1 AA.

**Instruction:** Build the component described below.

1. Propose the prop contract.

2. Implement the component with the five states: default, hover/focus, loading, empty, error.

3. Cover keyboard navigation and visible focus.

4. Add one rendering test per state.

**Input:**

Description:

[PASTE]

Design notes / screenshot description:

[PASTE]

**Constraints:**

- No inline colours / sizes if a token exists - use the design system.

- All interactive elements must be reachable and actionable by keyboard.

- No `any` types / implicit types - the prop types are part of the contract.

**Output Format:**

- Props table: Name | Type | Default | Purpose

- Component code

- States checklist (each state implemented)

- Test file
```
