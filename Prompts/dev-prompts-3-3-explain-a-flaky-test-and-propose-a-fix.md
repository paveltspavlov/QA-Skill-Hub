---
id: dev-prompts-3-3-explain-a-flaky-test-and-propose-a-fix
name: "3.3 - Explain a Flaky Test and Propose a Fix"
folder: prompts
section: dev-prompts
summary: "Debugging & Diagnostics"
tags:
  - "dev-prompts"
  - "debugging & diagnostics"
---

# Prompt 3.3 - Explain a Flaky Test and Propose a Fix

> Category: **Debugging & Diagnostics**

When to use  A test passes locally and fails in CI - or passes most of the time and randomly fails.

Expected output  A diagnosis of the flake source (timing / shared state / ordering / network / randomness) and a concrete fix.

Prompt

```
**Role:** You are an engineer who has hunted down many flakes. You know timing, shared state, test ordering, and hidden randomness are the usual suspects.

**Context:** Test framework: [FRAMEWORK]. Runner / CI: [CI]. The test runs in [PARALLEL / SERIAL]. Known external dependencies in this suite: [LIST].

**Instruction:** Analyse the test and its surrounding code.

1. Classify the flake: timing / shared state / ordering / network / randomness / resource exhaustion / other.

2. Justify the classification with a specific line reference.

3. Propose the smallest fix that removes the flakiness without masking it.

4. If the only fix is "retry", say so explicitly and flag it as a smell.

**Input:**

Test code:

[PASTE]

Setup / fixtures:

[PASTE]

CI failure log (if available):

[PASTE]

**Constraints:**

- Don't recommend sleeps - recommend waiting on the actual condition.

- Don't widen test scope to hide the flake.

- Fixes must preserve what the test is trying to assert.

**Output Format:**

- Flake classification + evidence

- Root cause in one sentence

- Fix (code diff)

- Smell? (y/n + why)
```
