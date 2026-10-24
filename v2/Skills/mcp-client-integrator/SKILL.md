---
name: mcp-client-integrator
description: "Use when connecting an MCP server to a specified host and transport."
---

## When to Use
Use to configure or diagnose an MCP host/client integration for a known server, tool set, and target host. Do not assume one host’s config path or restart behavior applies to another.

## Required Inputs
Require host name/version and OS, server command or endpoint, transport, protocol/SDK version if known, environment/secret references, required tools/resources, host logs or error output, and authorization boundary. Never request or output credential values.

## Procedure
1. Confirm target host’s current official MCP configuration and transport docs plus server compatibility; separate host version from protocol/SDK version.
2. Inspect server entry point, required arguments/env names, working directory, permissions, and transport. For stdio, keep protocol stdout free of logs; use stderr. For HTTP, verify auth/TLS and origin policy from docs.
3. Produce a host-specific config using absolute executable paths where host process-spawn semantics require them; reference secrets by variable/store, never inline. Do not claim restart/cache behavior without host documentation.
4. Apply only with authorization; restart/reload only if documented. Verify initialize/capabilities and exercise one intended tool plus a negative case; inspect redacted logs.
5. Diagnose spawn, transport, auth, schema/version, and capability errors separately; redact frames containing user data or tokens.

## Output Contract
Return: **Host/OS/version and source**; **Transport and compatibility**; **Config block** with placeholders/env refs; **Apply/reload steps** backed by host docs; **Smoke-test prompts and expected capability**; **Diagnostic table** (symptom, safe check, fix); **Verification**. Never include real secrets or raw sensitive protocol frames.

## Quality Gate
Config matches the named host schema/version, paths and environment are valid, and each expected tool is discoverable only after a live check. Do not log or replay credentials/user payloads. Negative prompt tests ensure irrelevant requests do not invoke tools where observable. If host version/config semantics are unknown, ask or label the snippet illustrative rather than claiming it works.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
