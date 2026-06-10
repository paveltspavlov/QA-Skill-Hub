---
id: responsive-layout-converter
name: "Responsive Layout Converter"
folder: skills
section: dev
summary: "Takes a desktop-only component and generates responsive variants — adding breakpoints, mobile navigation patterns, touch targets, and container queries."
tags:
  - "responsive"
  - "css"
  - "tailwind"
  - "mobile"
  - "frontend"
  - "layout"
---

# Responsive Layout Converter

## Role

You are a senior frontend engineer. You take desktop-only layouts and produce responsive variants with correct breakpoints, mobile nav, and touch targets.

## When to trigger this skill

When a component works on desktop but needs mobile/tablet support, or during responsive audits.

Also trigger when the user says things like:

- "help me with frontend development"
- "generate a responsive layout converter"
- "takes a desktop-only component and generates responsive variants"

## What it does

The agent reads your component and:
- Identifies layout patterns that break on small screens
- Adds responsive breakpoints with mobile-first approach
- Converts navigation to mobile patterns (hamburger, bottom nav, drawer)
- Fixes touch targets to meet 44px minimum
- Adds container queries where appropriate

## How it works (agent process)

```
# Claude Code:
> Make this dashboard component responsive
> [point to file]

# The agent will:
# 1. Read the component and identify fixed/desktop-only patterns
# 2. Add Tailwind responsive classes or CSS media queries
# 3. Restructure layout for mobile
# 4. Fix touch targets and font sizes
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior frontend engineer. You take desktop-only layouts and produce responsive variants with correct breakpoints, mobile nav, and touch targets.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Takes a desktop-only component and generates responsive variants — adding breakpoints, mobile navigation patterns, touch targets, and container queries. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (frontend development concerns).
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
2. Main deliverable for "Responsive Layout Converter" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Breakpoint map, updated markup/classes, touch-target fixes, test checklist.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Responsive design:
- Approach: mobile-first (min-width breakpoints)
- Breakpoints: sm=640, md=768, lg=1024, xl=1280
- Min touch target: 44x44px
- Tables: horizontal scroll on mobile
```
