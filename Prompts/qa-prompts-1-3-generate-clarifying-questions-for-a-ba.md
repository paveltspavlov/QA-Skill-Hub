---
id: qa-prompts-1-3-generate-clarifying-questions-for-a-ba
name: "1.3 - Generate Clarifying Questions for a BA"
folder: prompts
section: qa-prompts
summary: "Requirements Analysis"
tags:
  - "qa-prompts"
  - "requirements analysis"
---

# Prompt 1.3 - Generate Clarifying Questions for a BA

> Category: **Requirements Analysis**

When to use  When you have identified gaps in requirements and need a structured, professional list of questions to bring to a BA, PO, or business stakeholder meeting.

Expected output  Prioritized question list grouped by topic, professional in tone, ready to paste into a meeting invite or Jira comment.

Prompt

```
**Role:** You are a QA lead preparing for a requirements review meeting with the 

product owner and business analyst. You communicate in a collaborative, professional 

tone - you ask questions to clarify, not to challenge.

**Context:** The team is building [FEATURE/MODULE NAME] for [SYSTEM DESCRIPTION]. 

The following gaps and ambiguities have been identified in the current requirements.

**Instruction:** Based on the requirements gaps listed below, generate a prioritized 

list of clarifying questions to ask at the next BA/PO review session. 

Organize questions by topic area. For each question, include:

- The question itself

- Why it matters for testing (one sentence)

- The risk if it goes unanswered (one sentence)

**Input:**

Requirements document or story: [PASTE HERE]

Known gaps or ambiguities (from Prompt 1.2 or your own analysis):

[PASTE GAP LIST HERE, or describe gaps in bullet points]

**Constraints:**

- Write questions as a QA colleague would ask them in a meeting - direct but non-confrontational

- Prioritize questions by impact: High (blocks testing) / Medium (creates uncertainty) / 

  Low (nice to know)

- Group related questions together under a topic heading

- Maximum 15 questions total

**Output Format:**

# Clarifying Questions for [FEATURE NAME] - [DATE]

*Prepared by QA for BA/PO review*

## [Topic Group 1 - e.g., "Error Handling"]

**[Priority: HIGH/MEDIUM/LOW]**

**Q1:** [Question]

- *Why it matters:* [One sentence]

- *Risk if unanswered:* [One sentence]

[Repeat for each question]

---

*Total: [X] High priority | [X] Medium | [X] Low*
```
