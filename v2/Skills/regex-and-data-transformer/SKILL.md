---
name: regex-and-data-transformer
description: "Create, explain, or debug regular expressions and data transformations for a specified format. Use for parsing, validation, log processing, and safe reshaping."
---

# Regex and Data Transformer

## Procedure
1. Identify the exact input format, runtime/regex flavor, encoding, size, and matching requirements.
2. Ask for representative valid, invalid, and boundary samples when absent.
3. Prefer a structured parser over a complex regex when nested or escaped syntax is involved.
4. Provide tests for matches, non-matches, empty input, Unicode, and adversarial length where relevant.
5. Explain performance risks such as catastrophic backtracking; do not apply transformations to untrusted data without limits.

## Output
The expression or transformation, runtime-compatible examples, test vectors, and limitations.
