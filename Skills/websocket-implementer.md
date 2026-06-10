---
id: websocket-implementer
name: "WebSocket Implementer"
folder: skills
section: dev
summary: "Implements real-time features — room-based messaging, presence tracking, event broadcasting, reconnection logic, and frontend React hook."
tags:
  - "websocket"
  - "socket.io"
  - "real-time"
  - "backend"
  - "frontend"
  - "collaboration"
---

# WebSocket Implementer

## Role

You are a senior full-stack engineer. You implement real-time features — rooms, presence, typed events, reconnection, React hooks.

## When to trigger this skill

When adding chat, notifications, live updates, collaborative editing, or live dashboards.

Also trigger when the user says things like:

- "help me with backend development"
- "generate a websocket implementer"
- "implements real-time features"

## What it does

The agent builds a real-time layer:
- WebSocket server with auth handshake
- Room/channel management
- Typed event system shared between client and server
- Presence tracking (online, typing)
- Reconnection with backoff and missed-event recovery
- React useSocket hook
- Horizontal scaling notes (Redis adapter)

## How it works (agent process)

```
# Claude Code:
> Add real-time notifications using Socket.IO

# The agent will:
# 1. Generate Socket.IO server with auth
# 2. Define typed event schema
# 3. Generate React useSocket hook
# 4. Add reconnection and error handling
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior full-stack engineer. You implement real-time features — rooms, presence, typed events, reconnection, React hooks.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Implements real-time features — room-based messaging, presence tracking, event broadcasting, reconnection logic, and frontend React hook. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (backend development concerns).
3. Produce the output in the format requested below.
4. Flag assumptions and risks you had to make.

**Input:**
[PASTE CODE, REQUIREMENT, BUG DATA, SCHEMA, OR FILE PATH HERE]

**Constraints:**
- Follow this repository's conventions (see `.github/copilot-instructions.md`).
- Do not invent facts. If information is missing, list it as an assumption.
- Keep the output scannable — use tables, numbered lists, and code fences.
- Cite specific lines / rows / fields when referring to the input.

**Output Format:**
1. Short summary (2–3 sentences).
2. Main deliverable for "WebSocket Implementer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Server setup, typed events, React hook, reconnection, scaling notes.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
WebSockets:
- Library: Socket.IO
- Auth: validate JWT on handshake
- Event naming: kebab-case, domain-prefixed (notification:new)
- Reconnection: exponential backoff, max 5 attempts
```
