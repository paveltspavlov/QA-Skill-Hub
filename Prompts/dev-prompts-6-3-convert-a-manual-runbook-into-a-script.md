---
id: dev-prompts-6-3-convert-a-manual-runbook-into-a-script
name: "6.3 - Convert a Manual Runbook into a Script"
folder: prompts
section: dev-prompts
summary: "Workflow Automation & Infrastructure"
tags:
  - "dev-prompts"
  - "workflow automation & infrastructure"
---

# Prompt 6.3 - Convert a Manual Runbook into a Script

> Category: **Workflow Automation & Infrastructure**

When to use  Your runbook is 11 bullet points of shell commands pasted into Confluence - time to make it a real script with logging and failure handling.

Expected output  A runnable script + usage docs + the bits that should stay manual (with reasons).

Prompt

```
**Role:** You are an engineer who automates what's safe and leaves judgement calls to humans.

**Context:** Target shell / language: [BASH / PYTHON / POWERSHELL]. Where this script runs: [LAPTOP / CI / BASTION].

**Instruction:** Turn the runbook below into a script.

1. Identify which steps are safe to automate vs which require a human decision.

2. For automated steps: wrap each in a function, log start/end, and fail loudly on error.

3. For manual steps: prompt the operator and wait for explicit confirmation.

4. Add a dry-run flag.

5. Write usage docs at the top of the file.

**Input:**

Runbook:

[PASTE]

**Constraints:**

- `set -euo pipefail` (or equivalent) everywhere.

- No silent failures - every command's exit code is checked.

- Don't automate destructive steps without an explicit confirmation prompt.

**Output Format:**

- The script (full)

- Usage docs (at the top)

- What's intentionally left manual + why
```
