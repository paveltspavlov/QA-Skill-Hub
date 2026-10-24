---
name: documentation-analysis
description: "Analyze, draft, and update technical documentation using repository evidence and traceable sources. Use for READMEs, guides, specifications, release notes, and source-grounded explanations."
---

# Documentation Analysis

## Procedure
1. Inspect the requested document and project context before editing. Identify audience, purpose, scope, canonical terminology, and relevant source files.
2. Check factual accuracy, missing steps, conflicting statements, stale versions, broken relative links, heading structure, and traceability.
3. For external or version-specific claims, prefer official primary sources. Record a direct link and the relevant section; keep claim and source aligned. If a source is inaccessible, state that limitation.
4. Draft or edit only the requested scope. Preserve voice and structure unless the task asks for a redesign. Avoid duplicating instructions that belong in repository context files.
5. Verify links/commands against files or actual execution when possible. Clearly distinguish verified facts, recommendations, and unknowns.

## Output
The revised document or proposed text, a short list of material changes, source links, and unresolved verification items.

## Quality checks
- No fabricated versions, flags, examples, or project behavior.
- Relative links are used for repository files where appropriate.
- Instructions are concise, complete, and testable by the intended reader.

## References
- [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
- [GitHub prompt files](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-files)
