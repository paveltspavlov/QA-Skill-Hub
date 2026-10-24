---
name: defect-pattern-analysis
description: "Analyze a defect dataset for clusters, trends, recurring failure modes, and risk areas. Use when multiple defects are available and trend analysis is requested."
---

# Defect Pattern Analysis

## Procedure
1. Inspect fields, time range, duplicates, missing values, taxonomy, and sampling limits before drawing conclusions.
2. Normalize only with documented rules. Separate counts from rates and compare groups only with denominators.
3. Cluster by component, symptom, trigger, release, failure mode, and suspected cause; separate observed categories from inferred causes.
4. Prioritize patterns by severity, exposure, recurrence, and business impact. Do not infer causation from correlation alone.
5. Provide representative evidence, confidence limits, follow-up tests, and investigation questions.

## Output
A pattern report with method, counts/denominators, examples, ranked risks, caveats, and next actions.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
