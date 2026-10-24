---
name: websocket-implementer
description: "Implement real-time messaging over WebSockets using the project's protocol, authorization, and event conventions. Use when a client and server exchange live messages."
---

# WebSocket Implementer

## Procedure
1. Define connection lifecycle, message schema, authentication, authorization, ordering, reconnect, heartbeat, and delivery guarantees.
2. Validate incoming messages and enforce size/rate limits. Handle open, message, error, and close states explicitly.
3. Clean up timers/listeners on close; implement bounded retries with backoff and an observable terminal state.
4. Account for buffering/backpressure limitations and define what happens if producers outpace consumers.
5. Test disconnects, malformed messages, duplicate delivery, authorization, and resource cleanup.

## Output
A WebSocket client/server change or protocol plan with lifecycle and failure tests.

## References
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
