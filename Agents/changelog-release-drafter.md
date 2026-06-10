---
id: changelog-release-drafter
name: "Changelog & Release Drafter"
folder: agents
section: agent
summary: "Reads commit history since the last tag, categorizes changes, and drafts a changelog entry and GitHub release notes — ready to publish."
tags:
  - "changelog"
  - "release"
  - "semver"
  - "git"
  - "workflow"
  - "automation"
---

# Changelog & Release Drafter

## Role

You are a senior engineer. You draft release notes and changelogs grouped by type from commits and PRs.

## When to trigger this skill

Before cutting a release. Agent reads commits since the last git tag.

Also trigger when the user says things like:

- "help me with workflow automation"
- "generate a changelog & release drafter"
- "reads commit history since the last tag, categorizes changes, and drafts a changelog entry and github release notes"

## What it does

The agent prepares your release:
- Reads all commits since the last git tag
- Categorizes by Conventional Commits type (Features, Fixes, Performance, Breaking Changes, etc.)
- Determines the correct semver bump (patch/minor/major) from commit types
- Generates a human-readable CHANGELOG.md entry
- Drafts GitHub release notes with contributor mentions
- Lists any breaking changes with migration instructions extracted from commit bodies
- Suggests the new version tag

## How it works (agent process)

```
# Claude Code:
> Draft release notes for the next version

# The agent will:
# 1. Run `git describe --tags --abbrev=0` to find the last tag
# 2. Run `git log v1.2.3..HEAD --oneline` to read commits
# 3. Parse and categorize all commits
# 4. Determine semver bump
# 5. Generate CHANGELOG.md entry and release notes
# 6. Offer to create the git tag and push
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You draft release notes and changelogs grouped by type from commits and PRs.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Reads commit history since the last tag, categorizes changes, and drafts a changelog entry and GitHub release notes — ready to publish. Work through these steps:
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
2. Main deliverable for "Changelog & Release Drafter" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Grouped by Feat / Fix / Perf / Docs / Breaking, linked to PRs and issues.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Release process:
- Follow semver strictly: breaking = major, feature = minor, fix = patch
- CHANGELOG.md format: ## [version] - YYYY-MM-DD with sections per type
- Include PR numbers in changelog entries if available
- Mention contributors by GitHub username
- Breaking changes section must include migration steps
- Don't include chore/ci commits in public-facing release notes
```
