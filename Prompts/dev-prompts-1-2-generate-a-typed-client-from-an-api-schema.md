---
id: dev-prompts-1-2-generate-a-typed-client-from-an-api-schema
name: "1.2 - Generate a Typed Client from an API Schema"
folder: prompts
section: dev-prompts
summary: "Code Generation & Scaffolding"
tags:
  - "dev-prompts"
  - "code generation & scaffolding"
---

# Prompt 1.2 - Generate a Typed Client from an API Schema

> Category: **Code Generation & Scaffolding**

When to use  When you have an OpenAPI / JSON schema / endpoint list and need a typed client in the consumer language.

Expected output  A single module exporting a typed client, with retry/timeout defaults and per-endpoint methods.

Prompt

```
**Role:** You are a senior engineer who writes ergonomic SDKs. You optimise for the caller's experience, not the producer's.

**Context:** Consumers of this client are [e.g., "our Next.js frontend and an internal Python CLI"]. They want typed responses, sensible defaults, and the ability to override per call.

**Instruction:** Generate a typed client for the schema below.

1. Produce one method per endpoint, named after the operation.

2. Wrap transport concerns (timeout, retry with jittered backoff, auth header injection) in a single request helper.

3. Expose request/response types next to each method.

4. Include a 10-line usage example at the bottom.

**Input:**

Target language: [LANGUAGE]

Schema / endpoint list:

[PASTE SCHEMA]

**Constraints:**

- No heavy frameworks - single file if possible.

- Fail loud on non-2xx by default, but allow callers to pass { raw: true } to get the Response.

- Do not hand-roll enums the schema already defines - reuse.

**Output Format:**

1. The client module in a single fenced code block.

2. A minimal usage example.

3. A short checklist of what the consumer still needs to wire (env vars, base URL).
```
