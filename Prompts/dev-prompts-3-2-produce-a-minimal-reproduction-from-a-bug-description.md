---
id: dev-prompts-3-2-produce-a-minimal-reproduction-from-a-bug-description
name: "3.2 - Produce a Minimal Reproduction from a Bug Description"
folder: prompts
section: dev-prompts
summary: "Debugging & Diagnostics"
tags:
  - "dev-prompts"
  - "debugging & diagnostics"
---

# Prompt 3.2 - Produce a Minimal Reproduction from a Bug Description

> Category: **Debugging & Diagnostics**

When to use  A teammate describes a bug in prose and you need a runnable repro in under 30 lines.

Expected output  A minimal script / test that deterministically reproduces the bug, with clearly labelled inputs.

Prompt

```
**Role:** You are a pragmatic engineer who believes a repro is worth ten descriptions.

**Context:** Language / framework: [STACK]. Required deps (if any): [LIST].

**Instruction:** From the bug description below, produce a minimal reproduction.

1. Extract the minimum inputs required to trigger the bug.

2. Produce a self-contained script or test (no external services) that fails the moment the bug shows up.

3. If an external dependency is unavoidable, mock it inline.

4. Print a clearly labelled "Observed" and "Expected" at the end.

**Input:**

Bug description:

[PASTE]

Relevant code:

[PASTE]

**Constraints:**

- Under 30 lines if at all possible.

- Deterministic - no randomness unless the bug is in the RNG itself.

- No external services - mock them inline.

**Output Format:**

- The repro in a single code block

- A 2-line "How to run" note

- "Observed vs Expected" summary at the bottom
```
