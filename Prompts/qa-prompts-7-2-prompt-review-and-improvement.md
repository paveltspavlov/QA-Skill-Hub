---
id: qa-prompts-7-2-prompt-review-and-improvement
name: "7.2 - Prompt Review and Improvement"
folder: prompts
section: qa-prompts
summary: "Meta Prompts"
tags:
  - "qa-prompts"
  - "meta prompts"
---

# Prompt 7.2 - Prompt Review and Improvement

> Category: **Meta Prompts**

When to use  When an existing prompt isn't producing the output quality you want. Paste in your weak prompt and get a diagnosis and an improved version.

Expected output  A diagnosis of what's wrong with the prompt and an improved version that addresses the issues.

Prompt

```
**Role:** You are a prompt engineering expert. You analyze prompts that are 

not producing good output, diagnose the issues, and provide improved versions.

**Context:** The prompt being reviewed is for a [QA/TESTING TASK DESCRIPTION]. 

The AI model being used is [MODEL NAME OR "an LLM-based assistant"].

**Instruction:** Review the prompt below and provide:

1. A diagnosis - what specific weaknesses in the prompt are likely causing 

   poor output? Be specific about which parts of the prompt are problematic.

2. An improved version of the prompt that addresses each issue identified

3. An explanation of each change made and why it improves the output

**Input:**

The weak prompt:

[PASTE YOUR PROMPT HERE]

What was wrong with the output it produced:

[DESCRIBE WHAT WAS BAD - e.g., "too generic," "wrong format," "missed edge cases," 

"hallucinated details," "too long," "ignored the constraints I set"]

Example of the kind of output you actually want:

[OPTIONAL BUT HELPFUL: Show or describe what good output looks like]

**Constraints:**

- Diagnose the root cause of each problem - don't just say "add more detail"

- The improved prompt must use the 6-part structure 

  (Role / Context / Instruction / Input / Constraints / Output Format)

- Explain changes in plain language, not technical prompt engineering jargon

- If the prompt is fundamentally unsalvageable (e.g., the task is too complex 

  for a single prompt), say so and recommend a chaining approach instead

**Output Format:**

**Prompt Diagnosis:**

| Issue # | Problem found | Part of prompt affected | Likely impact on output |

|---|---|---|---|

**Improved Prompt:**

[Complete improved prompt, all 6 parts clearly labeled]

**What changed and why:**

| Change | Reason |

|---|---|

**Estimated improvement:** [Low / Medium / High - with a one-line explanation]
```
