---
id: qa-prompts-2-4-generate-exploratory-testing-charters
name: "2.4 - Generate Exploratory Testing Charters"
folder: prompts
section: qa-prompts
summary: "Test Case Design"
tags:
  - "qa-prompts"
  - "test case design"
---

# Prompt 2.4 - Generate Exploratory Testing Charters

> Category: **Test Case Design**

When to use  When planning an exploratory testing session. Gives exploratory testers a structured mission rather than leaving them to "just test everything."

Expected output  A set of time-boxed exploratory testing charters covering different risk areas and testing dimensions.

Prompt

```
**Role:** You are a skilled exploratory testing practitioner using session-based 

test management. You design charters that give testers clear missions while 

leaving room for discovery.

**Context:** The feature or area being explored is [FEATURE/AREA NAME] in 

[SYSTEM DESCRIPTION]. The risk areas of most concern are: 

[LIST KEY RISK AREAS - e.g., "data integrity, authentication bypass, mobile 

responsiveness, performance under load"].

**Instruction:** Create a set of exploratory testing charters for the feature 

described below. Each charter should follow the SBTM (Session-Based Test Management) 

format:

- Area: what part of the system

- Mission (Charter): what to explore and why

- Environment/Setup: what's needed before starting

- Time box: suggested duration

- Risks/Concerns: what could go wrong in this area

- Potential oracles: how to recognize a problem when you find one

- Notes to capture: what information to record during the session

**Input:**

Feature description:

[PASTE FEATURE DESCRIPTION, USER STORY, OR SPECIFICATION]

Known high-risk areas:

[LIST OR DESCRIBE THE AREAS OF GREATEST CONCERN]

**Constraints:**

- Generate 5-7 charters covering different dimensions (functional, usability, 

  security, performance, data integrity, integration, accessibility)

- Each charter should be completable in a 60-90 minute session

- Charters should not overlap significantly

- Write in plain language - charters will be given to testers with varying experience

**Output Format:**

---

**Charter #[N]**

**Area:** [System area]

**Mission:** Explore [what] to discover [what types of problems]

**Time Box:** [X minutes]

**Setup:** [What's needed]

**Key Questions to Answer:** [Bullet list]

**Oracles (how to recognize a problem):** [Bullet list]

**Risks this charter addresses:** [Bullet list]

---
```
