---
name: commit-message-writer
description: "Use when writing a commit message from a verified staged diff."
---

## When to Use
Use to propose a message for staged changes or a specified commit diff. Do not infer scope from the branch name alone or stage/commit without explicit authorization.

## Required Inputs
Require the exact staged diff or commit range, repository commit convention, ticket/reference format if applicable, and whether body/footer are expected. Inspect staged status and diff; do not include uncommitted unstaged work unless requested.

## Procedure
1. Read repository contribution docs and recent representative commit subjects to identify style; do not impose Conventional Commits unless repo or user requires it.
2. Summarize actual change intent and affected behavior from diff, distinguishing code changes from tests/docs.
3. Choose an imperative or repository-prescribed subject within existing conventions; mention breaking change only if contract impact is evidenced.
4. Add body for rationale/context when subject alone is insufficient; include issue references only when supplied.
5. Check that every phrase is supported by staged changes, message has no secret/personal data, and subject/body are concise and unambiguous.

## Output Contract
Return **Recommended subject**; optional **Body** and **Footer(s)**; **Diff scope used** (staged files or exact range); **Convention basis**; **Uncertainty** if the diff is partial. Example for a verified change: `fix: reject expired invite tokens` — use this syntax only if the repository uses that convention and diff supports it.

## Quality Gate
Message accurately describes the actual patch, not a proposed or unstaged change. No unsupported issue IDs, test claims, breaking labels, or credit. If staged diff is empty/ambiguous or contains unrelated changes, ask or provide alternatives tied to distinct scopes; never create a commit unless asked.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
