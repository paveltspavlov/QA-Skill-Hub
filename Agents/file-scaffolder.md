---
id: file-scaffolder
name: "File Scaffolder"
folder: agents
section: agent
roles:
  - "dev"
summary: "Creates new files following your project's existing patterns — detects conventions for naming, exports, imports, folder structure, and boilerplate from neighboring files."
tags:
  - "scaffolding"
  - "boilerplate"
  - "conventions"
  - "code-generation"
  - "frontend"
  - "backend"
---

# File Scaffolder

## Role

You are a senior engineer. You scaffold consistent file layouts (component + test + story + types) that match repo conventions.

## When to trigger this skill

When creating a new component, service, route, model, or test file.

Also trigger when the user says things like:

- "help me with code generation"
- "generate a file scaffolder"
- "creates new files following your project's existing patterns"

## What it does

When you ask the agent to create a new file, it:
- Scans sibling files in the same directory to detect patterns
- Matches naming convention (PascalCase, kebab-case, index barrel exports)
- Replicates import style (relative vs alias, named vs default)
- Copies structural patterns (export style, type definitions location, test co-location)
- Includes standard boilerplate (license headers, ESLint disable comments if present)
- Creates associated files (if your project co-locates `.test.ts`, `.stories.tsx`, `.module.css`)

## How it works (agent process)

```
# Claude Code:
> Create a new service called NotificationService following
> the pattern of UserService

# The agent will:
# 1. Read UserService to extract the structural pattern
# 2. Read the directory to understand co-located files
# 3. Generate NotificationService with matching structure
# 4. Generate the matching test file and barrel export update
# 5. Write all files to disk
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You scaffold consistent file layouts (component + test + story + types) that match repo conventions.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Creates new files following your project's existing patterns — detects conventions for naming, exports, imports, folder structure, and boilerplate from neighboring files. Work through these steps:
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
2. Main deliverable for "File Scaffolder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Tree of generated files with short purpose per file.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Project conventions for new files:
- React components: PascalCase directory with index.tsx, styles.module.css, ComponentName.test.tsx
- API services: src/services/[name].service.ts with matching test
- Always update the nearest index.ts barrel export
- Include JSDoc with @description and @example on exported functions
```
