---
id: dev-prompts-6-1-write-a-github-actions-workflow-for-a-new-pipeline
name: "6.1 - Write a GitHub Actions Workflow for a New Pipeline"
folder: prompts
section: dev-prompts
summary: "Workflow Automation & Infrastructure"
tags:
  - "dev-prompts"
  - "workflow automation & infrastructure"
---

# Prompt 6.1 - Write a GitHub Actions Workflow for a New Pipeline

> Category: **Workflow Automation & Infrastructure**

When to use  When you need a new CI / CD / scheduled pipeline and want it to follow the project's existing conventions.

Expected output  A .github/workflows/*.yml file + a short explanation of triggers, secrets, caching, and concurrency.

Prompt

```
**Role:** You are an engineer who writes CI like production code - pinned, cached, and predictable.

**Context:** Repo language(s): [LANGS]. Existing workflow style: [PIN SHA / PIN TAG / UNPINNED]. Secrets available: [LIST]. Self-hosted runners?: [Y/N].

**Instruction:** Generate a workflow for the pipeline described below.

1. Decide the triggers (push / pull_request / schedule / workflow_dispatch).

2. Pin action versions the same way other workflows in this repo do.

3. Cache dependency installs.

4. Use concurrency to cancel superseded runs.

5. Fail fast when it's safe; continue-on-error only where it makes sense.

**Input:**

Pipeline description:

[PASTE]

Related existing workflow (for style):

[PASTE OR LINK]

**Constraints:**

- No unpinned `@main` references.

- No plaintext secrets - every secret comes from `secrets.*`.

- Job matrix only when it's actually saving time, not just for show.

**Output Format:**

- The workflow file

- Triggers + concurrency notes

- Cache keys + invalidation logic

- Failure mode summary
```
