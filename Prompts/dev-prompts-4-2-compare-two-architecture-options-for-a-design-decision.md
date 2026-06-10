---
id: dev-prompts-4-2-compare-two-architecture-options-for-a-design-decision
name: "4.2 - Compare Two Architecture Options for a Design Decision"
folder: prompts
section: dev-prompts
summary: "API & Architecture Design"
tags:
  - "dev-prompts"
  - "api & architecture design"
---

# Prompt 4.2 - Compare Two Architecture Options for a Design Decision

> Category: **API & Architecture Design**

When to use  When choosing between technologies (e.g., queue vs stream, sync vs async, library A vs library B) and you need a decision memo.

Expected output  A short ADR-style memo: options, criteria, trade-offs, recommendation, reversibility.

Prompt

```
**Role:** You are a staff engineer who writes decision memos that stand up to scrutiny six months later.

**Context:** The decision is about [DECISION TOPIC]. The broader system is [1-PARAGRAPH CONTEXT]. Scale constraints: [LATENCY / THROUGHPUT / COST]. Team constraints: [SIZE / EXPERIENCE].

**Instruction:** Produce an ADR (Architecture Decision Record) comparing the two options below.

1. State the question in one sentence.

2. List the criteria that actually matter here (avoid generic "scalability" - make them concrete).

3. Score each option against each criterion (+ / 0 / −) with one-line justification.

4. Recommend one with a clear reason.

5. State the reversibility - how painful is it to undo this decision in 6 months?

**Input:**

Option A: [NAME + 1-LINER]

Option B: [NAME + 1-LINER]

**Constraints:**

- Criteria must be specific to this decision, not a generic list.

- No equivocation - pick one.

- If the answer is "it depends", say what it depends on.

**Output Format:**

- ADR Title

- Question

- Criteria (bullet list, concrete)

- Scoring table: Criterion | A | B | Notes

- Recommendation + reason

- Reversibility
```
