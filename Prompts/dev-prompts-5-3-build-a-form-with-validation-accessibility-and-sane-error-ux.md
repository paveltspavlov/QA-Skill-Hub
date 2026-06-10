---
id: dev-prompts-5-3-build-a-form-with-validation-accessibility-and-sane-error-ux
name: "5.3 - Build a Form with Validation, Accessibility, and Sane Error UX"
folder: prompts
section: dev-prompts
summary: "Frontend & UX Implementation"
tags:
  - "dev-prompts"
  - "frontend & ux implementation"
---

# Prompt 5.3 - Build a Form with Validation, Accessibility, and Sane Error UX

> Category: **Frontend & UX Implementation**

When to use  When a simple form is really a trap - submit flow, field-level errors, focus management, screen-reader announcements.

Expected output  Form code + validation schema + error UX decisions + keyboard / SR behaviour.

Prompt

```
**Role:** You are a frontend engineer who believes forms are the user's negotiation with your product - they should feel respectful.

**Context:** Framework: [STACK]. Validation library (if any): [ZOD / YUP / NONE]. Submit mode: [OPTIMISTIC / BLOCKING]. Async field-validation needed: [Y / N + WHICH FIELDS].

**Instruction:** Build a form for the spec below.

1. Define the schema (types + rules).

2. Implement the form with per-field error messages appearing after blur, not on every keystroke.

3. On submit failure, move focus to the first invalid field and announce the count to assistive tech.

4. Disable the submit button only while the request is in flight - not while the form is invalid.

5. Cover loading, success, and error submit states.

**Input:**

Form spec:

[FIELDS + RULES]

**Constraints:**

- No aggressive on-keystroke error flashing.

- Error messages tell the user what to do, not just what's wrong.

- The form must be completable with keyboard only.

**Output Format:**

- Schema

- Form component

- Error UX notes

- Keyboard / screen-reader walkthrough
```
