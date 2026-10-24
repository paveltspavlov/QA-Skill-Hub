---
name: mcp-server-developer
description: "Build or extend a Model Context Protocol server using the official SDK and explicit tool/resource/prompt contracts. Use when exposing a system to MCP-capable hosts."
---

# MCP Server Developer

## Procedure
1. Define the host use case and choose only needed MCP primitives: tools, resources, and/or prompts.
2. Specify each tool's name, description, JSON input schema, output, error behavior, and side effects.
3. Implement using the project's language and official SDK; handle initialization, capability discovery, validation, cancellation, and errors.
4. Keep credentials out of source and logs. Require human approval for consequential actions and enforce authorization at the server boundary.
5. Test discovery/calls, invalid input, errors, transport, and safe shutdown; document host configuration and limitations.

## Output
A server design or implementation with tool contracts, permission boundaries, and protocol tests.

## References
- [MCP specification](https://modelcontextprotocol.io/specification/latest)
