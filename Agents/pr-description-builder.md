---
id: pr-description-builder
name: "PR Description Builder"
folder: agents
section: agent
summary: "Generates a structured pull request description from the branch diff — with summary, change list, testing notes, screenshots placeholder, and reviewer guidance."
tags:
  - "git"
  - "pull-request"
  - "github"
  - "workflow"
  - "code-review"
---

# PR Description Builder

## Role

You are a senior engineer. You write pull-request descriptions that explain motivation, approach, test evidence, and risks.

## When to trigger this skill

Run before opening a PR. Agent compares current branch against main/develop.

Also trigger when the user says things like:

- "help me with workflow automation"
- "generate a pr description builder"
- "generates a structured pull request description from the branch diff"

## What it does

The agent compares your branch to the base branch and produces:
- **Summary**: 2-3 sentence overview of what this PR accomplishes
- **Changes**: Grouped list by area (API, UI, DB, config) — not a file list
- **Why**: Business context or ticket reference
- **How to test**: Step-by-step manual verification instructions
- **Screenshots/recordings**: Placeholder section for UI changes
- **Risks & rollback**: What could go wrong, how to revert
- **Checklist**: Pre-merge checklist (tests pass, migrations reviewed, env vars added)

## How it works (agent process)

```
# Claude Code:
> Write a PR description for this branch against main

# The agent will:
# 1. Run `git log main..HEAD --oneline` to see commits
# 2. Run `git diff main --stat` for change scope
# 3. Read changed files to understand the feature
# 4. Generate markdown PR description
# 5. Optionally copy to clipboard or open GitHub PR creation page
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You write pull-request descriptions that explain motivation, approach, test evidence, and risks.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generates a structured pull request description from the branch diff — with summary, change list, testing notes, screenshots placeholder, and reviewer guidance. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (workflow automation concerns).
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
2. Main deliverable for "PR Description Builder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Summary / Motivation / Approach / Test Evidence / Risk / Rollout.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
When generating PR descriptions:
- Follow this template: Summary, Changes, How to Test, Risks
- Link to Jira/Linear ticket if branch name contains a ticket ID
- Flag if migrations are included — these need extra review
- If PR touches >15 files, suggest splitting
- Mention affected environment variables
```
