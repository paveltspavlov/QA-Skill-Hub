---
id: dev-prompts-4-3-data-model-schema-design-from-requirements
name: "4.3 - Data Model / Schema Design from Requirements"
folder: prompts
section: dev-prompts
summary: "API & Architecture Design"
tags:
  - "dev-prompts"
  - "api & architecture design"
---

# Prompt 4.3 - Data Model / Schema Design from Requirements

> Category: **API & Architecture Design**

When to use  You have a requirements doc and need a relational schema or NoSQL document shape before writing code.

Expected output  Entities, fields, relationships, index candidates, and a list of decisions worth escalating.

Prompt

```
**Role:** You are a data-aware engineer who treats schema design as an API - it outlives the code.

**Context:** Target store: [RELATIONAL / DOCUMENT / KEY-VALUE / GRAPH - plus specific engine]. Read / write ratio expectation: [E.G., "read-heavy, 95/5"]. Key access patterns: [LIST].

**Instruction:** Design the data model.

1. Extract entities and their attributes from the requirements.

2. Define relationships (1:1 / 1:N / N:M) and the ownership direction.

3. Propose primary keys and candidate indexes for the named access patterns.

4. Call out any denormalisation and why it's justified.

5. Flag any decision the team should review - naming, PK strategy, soft delete, audit fields.

**Input:**

Requirements:

[PASTE]

Key access patterns:

[LIST]

**Constraints:**

- Do not invent entities the requirements don't imply.

- Name tables / collections in the project's chosen style.

- Don't silently add a `deleted_at` - flag it as a decision.

**Output Format:**

- Entities (table / collection per entity with fields + types)

- Relationships diagram (ASCII or Mermaid)

- Indexes per access pattern

- Denormalisations (with justification)

- Decisions worth escalating
```
