---
id: dev-prompts-1-3-scaffold-a-new-module-with-tests
name: "1.3 - Scaffold a New Module with Tests"
folder: prompts
section: dev-prompts
summary: "Code Generation & Scaffolding"
tags:
  - "dev-prompts"
  - "code generation & scaffolding"
---

# Prompt 1.3 - Scaffold a New Module with Tests

> Category: **Code Generation & Scaffolding**

When to use  Starting a new domain concept (entity + service + tests) inside an existing codebase.

Expected output  Entity / service / repository / test skeleton with TODO markers for domain rules.

Prompt

```
**Role:** You are a senior engineer bootstrapping a new module inside a mature codebase. You respect existing conventions before inventing new ones.

**Context:** Tech stack: [STACK]. Project layout: [e.g., "src/modules/<name>/{domain,application,infrastructure,interface}"]. Test framework: [FRAMEWORK].

**Instruction:** Create a new module called [MODULE_NAME] that owns the concept of [BUSINESS_CONCEPT].

1. Propose the file tree mirroring the existing layout exactly.

2. Generate an entity + one representative use case (create/update/query).

3. Generate matching unit tests that cover happy path + one invalid input.

4. Use `// TODO(human):` where domain rules need input.

**Input:**

Existing module to mirror:

[PASTE ONE EXISTING MODULE TREE]

Business concept:

[1-2 SENTENCES]

**Constraints:**

- No magic helpers imported from outside the module.

- Unit tests must run without network or DB - use in-memory fakes.

- Keep the entity free of framework imports.

**Output Format:**

1. File tree.

2. Each file in its own code block.

3. A "What's intentionally not covered" note.
```
