---
id: qa-prompts-7-1-the-meta-prompt-write-me-a-prompt-for-testing-task
name: "7.1 - The Meta-Prompt: \"Write Me a Prompt for [Testing Task]\""
folder: prompts
section: qa-prompts
summary: "Meta Prompts"
tags:
  - "qa-prompts"
  - "meta prompts"
---

# Prompt 7.1 - The Meta-Prompt: "Write Me a Prompt for [Testing Task]"

> Category: **Meta Prompts**

When to use  When you need a prompt for a task that isn't covered in this library, or when you want to create a new, reusable prompt for your team. Use this to build prompts, not to do testing tasks directly.

Expected output  A complete, ready-to-use prompt template with [PLACEHOLDER] markers and all 6 parts, ready to add to this library.

Prompt

```
**Role:** You are a prompt engineering expert specializing in creating effective 

prompts for software quality assurance tasks. You design prompts that are clear, 

structured, and immediately usable by QA engineers.

**Context:** The prompt you are creating will be used by QA engineers with varying 

levels of AI experience on [DESCRIBE TESTING CONTEXT - e.g., "a team testing a 

fintech web application" or "a mobile app QA team using Appium"].

**Instruction:** Create a reusable prompt template for the following testing task. 

The prompt must:

1. Follow the 6-part structure: Role, Context, Instruction, Input, Constraints, 

   Output Format

2. Use [PLACEHOLDER] markers wherever the user needs to insert their specific content

3. Include enough specificity to produce useful output without being so rigid that 

   it only works in one narrow scenario

4. Be immediately usable - someone should be able to copy it, fill in the 

   placeholders, and get good output on the first try

**Input:**

Testing task I need a prompt for:

[DESCRIBE THE TASK - be specific about what input you'll have and what output 

you want. Example: "I want a prompt that takes a user story and generates 

exploratory testing notes for a 60-minute session"]

Examples of good output you want the prompt to produce:

[OPTIONAL: Describe or paste an example of what great output looks like]

**Constraints:**

- The prompt should be generalized enough to reuse across different features, 

  not specific to one scenario

- Include a 1-line "When to use" description at the top

- Include an "Expected output" note at the top

- The output format section should be specific - tables, code blocks, or structured 

  sections are better than "respond in a helpful way"

- Add a "Common tweaks" note at the bottom: 2-3 ways users can modify the prompt 

  to adjust the output

**Output Format:**

**When to use:** [1-line description]

**Expected output:** [1-line description]
```
