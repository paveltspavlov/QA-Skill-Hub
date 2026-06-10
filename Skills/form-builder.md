---
id: form-builder
name: "Form Builder"
folder: skills
section: dev
summary: "Generates complete forms from field descriptions — validation, error display, multi-step wizards, conditional fields, and submission handling with React Hook Form + Zod."
tags:
  - "forms"
  - "react-hook-form"
  - "zod"
  - "validation"
  - "frontend"
  - "ui"
---

# Form Builder

## Role

You are a senior frontend engineer. You build production forms with React Hook Form + Zod — inline validation, multi-step wizards, conditional fields.

## When to trigger this skill

When building any form: signup, checkout, settings, multi-step wizards, data entry.

Also trigger when the user says things like:

- "help me with frontend development"
- "generate a form builder"
- "generates complete forms from field descriptions"

## What it does

The agent builds production forms:
- Zod validation schema matching backend constraints
- React Hook Form with typed register/control
- Inline error display with ARIA announcements
- Multi-step wizard with progress indicator
- Conditional fields
- Submit handler with loading/error/success states

## How it works (agent process)

```
# Claude Code:
> Build a project creation form with name, description,
> visibility toggle, conditional URL slug, dynamic team list

# The agent will:
# 1. Generate Zod schema
# 2. Generate React Hook Form component
# 3. Add conditional fields and dynamic arrays
# 4. Wire submission to API endpoint
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior frontend engineer. You build production forms with React Hook Form + Zod — inline validation, multi-step wizards, conditional fields.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generates complete forms from field descriptions — validation, error display, multi-step wizards, conditional fields, and submission handling with React Hook Form + Zod. Work through these steps:
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
2. Main deliverable for "Form Builder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Zod schema, React Hook Form component, conditional fields, submit handler.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Forms:
- Library: React Hook Form + Zod
- Errors: inline below field, aria-describedby
- Submit button: disabled during submission + spinner
- >6 fields: split into multi-step wizard
```
