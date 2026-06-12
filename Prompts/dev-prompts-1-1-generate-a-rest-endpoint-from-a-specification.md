---
id: dev-prompts-1-1-generate-a-rest-endpoint-from-a-specification
name: "1.1 - Generate a REST Endpoint from a Specification"
folder: prompts
section: dev-prompts
summary: "Code Generation & Scaffolding"
tags:
  - "dev-prompts"
  - "code generation & scaffolding"
---

# Prompt 1.1 - Generate a REST Endpoint from a Specification

> Category: **Code Generation & Scaffolding**

When to use  When you have an OpenAPI-like description or an acceptance criterion and need a working endpoint with validation and tests.

Expected output  A runnable controller/handler + input validation + happy-path + 2 edge-case tests, using the project's conventions.

Prompt

```
**Role:** You are a senior backend engineer with deep experience in [LANGUAGE/FRAMEWORK - e.g., "Python + FastAPI" or "TypeScript + NestJS"].

**Context:** The codebase is [BRIEF ARCHITECTURE - e.g., "a modular monolith with service + repository layers; errors are raised as domain exceptions and mapped to HTTP in a central handler"]. Auth is handled via [AUTH MECHANISM]. The ORM is [ORM].

**Instruction:** Generate a new endpoint that satisfies the specification below. Think step by step:

1. Infer the full request and response contracts (including error shapes).

2. Write the handler using the project's existing patterns - do not introduce new layers.

3. Add request validation at the boundary.

4. Write one happy-path test and two edge-case tests (invalid input; authorisation failure).

**Input:**

Specification:

[PASTE SPEC OR USER STORY]

Related existing file(s) to match style:

[PASTE 1-2 SHORT FILES OR LINK]

**Constraints:**

- Do not invent new infrastructure (no new logger, no new exception types unless justified).

- If a dependency is unclear, mark it with // TODO(human): and keep going.

- Keep the handler thin - business logic goes to the service layer.

**Output Format:**

1. File tree of changes (paths only).

2. Each file in its own fenced code block, full contents.

3. A short "Assumptions & open questions" list at the end.
```
