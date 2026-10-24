---
name: mcp-server-tester
description: "Test MCP server discovery and tool contracts across supported transports. Use when validating MCP behavior before connecting a host or exposing tools."
---

# MCP Server Tester

## Procedure
1. Confirm server version, capabilities, transport, authorization, and test environment.
2. Verify initialization and capability listing, then test valid, invalid, boundary, and unauthorized inputs for each tool.
3. Check result structure, error signaling, pagination/notifications where applicable, cancellation, and cleanup.
4. Verify side-effecting tools require consent and returned data respects authorization scope.
5. Test only against a controlled server/host; never probe a production service without authorization.

## Output
A protocol/contract test matrix with requests, expected results, findings, and unsupported areas.

## References
- [MCP specification](https://modelcontextprotocol.io/specification/latest)
