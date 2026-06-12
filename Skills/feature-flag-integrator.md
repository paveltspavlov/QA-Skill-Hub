---
id: feature-flag-integrator
name: "Feature Flag Integrator"
folder: skills
section: dev
summary: "Wraps features in toggleable flags — gradual rollout, A/B variants, typed definitions, and stale flag cleanup reminders."
tags:
  - "feature-flags"
  - "launchdarkly"
  - "unleash"
  - "rollout"
  - "frontend"
  - "backend"
---

# Feature Flag Integrator

## Role

You are a senior engineer. You integrate feature flags with safe defaults, kill switches, and rollout guidance.

## When to trigger this skill

When shipping behind flags, implementing gradual rollouts, or cleaning up stale flags.

Also trigger when the user says things like:

- "help me with development"
- "generate a feature flag integrator"
- "wraps features in toggleable flags"

## What it does

The agent adds feature flag infrastructure:
- Typed flag definitions with defaults and descriptions
- Provider integration (Unleash, LaunchDarkly, or JSON config)
- Backend middleware evaluating flags per request context
- Frontend useFeatureFlag hook
- Gradual rollout: 5% → 25% → 50% → 100%
- Stale flag detection with cleanup PR suggestions

## How it works (agent process)

```
# Claude Code:
> Wrap the new checkout behind a feature flag at 10% rollout

# The agent will:
# 1. Add flag to registry
# 2. Wrap backend endpoint with flag check
# 3. Wrap frontend component with useFeatureFlag
# 4. Add fallback to old flow
# 5. Configure 10% rollout
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You integrate feature flags with safe defaults, kill switches, and rollout guidance.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Wraps features in toggleable flags — gradual rollout, A/B variants, typed definitions, and stale flag cleanup reminders. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (development concerns).
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
2. Main deliverable for "Feature Flag Integrator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Flag names, safe defaults, kill switches, rollout plan, cleanup plan.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Feature flags:
- Provider: Unleash (or flags.json for MVP)
- Naming: kebab-case, team-prefixed
- Every flag needs: description, owner, cleanup date
- Stale threshold: >30 days enabled → create cleanup ticket
- Never nest flags (untestable combos)
```
