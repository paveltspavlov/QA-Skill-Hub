---
id: qa-prompts-7-3-evaluate-ai-output-quality
name: "7.3 - Evaluate AI Output Quality"
folder: prompts
section: qa-prompts
summary: "Meta Prompts"
tags:
  - "qa-prompts"
  - "meta prompts"
---

# Prompt 7.3 - Evaluate AI Output Quality

> Category: **Meta Prompts**

When to use  When you have AI-generated test artifacts and want a structured quality review before committing them to your test suite or documentation.

Expected output  A scored quality assessment of the AI output with specific items flagged for correction, and an overall recommendation (use as-is / edit and use / regenerate).

Prompt

```
**Role:** You are a senior QA engineer reviewing AI-generated testing artifacts 

for quality, accuracy, and usefulness. You apply the same critical eye you'd 

apply to a junior colleague's first draft.

**Context:** The artifact being reviewed is [ARTIFACT TYPE - e.g., "AI-generated 

test cases," "AI-generated BDD scenarios," "AI-generated bug report," 

"AI-generated test data"]. It was generated for [FEATURE/SYSTEM DESCRIPTION].

**Instruction:** Review the AI-generated artifact below using these quality dimensions:

1. **Accuracy** - Are facts, field names, endpoints, business rules correct?

2. **Relevance** - Does it actually address the task, or did the AI drift 

   toward a generic/easier version?

3. **Completeness** - Are edge cases covered? Are important scenarios missing?

4. **Consistency** - Does the artifact contradict itself anywhere?

5. **Executability** - For test cases: are steps specific enough to execute? 

   For code: will it run?

6. **Hallucination check** - Are there any invented facts, made-up endpoints, 

   or fabricated business rules?

Score each dimension 1-5 (1 = unusable, 5 = excellent).

**Input:**

The original prompt used to generate this artifact:

[PASTE PROMPT]

The AI-generated artifact to review:

[PASTE AI OUTPUT]

Reference material (requirements, specs, or system knowledge to check against):

[PASTE RELEVANT REFERENCE MATERIAL, OR DESCRIBE WHAT YOU KNOW ABOUT THE SYSTEM]

**Constraints:**

- Be specific: flag exact lines or items that have quality issues, 

  don't give general feedback

- Separate what is definitely wrong from what might need verification

- Provide specific correction text for each flagged issue (don't just say 

  "this is wrong" - say what it should be)

**Output Format:**

**Quality Assessment Summary**

| Dimension | Score (1-5) | Key Observations |

|---|---|---|

| Accuracy | | |

| Relevance | | |

| Completeness | | |

| Consistency | | |

| Executability | | |

| Hallucination Risk | | |

| **Overall** | | |

**Specific Issues Found:**

| # | Item/Line | Issue Type | What's wrong | Suggested correction |

|---|---|---|---|---|

**Missing elements:**

[List anything important that the AI failed to include]

**Recommendation:**

- [ ] Use as-is - quality is high enough, minor polish only

- [ ] Edit and use - specific fixes identified above, addressable without regenerating

- [ ] Regenerate - fundamental quality issues, improved prompt recommended

**Prompt improvement suggestion:**

[If regeneration is recommended: what specific change to the prompt would address 

the root cause of the quality issues?]

Contributing New Prompts

This is a living document. When you discover a prompt that works well in real QA work, add it to the right category using the template below. Keep the 6-part structure - the consistency is what makes the library browsable and the outputs predictable.

Prompt template

### Prompt [CATEGORY].[N] - [Descriptive Name]

**When to use:** [1 line description of the trigger situation]

**Expected output:** [1 line description of the shape of the response]

**Role:** You are a [role with relevant expertise and years].

**Context:** [The system, feature, or data this task sits inside.]

**Instruction:** [Numbered reasoning steps the AI must follow.]

**Input:** [The user story / requirement / code / data to process.]

**Constraints:**

- [Output shape, length, or forbidden moves]

- [Assumption rules - e.g. flag unknowns, do not invent]

**Output Format:** [Exact structure - table, JSON schema, Gherkin, etc.]

Quality checklist before you commit a new prompt

All 6 parts are filled in - even if Constraints is just one line.

Placeholders are clearly in [SQUARE_BRACKETS] so a teammate can spot them.

You ran the prompt at least twice against different inputs and the output stayed on-format.

The Output Format block would tell a reviewer what 'correct' looks like without guessing.

The prompt names a persona - not just 'you are helpful'.
```
