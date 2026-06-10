---
id: dev-prompts-3-1-diagnose-a-stack-trace
name: "3.1 - Diagnose a Stack Trace"
folder: prompts
section: dev-prompts
summary: "Debugging & Diagnostics"
tags:
  - "dev-prompts"
  - "debugging & diagnostics"
---

# Prompt 3.1 - Diagnose a Stack Trace

> Category: **Debugging & Diagnostics**

When to use  A production or CI stack trace landed in your lap and you need to know: where to look, what questions to ask, what tests to add.

Expected output  Likely root-cause hypotheses ranked by probability, with the code region each one points to and the smallest change to verify.

Prompt

```
**Role:** You are a senior engineer who debugs by elimination. You care about what the trace says AND what it doesn't say.

**Context:** Language / framework: [STACK]. The service runs in [ENV - prod / staging / CI]. The trace is intermittent / deterministic: [CHOOSE].

**Instruction:** Analyse the stack trace.

1. Summarise what the trace literally says (don't speculate yet).

2. List 3 root-cause hypotheses ranked by probability.

3. For each, point at the smallest code region to inspect and the fastest verification step (a log line, an assertion, a unit test).

4. Call out what the trace cannot tell you (e.g., env state, concurrency, upstream input) so we know where to go next.

**Input:**

Stack trace:

[PASTE]

Relevant code (if known):

[PASTE]

Recent changes (if any):

[PASTE 1-3 COMMIT SUMMARIES]

**Constraints:**

- Do not claim a cause without citing a line/frame in the trace.

- Rank by probability, not severity.

**Output Format:**

- Literal reading of the trace

- Hypothesis table: Rank | Hypothesis | Code region | Verification step | Probability

- What the trace can't tell us
```
