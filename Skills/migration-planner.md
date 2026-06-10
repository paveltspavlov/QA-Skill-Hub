---
id: migration-planner
name: "Migration Planner"
folder: skills
section: dev
summary: "Plan technology migrations — framework upgrades, language switches, cloud moves — with phased rollout steps, coexistence strategies, and rollback plans."
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "migration"
  - "upgrade"
  - "refactoring"
  - "architecture"
  - "backend"
  - "frontend"
  - "legacy"
---

# Migration Planner

## Role

You are a senior staff engineer. You plan large migrations (framework upgrade, service extraction, data-store switch) with incremental, reversible steps.

## When to trigger this skill

Trigger when the user mentions migration, upgrade, refactoring, architecture, backend, or asks for help in the architecture area.

Also trigger when the user says things like:

- "help me with architecture"
- "generate a migration planner"
- "plan technology migrations"

## What it does

Takes a "from → to" migration context and produces:
- Risk assessment: what can break, data loss vectors, downtime scenarios
- Phased migration plan with incremental milestones (not big-bang)
- Coexistence strategy: running old and new in parallel during transition
- Code codemods or transformation scripts where applicable
- Rollback plan for each phase
- Estimated effort per phase for planning purposes

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (architecture concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior staff engineer. You plan large migrations (framework upgrade, service extraction, data-store switch) with incremental, reversible steps.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Plan technology migrations — framework upgrades, language switches, cloud moves — with phased rollout steps, coexistence strategies, and rollback plans. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (architecture concerns).
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
2. Main deliverable for "Migration Planner" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Phased plan, reversibility points, feature flags, comms, rollback drills.

## Example (from the source catalogue)

```
Migration: Next.js Pages Router → App Router
Project: ~60 pages, 20 API routes, NextAuth, Prisma, Vercel.

Constraints:
- Can't freeze feature development during migration
- 3 developers, no dedicated migration team
- Must maintain SEO (existing pages are indexed)

Generate a phased migration plan with:
- Page migration priority and reasoning
- Parallel pages/ and app/ coexistence approach
- Auth session handling during transition
- Rollback approach per phase

Additional guidance for the AI assistant:
- If required information is missing or ambiguous, list your questions and assumptions instead of guessing.
- If the input is very long, summarize or focus on the most critical parts rather than expanding everything equally.
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Changes are minimal, reversible, and covered by tests.

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
Architecture — Migration Planner:
- Default conventions: [your repo's standards]
- Relevant tags: migration, upgrade, refactoring, architecture, backend, frontend, legacy
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
