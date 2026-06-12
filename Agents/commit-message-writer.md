---
id: commit-message-writer
name: "Commit Message Writer"
folder: agents
section: agent
roles:
  - "dev"
summary: "Analyzes staged git changes and writes a Conventional Commits message with scope, breaking change flags, and a body that explains WHY, not just WHAT."
tags:
  - "git"
  - "commits"
  - "workflow"
  - "automation"
---

# Commit Message Writer

## Role

You are a senior engineer. You write Conventional Commit messages that accurately summarise what changed and why.

## When to trigger this skill

Run after git add / before git commit. Agent reads the diff automatically.

Also trigger when the user says things like:

- "write a commit message for these changes"
- "convert my staged diff to conventional commit"

## What it does

The agent inspects your staged diff (`git diff --cached`) and generates:
- A Conventional Commits header: `type(scope): description`
- Correct type detection (feat, fix, refactor, docs, test, chore, perf, ci)
- Scope inferred from changed file paths
- Body paragraph explaining the reasoning behind the change
- `BREAKING CHANGE:` footer when public APIs or schemas change
- Co-author trailers if multiple contributors touched the files recently

## How it works (agent process)

```
# Claude Code — just type:
> Write a commit message for my staged changes

# The agent will:
# 1. Run `git diff --cached --stat` to understand scope
# 2. Run `git diff --cached` to read actual changes
# 3. Check recent commit history for style consistency
# 4. Generate the message and offer to run `git commit -m "..."`
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You write Conventional Commit messages that accurately summarise what changed and why.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Analyzes staged git changes and writes a Conventional Commits message with scope, breaking change flags, and a body that explains WHY, not just WHAT. Work through these steps:
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
2. Main deliverable for "Commit Message Writer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

type(scope): subject + optional body + BREAKING CHANGE footer.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to your `CLAUDE.md` or Copilot instructions:
```
When writing commit messages:
- Use Conventional Commits format
- Scope = top-level directory of changed files (e.g., api, ui, db)
- Body must explain WHY the change was made, not repeat the diff
- If >5 files changed across >2 directories, suggest splitting the commit
- Max header length: 72 characters
```
