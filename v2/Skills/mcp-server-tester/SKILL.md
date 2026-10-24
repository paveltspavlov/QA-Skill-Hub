---
name: mcp-server-tester
description: "Test MCP server discovery and tool contracts across supported transports. Use when validating MCP behavior before connecting a host or exposing tools."
---

# MCP Server Tester

## When to Use
Use to validate a Model Context Protocol (MCP) server's initialization, advertised capabilities, tool schemas, results/errors, transport behavior, and host integration. Protocol specifics evolve; use the version the server declares and the current official specification for consequential assertions.

## Required Inputs
Confirm SDK/server version, protocol revision, advertised tools/resources/prompts, input schemas, transport (stdio or supported HTTP mode), host/client version, auth boundary, expected side effects, test harness and command, and controlled environment. Obtain explicit authorization for live systems and use synthetic data where possible.

## Procedure
1. Inventory every advertised capability and map it to implementation and intended access. Preserve raw JSON-RPC request/response evidence with secrets removed.
2. Verify initialization/capability negotiation and supported method flows against selected protocol version. Test each advertised tool with schema-derived valid, missing, wrong-type, boundary, and unauthorized inputs; derive limits only from schemas or explicit contracts.
3. Check result shape, error signaling, notifications/pagination where applicable, cancellation, timeout, and transport framing/reconnect behaviors only if supported by version/transport. Do not rely on old transport assumptions.
4. For malformed envelopes, use a bounded local harness and verify the server reports protocol-appropriate errors and remains available; avoid unbounded fuzzing. Test side-effecting operations only with disposable data and explicit approval.
5. Test host integration (for example Inspector or a named client) separately from protocol conformance. Record host/model prompt routing as integration evidence, not a protocol guarantee.
6. Report missing advertised implementations, extra undocumented access, data leakage, or result ambiguity; include exact safe reproducer and cleanup.

## Output Contract
Coverage table `Capability/tool | Protocol revision | Transport | Happy | Invalid/boundary | Auth/side-effect | Result/error oracle | Status`; findings table `ID | Layer | Request/payload | Expected | Actual | Severity | Evidence | Fix`. Status values `PASS`, `FAIL`, `BLOCKED`, `NOT TESTED`. Example: `lookup_item | declared schema requires id:string | stdio | valid ID | missing id | unauthorized scope if contract defines it | schema error response | NOT TESTED` until executed; payloads must not include secrets.

## Quality Gate
Every advertised capability is accounted for; expected results follow selected specification/schema; tool side effects are authorized; protocol and host tests are distinguished; fuzz scope is bounded; exact execution status and unsupported cases are disclosed. Verify syntax and behavior against official MCP specification/SDK docs for the version in use.

## Evidence and Uncertainty
Use declared server version, raw exchanges, harness output, and official versioned protocol docs. Apply evidence readiness: clear scope, traceable claims, complete contract, relevant verification each evidenced (25 points). Below 75/100, ask, qualify, or abstain; no guessed confidence percentage. Critical authorization, privacy, safety, or acceptance failures block readiness.
