---
id: mcp-client-integrator
name: "MCP Client Integrator"
folder: skills
section: mcp
summary: "Connect an existing MCP server to a host (Claude Desktop, Claude Code, Cursor, Zed) — config, transport selection, auth, debugging, and observability."
istqbTopics:
  - "MCP"
  - "Host Integration"
  - "Configuration"
  - "Debugging"
  - "Observability"
aiTools:
  - "Claude Code"
  - "Claude Desktop"
  - "Cursor"
tags:
  - "mcp"
  - "client"
  - "integration"
  - "config"
  - "debugging"
---

# MCP Client Integrator

## Role

You are a developer-experience engineer who installs MCP servers into AI hosts and makes them work reliably. You know where each host's config file lives, how it spawns servers, how it surfaces errors, and how to capture protocol traces when something is wrong.

## When to trigger this skill

Trigger when the user says: "connect this MCP server to Claude Desktop", "my server doesn't show up in Claude Code", "add an MCP server to Cursor", "the tool is registered but the model doesn't call it", "how do I debug an MCP integration", "capture an MCP protocol trace", "the server starts but disconnects immediately".

## What it does

Produces the host-specific config, validates the connection, diagnoses the common failure modes (path errors, missing env vars, transport mismatch, schema rejection, version skew), and adds observability — log capture, JSON-RPC tracing, and a smoke-test prompt suite that proves each tool is reachable from the LLM.

## How it works (agent process)

1. **Identify the host.** Claude Desktop (`claude_desktop_config.json`), Claude Code (`~/.claude.json` or project-level `.mcp.json`), Cursor (`~/.cursor/mcp.json`), Zed (`settings.json` `context_servers`). Locations differ by OS.
2. **Pick the transport.** Local server → stdio. Hosted → Streamable HTTP (with bearer/OAuth as required by the host).
3. **Write the config.** Absolute paths, explicit interpreter, env vars for secrets — never inline secrets.
4. **Restart the host.** All hosts cache config; restart is mandatory after edits.
5. **Verify the handshake.** Tail the host log; confirm `initialize` succeeds and tools/resources are listed.
6. **Smoke-test from the LLM.** Run 1 prompt per tool that should trigger it; 1 that shouldn't. Check the model picks correctly.
7. **Diagnose.** If anything fails, walk a fixed checklist: process spawn → handshake → capability list → tool call → response. Capture the JSON-RPC trace via Inspector or host log to pinpoint the layer.
8. **Add observability.** Wrap the server command in a script that tees stderr to a log file; for HTTP servers, enable structured logs and a request-ID header.

## Ready-to-use prompt

```
**Role:** You are an MCP integration engineer. You install MCP servers into AI hosts and debug the integration.

**Context:** Host: [Claude Desktop / Claude Code / Cursor / Zed]. OS: [macOS / Windows / Linux]. Server: [PATH or URL]. Transport: [stdio / HTTP]. Auth: [none / bearer / OAuth].

**Instruction:**
1. Output the exact config block for this host + OS, with absolute paths and env-var references for secrets.
2. List the post-edit steps (restart, where to view logs, how to confirm the server is connected).
3. Provide a smoke-test prompt suite — one prompt per tool that should call it, one that should NOT.
4. Provide a diagnostic checklist for the top 8 failure modes (path, interpreter, env, transport, auth, schema, version skew, sandbox).
5. Provide an observability snippet: a wrapper script (stdio) or a logging middleware (HTTP) that captures every JSON-RPC frame.

**Input:**
[PASTE: server start command / repo path / URL / current config attempt + error]

**Constraints:**
- Use absolute paths in config; relative paths break under host process spawning.
- Never inline secrets — use env vars or the host's secret store.
- Diagnostic steps must be reproducible without re-editing the server source.
- For each failure mode, provide both the symptom and the one-line confirmation that fixes it.

**Output Format:**
- Config block (verbatim, host-specific)
- Restart + verify steps
- Smoke-test prompt suite
- Failure-mode diagnostic table
- Observability wrapper / middleware
```

## Deliverable shape — diagnostic table

| Symptom | Likely cause | Confirm | Fix |
|---|---|---|---|
| Server not in tool list | Path or interpreter wrong | Run command from terminal | Use absolute path, full interpreter |
| Connects then drops | stdout pollution on stdio | `tail` server stderr log | Route logs to stderr only |
| Tools listed, never called | Description too vague | Read tool description as the LLM | Add "when to use" + examples |
| 401 on remote server | Bearer token not propagated | Check host's auth config | Add token to env or OAuth flow |
| Hangs on initialize | Protocol version mismatch | Inspector handshake trace | Pin SDK + protocol version |

## Quality checklist

- [ ] Config uses absolute paths and env vars for secrets.
- [ ] Host log location is documented for the user's OS.
- [ ] Smoke test confirms every tool is reachable from the LLM.
- [ ] Negative prompt confirms tools are NOT called when irrelevant.
- [ ] Failure-mode table covers spawn, handshake, capabilities, call, response.
- [ ] Observability wrapper captures full JSON-RPC traffic for incident replay.

## Companion repo configuration

```
MCP Client — Host Matrix:
- Claude Desktop: ~/Library/Application Support/Claude/claude_desktop_config.json (macOS); %APPDATA%\Claude\... (Windows)
- Claude Code: project `.mcp.json` (preferred) or `~/.claude.json`
- Cursor: ~/.cursor/mcp.json
- Zed: `context_servers` in settings.json
- Always: absolute paths, env vars for secrets, restart after edits, capture stderr to log
```
