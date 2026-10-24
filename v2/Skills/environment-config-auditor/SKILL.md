---
name: environment-config-auditor
description: "Use when reviewing environment configuration for completeness and secret safety."
---

## When to Use
Use to audit env files, deployment variable definitions, config loaders, or local setup docs. Review only the requested repository and environment scope; do not expose or rotate secrets without authorization.

## Required Inputs
Require target environment(s), config loader/source files, documented variable names, deployment manifest/secret references, safe access to value presence (not secret values), and desired audit scope. Clarify whether required-vs-optional and example-file policy are defined.

## Procedure
1. Inventory variable names and references in config parsing, env templates, deployment manifests, CI definitions, docs and tests. Read names/metadata only; do not print secret values.
2. Build a matrix: key, consumer, required/optional condition, source per environment, default, validation, sensitivity, and docs. Verify each classification from code or owner input; mark unknown.
3. Detect missing keys, unused/misspelled names, unsafe defaults, committed credential-like literals, sample/live-value confusion, and inconsistent quoting/type parsing. Do not assert a secret is compromised from a pattern match alone.
4. Inspect ignore rules and secret-management references; propose remediation and rotation only when evidence and authorization support it.
5. Run safe config/schema tests or static scans without echoing values; report suppressed-value findings and limitations.

## Output Contract
Return: **Scope**; **Environment-variable matrix** (name, consumer, required condition, source, default, validation, secret classification); **Findings** (severity, path/line, evidence, safe remediation); **Potential exposed-secret handling**; **Checks run and limitations**. Never include actual secret values in report or patch.

## Quality Gate
No credentials or tokens appear in output, logs, or examples. Requiredness, defaults, and environment mappings are sourced rather than guessed; uncertain items are marked for owner confirmation. Fixes preserve deploy behavior and secret-store policy. A possible exposed credential is treated as sensitive: limit disclosure, follow authorized incident process, and never rotate or publish it without approval.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
