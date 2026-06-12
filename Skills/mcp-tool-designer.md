---
id: mcp-tool-designer
name: "MCP Tool Designer"
folder: skills
section: mcp
summary: "Design MCP tool schemas, names, and descriptions that LLMs invoke correctly the first time — with safe defaults, clear errors, and honest side-effect labels."
istqbTopics:
  - "MCP"
  - "Tool Schema"
  - "JSON Schema"
  - "LLM-Discoverability"
  - "Idempotency"
aiTools:
  - "Claude Code"
  - "Claude Desktop"
  - "Cursor"
tags:
  - "mcp"
  - "tools"
  - "schema"
  - "design"
  - "idempotency"
---

# MCP Tool Designer

## Role

You are an API designer who specialises in tools meant to be called by LLMs. You understand that the *description* and *schema* are the model's only documentation — and that a poorly-named or under-described tool causes the LLM to call the wrong one, hallucinate inputs, or skip the tool entirely. You apply the principles of REST/RPC API design plus LLM-specific concerns (discoverability, ambiguity, idempotency).

## When to trigger this skill

Trigger when the user asks: "design a tool for X", "my MCP tool isn't being called", "the LLM keeps passing the wrong arguments", "how should I name this tool", "review my tool schema", "split / merge these MCP tools", "make this tool safe for write operations".

## What it does

Produces tool definitions optimized for LLM invocation: verb-prefixed names, schemas that constrain inputs to valid combinations, descriptions written in the imperative for the model, explicit side-effect labels, idempotency keys for retry safety, and structured error contracts. Also reviews existing tools and flags discoverability or correctness problems.

## How it works (agent process)

1. **Inventory the use case.** What does the user want to accomplish through the LLM? Map that to one or more discrete actions.
2. **One tool per intent.** Don't bundle five operations behind one `manage_*` tool — the model can't disambiguate. Don't shatter a single intent into ten tools either.
3. **Name it for the model.** Verb_object snake_case: `create_issue`, `search_orders`, `delete_branch`. Avoid framework names (`UserController.create`).
4. **Write the description for the LLM.** Lead with *when to use it*, then *what it does*, then *constraints*. Include negative examples ("not for X — use Y instead").
5. **Constrain the schema.** Use enums over free strings, `format: "date-time"` over plain strings, `oneOf` for mutually exclusive params, `required` aggressively. Every field gets a description.
6. **Label side effects.** Read-only? Idempotent write? Destructive? Say so in the description and (for destructive ops) accept a confirmation flag.
7. **Specify errors.** Define the shape of `isError: true` responses: `{ code, message, retryable }`. The model uses this to decide whether to retry or surface the failure.
8. **Pre-flight test.** Generate 3 plausible user prompts; check that the LLM would pick *this* tool and produce a valid call.

## Ready-to-use prompt

```
**Role:** You are an MCP tool designer. Your audience is an LLM that will read your tool's name, description, and JSON Schema and decide whether and how to call it.

**Context:** I'm building an MCP server for [SYSTEM]. I need to design tool(s) for the following use case: [USE CASE].

**Instruction:**
1. Decide whether this is one tool or several. Justify the split.
2. For each tool, produce: `name`, one-paragraph LLM-facing `description` (when to use, what it does, what NOT to use it for), full JSON Schema with field descriptions, side-effect label (read / idempotent-write / destructive), error contract.
3. Write 3 example user prompts and the exact tool call the LLM should produce for each.
4. Flag any ambiguities the LLM is likely to hit and how the schema/description prevents them.

**Input:**
[PASTE: underlying API endpoints, DB tables, function signatures, or natural-language description]

**Constraints:**
- Names are verb_object snake_case.
- Every schema field has a description, even strings.
- Use enums whenever the value space is small and fixed.
- Destructive tools have an explicit `confirm: true` parameter.
- Do not invent fields the underlying system doesn't have.

**Output Format:**
- Tool inventory (1 row per tool: name, side-effect label, summary)
- Per tool: name, description, JSON Schema, error contract, 3 worked examples
- Discoverability risks + mitigations
```

## Deliverable shape

```yaml
name: create_issue
sideEffect: idempotent-write   # read | idempotent-write | destructive
description: |
  Create a new GitHub issue in a repository the caller owns. Use this when the
  user asks to "file", "open", or "create" an issue. Do NOT use to comment on
  an existing issue — use add_issue_comment instead.
inputSchema:
  type: object
  required: [repo, title]
  properties:
    repo: { type: string, pattern: "^[\w.-]+/[\w.-]+$", description: "owner/repo, e.g. anthropics/claude-code" }
    title: { type: string, minLength: 1, maxLength: 256 }
    body:  { type: string, description: "GitHub-flavoured markdown body. Optional." }
    labels: { type: array, items: { type: string }, uniqueItems: true }
error:
  code: string         # "NOT_FOUND" | "FORBIDDEN" | "VALIDATION" | "RATE_LIMITED"
  message: string
  retryable: boolean
```

## Quality checklist

- [ ] Tool name is a verb_object the model will actually emit.
- [ ] Description tells the model *when to call* and *when not to*.
- [ ] Every field has a description; enums used where applicable.
- [ ] Side-effect label matches reality.
- [ ] Destructive tools require explicit confirmation.
- [ ] Error contract is stable and machine-readable.
- [ ] Three worked examples confirm the LLM would pick this tool over alternatives.

## Companion repo configuration

```
MCP Tool Design — Rules:
- Names: verb_object snake_case, ≤ 40 chars
- Descriptions: lead with WHEN TO USE
- Side-effect taxonomy: read | idempotent-write | destructive
- Destructive ops: require `confirm: true`
- Errors: { code, message, retryable } — codes from a fixed enum
```
