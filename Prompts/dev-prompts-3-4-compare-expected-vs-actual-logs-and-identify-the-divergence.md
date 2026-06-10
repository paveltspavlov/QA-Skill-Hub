---
id: dev-prompts-3-4-compare-expected-vs-actual-logs-and-identify-the-divergence
name: "3.4 - Compare Expected vs Actual Logs and Identify the Divergence"
folder: prompts
section: dev-prompts
summary: "Debugging & Diagnostics"
tags:
  - "dev-prompts"
  - "debugging & diagnostics"
---

# Prompt 3.4 - Compare Expected vs Actual Logs and Identify the Divergence

> Category: **Debugging & Diagnostics**

When to use  You have two runs of the same flow - one succeeded, one failed - and need to find where they diverged.

Expected output  A side-by-side divergence point + the surrounding code + a hypothesis for why.

Prompt

```
**Role:** You are an engineer who treats logs like a crime-scene diff.

**Context:** Language / framework: [STACK]. Log format: [JSON / plain text / other]. The runs share the same inputs / differ by [WHAT].

**Instruction:** Compare the two log excerpts below.

1. Align them by operation or timestamp - be explicit about how.

2. Identify the first divergent step.

3. Map that step back to the code region responsible for it.

4. Propose one hypothesis for the divergence - state + evidence.

**Input:**

Successful run log:

[PASTE]

Failed run log:

[PASTE]

Relevant code (if known):

[PASTE]

**Constraints:**

- Identify the FIRST divergence, not a subsequent symptom.

- Use log line numbers or timestamps as evidence.

**Output Format:**

- Alignment note

- Divergence point (both lines quoted)

- Code region responsible

- Hypothesis
```
