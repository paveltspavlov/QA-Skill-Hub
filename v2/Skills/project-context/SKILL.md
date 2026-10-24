---
name: project-context
description: "Inspect project structure and maintain concise, evidence-based project context. Use before repository work or when a project’s context files need updating."
---

# Project Context

Use when work depends on understanding a repository or when its reusable project context should be created or refreshed.

## Procedure
1. Inspect the repository root, README, manifests/configuration, test commands, and relevant source folders. Search for existing guidance in `AGENTS.md`, `CLAUDE.md`, `.copilot/`, `.vscode/`, and `.github/copilot-instructions.md`.
2. Identify the canonical context location from existing files and repository conventions. Update a context file already used by the project. If `.copilot/` has project guidance, prefer its context file; otherwise use `.vscode/` when a VS Code workspace is established. If both folders exist with relevant context, update the canonical existing file and avoid duplicates; if their instructions conflict, ask which source is authoritative. If neither folder has context, use `.vscode/project-context.md` only when the project clearly uses a VS Code workspace; otherwise create `.copilot/project-context.md`.
3. Update the existing file in place when possible. Preserve unrelated settings and user-authored instructions. Do not overwrite IDE settings, secrets, or generated files.
4. Keep the context short and verifiable: project purpose; language/framework and versions; important folders; setup/test/build commands; style and architecture conventions; data/security constraints; known unknowns.
5. Cite evidence paths (for example, `pyproject.toml`, `package.json`, a workflow file) for technical claims. Mark uncertain details instead of guessing.
6. Do not copy credentials, personal data, or large source files into context.

## Output
Report the context file inspected or changed, the evidence used, unresolved facts, and any files not modified.

## Portability note
`.vscode/` and `.copilot/` are the requested portable project-context locations, but hosts differ in which files they automatically load. Do not claim automatic loading. If the user requests GitHub Copilot auto-loading, explain the separate `.github/copilot-instructions.md` adapter and create it only when asked.

## References
- [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
- [GitHub custom-instructions support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support)
