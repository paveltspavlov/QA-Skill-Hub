---
name: regex-and-data-transformer
description: "Create or debug a regex or data transformation for a specified format and runtime. Use for parsing, validation, logs, and safe reshaping."
---

# Regex and Data Transformer

## When to Use
Use when the input format and matching/transformation behavior can be specified with examples. Prefer a real parser for nested, recursive, escaped, or grammar-based formats.

## Required Inputs
Runtime and regex flavor, encoding, representative valid/invalid/boundary samples, size limits, capture groups, desired output shape, and whether input is untrusted.

## Procedure
1. Write examples as input → expected match/captures/output before designing the pattern.
2. Build the simplest anchored pattern or parser consistent with the runtime; name captures and explain flags/escaping.
3. Check empty, Unicode, multiline, malformed, large, and adversarial inputs as relevant.
4. Review worst-case performance and catastrophic backtracking risk. Add input bounds or use a non-backtracking parser for untrusted input.
5. Provide executable test vectors in the target runtime; do not claim runtime compatibility without checking the dialect.

## Output Contract
Return: runtime/dialect; exact regex or transformation; explanation of each major group/step; a test table with input, expected match/captures/output, and reason; limitations; and safe usage example. State when a structured parser is preferable.

## Quality Gate
All supplied test vectors match their expected results. Escaping and anchoring are deliberate. Invalid input is rejected safely. No unbounded catastrophic-backtracking pattern is proposed for untrusted, unbounded input.

## Evidence and Uncertainty
Treat supplied samples as the format specification unless contradicted. Ask for examples when edge behavior is unknown; label inferred grammar rules. Do not claim the expression is universally safe or portable across regex engines. Apply the evidence-readiness-gate.
