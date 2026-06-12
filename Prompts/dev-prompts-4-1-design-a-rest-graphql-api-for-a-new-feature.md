---
id: dev-prompts-4-1-design-a-rest-graphql-api-for-a-new-feature
name: "4.1 - Design a REST / GraphQL API for a New Feature"
folder: prompts
section: dev-prompts
summary: "API & Architecture Design"
tags:
  - "dev-prompts"
  - "api & architecture design"
---

# Prompt 4.1 - Design a REST / GraphQL API for a New Feature

> Category: **API & Architecture Design**

When to use  Before implementation, when you need the shape of the request/response and the error model agreed.

Expected output  Endpoints + request/response schemas + error model + versioning note + open questions.

Prompt

```
**Role:** You are a senior engineer who designs APIs from the consumer backwards.

**Context:** Consumers are [LIST - e.g., "internal web app, mobile app, partner integration"]. Auth model: [AUTH]. Versioning style: [URL / HEADER / NONE]. Style constraints in the rest of the system: [NAMING CONVENTIONS, STATUS CODE POLICY, PAGINATION PATTERN].

**Instruction:** Design the API for the feature below.

1. List the consumer stories the API must satisfy (who asks for what, to do what).

2. Propose endpoints - method, path, purpose.

3. For each, sketch request and response schemas with field types.

4. Define the error model (status code + code + message + details).

5. Name the fields using the project's conventions.

6. Flag any assumption with a ⚠️ so it's reviewable.

**Input:**

Feature description:

[PASTE]

Existing endpoint style (1 example):

[PASTE]

**Constraints:**

- No chatty endpoints - N+1 at the API boundary is a red flag, call it out if you see one in your own design.

- Keep the happy-path response under 10 top-level fields where possible.

- Don't expose internal IDs if stable slugs make sense.

**Output Format:**

- Consumer stories

- Endpoint table: Method | Path | Purpose

- Request / response schemas per endpoint

- Error model

- Open questions (⚠️)
```
