---
id: dev-prompts-6-2-write-a-dockerfile-optimised-for-size-and-cache
name: "6.2 - Write a Dockerfile Optimised for Size and Cache"
folder: prompts
section: dev-prompts
summary: "Workflow Automation & Infrastructure"
tags:
  - "dev-prompts"
  - "workflow automation & infrastructure"
---

# Prompt 6.2 - Write a Dockerfile Optimised for Size and Cache

> Category: **Workflow Automation & Infrastructure**

When to use  You need a Dockerfile (or want to clean up an existing one) that builds fast in CI and ships small to prod.

Expected output  A multi-stage Dockerfile + .dockerignore + notes on layer order and base-image choice.

Prompt

```
**Role:** You are an engineer who has watched 1.2 GB images boot slow in production and doesn't want it to happen again.

**Context:** Language / runtime: [LANG]. Target platform: [LINUX/ARM/AMD64]. Runtime user must be non-root: [Y/N (default Y)].

**Instruction:** Produce a production-quality Dockerfile.

1. Choose a minimal base image and justify the choice.

2. Use a multi-stage build: builder + runtime.

3. Order layers so dependency installs are cached before source copy.

4. Drop to a non-root user in the final stage.

5. Provide a matching .dockerignore.

**Input:**

Language / framework:

[SPEC]

Build command:

[CMD]

Start command:

[CMD]

**Constraints:**

- Final image: as small as reasonably possible - justify any >200MB addition.

- No secrets in layers - only via build args or mounted secrets.

- HEALTHCHECK where it makes sense.

**Output Format:**

- Dockerfile

- .dockerignore

- Image-size + security notes
```
