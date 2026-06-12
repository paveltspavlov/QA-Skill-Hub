---
id: git-workflow-automator
name: "Git Workflow Automator"
folder: skills
section: dev
summary: "Generate Git hooks, branching strategies, CI workflow files, and commit conventions tailored to your team size and release cadence."
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "git"
  - "github-actions"
  - "gitlab-ci"
  - "devops"
  - "ci-cd"
  - "branching"
  - "automation"
---

# Git Workflow Automator

## Role

You are a senior DevOps engineer. You design Git workflows, hooks, and branch policies that fit the team's release cadence.

## When to trigger this skill

Trigger when the user mentions git, github-actions, gitlab-ci, devops, ci-cd, or asks for help in the devops area.

Also trigger when the user says things like:

- "help me with devops"
- "generate a git workflow automator"
- "generate git hooks, branching strategies, ci workflow files, and commit conventions tailored to your team size and release cadence."

## What it does

Takes your team context and generates:
- Branching strategy document (GitFlow, trunk-based, or hybrid) with reasoning
- GitHub Actions / GitLab CI workflow files for your stack
- Pre-commit hooks (lint, format, type-check, commit message validation)
- Conventional commits config + changelog generation setup
- Branch protection rules recommendation
- Release automation (semantic versioning, auto-tagging, release notes)
- PR template with checklist

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (devops concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior DevOps engineer. You design Git workflows, hooks, and branch policies that fit the team's release cadence.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generate Git hooks, branching strategies, CI workflow files, and commit conventions tailored to your team size and release cadence. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (devops concerns).
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
2. Main deliverable for "Git Workflow Automator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Workflow diagram, branch policy, hooks, PR template, release cadence.

## Example (from the source catalogue)

```
Team: 6 devs, 2-week sprints, deploy to staging on merge,
production release every 2 weeks.
Stack: TypeScript monorepo (Turborepo), pnpm, Next.js + NestJS

Generate:
1. Branching strategy with diagram
2. GitHub Actions: lint + typecheck + test on PR, deploy on merge
3. Pre-commit hooks config (husky + lint-staged)
4. Conventional commits setup with auto-changelog
5. PR template
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
DevOps — Git Workflow Automator:
- Default conventions: [your repo's standards]
- Relevant tags: git, github-actions, gitlab-ci, devops, ci-cd, branching, automation
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
