---
name: mcp-client-integrator
description: "Connect an existing MCP server to a supported host using an explicit transport, identity, and permission model. Use when configuring or troubleshooting an MCP client."
---

# MCP Client Integrator

## Procedure
1. Identify host/client version, server endpoint or command, transport, authentication, and required capabilities.
2. Configure only needed servers/tools; use the host's documented format and protect credentials outside checked-in files.
3. Verify initialization and tool discovery before calls. Start with read-only tools and confirm scope/consent behavior.
4. Test representative calls, malformed results, timeout/disconnect, and server restart; inspect logs without exposing secrets.
5. Document config location, restart requirements, capability differences, and troubleshooting for that host.

## Output
A minimal integration configuration and verified connection/discovery steps, with host-specific limits stated.

## References
- [MCP specification](https://modelcontextprotocol.io/specification/latest)
