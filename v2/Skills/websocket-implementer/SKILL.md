---
name: websocket-implementer
description: "Use when implementing a real-time client/server message flow."
---

## When to Use
Use for live updates, collaboration, presence, notifications, or bidirectional messaging over WebSocket or an existing abstraction. Do not assume Socket.IO, Redis, delivery guarantees, or event names.

## Required Inputs
Require protocol/library and versions, client/server locations, event schemas, authentication and room/tenant authorization, ordering/delivery needs, reconnect/resume semantics, heartbeat/timeouts, backpressure limits, scaling/deployment topology, and tests.

## Procedure
1. Inspect current transport, auth, event conventions, proxy/load-balancer behavior, and official version-specific docs. Define lifecycle and event contract before coding.
2. Validate every inbound message against a schema and authorize topic/room access on server; define size/rate limits and correlation/version fields only when required.
3. Handle connect, auth failure, message, heartbeat, reconnect, close and cleanup explicitly. Use bounded backoff and expose terminal offline/error state; define replay/cursor strategy only if server supports it.
4. Bound queues/buffers and decide what to drop, coalesce, persist or reject under backpressure. Keep sensitive payloads out of logs.
5. Test auth/tenant isolation, malformed and oversized messages, disconnect/reconnect, duplicates/order assumptions, backpressure, cleanup and rolling deploy compatibility; verify with local integration test or protocol inspector if available.

## Output Contract
Return: **Protocol/library/version**; **Connection lifecycle**; **Typed event schema**; **Authentication/authorization and room/channel scope**; **Presence or client hook** only when requested; **Reconnect/replay/backpressure policy**; **Scaling assumptions**; **Files/deployment changes**; **Failure tests and results**. State guarantees as implemented, not hoped for; distinguish transport-level delivery from application acknowledgment.

## Quality Gate
No cross-tenant event leakage or unvalidated message mutation. Reconnection does not imply event recovery unless a verified cursor/replay mechanism exists. Timers/listeners are cleaned up and resource limits are explicit. Do not claim exactly-once, ordered delivery, or horizontal scaling without system-level evidence. Verify protocol/library semantics in official docs for deployed version.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
