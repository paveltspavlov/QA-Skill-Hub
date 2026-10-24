---
name: mcp-tool-designer
description: "Design MCP tool names, descriptions, schemas, and side-effect boundaries so hosts can invoke tools safely and predictably. Use before implementing a tool server."
---

# MCP Tool Designer

## Procedure
1. Express the user outcome as small atomic operations; avoid one oversized tool that mixes unrelated actions.
2. Give each tool a unique name and description stating purpose, required inputs, output, and limits.
3. Use precise JSON Schema: required fields, types, enums, bounds, and clear validation errors.
4. Make read-only versus consequential writes explicit; require confirmation for destructive or irreversible actions.
5. Review examples against expected prompts and test ambiguous/invalid arguments before publishing.

## Output
A tool catalog with schemas, examples, error cases, and side-effect/confirmation notes.

## References
- [MCP specification](https://modelcontextprotocol.io/specification/latest)
