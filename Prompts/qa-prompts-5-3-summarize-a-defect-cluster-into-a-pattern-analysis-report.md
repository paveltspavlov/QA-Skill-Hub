---
id: qa-prompts-5-3-summarize-a-defect-cluster-into-a-pattern-analysis-report
name: "5.3 - Summarize a Defect Cluster into a Pattern Analysis Report"
folder: prompts
section: qa-prompts
summary: "Defect Management"
tags:
  - "qa-prompts"
  - "defect management"
---

# Prompt 5.3 - Summarize a Defect Cluster into a Pattern Analysis Report

> Category: **Defect Management**

When to use  At the end of a test cycle or sprint when you have a collection of defects and want to identify systemic patterns, root cause themes, or areas of the system needing architectural attention.

Expected output  A management-ready defect pattern analysis identifying systemic issues, common root causes, and specific recommendations.

Prompt

```
**Role:** You are a QA lead preparing a defect trend analysis report for a sprint 

retrospective and release quality review. You identify systemic patterns, not just 

individual bugs.

**Context:** The system is [SYSTEM DESCRIPTION]. The defects below were found during 

[TEST CYCLE NAME / SPRINT / PERIOD]. The team is looking for patterns to address in 

the next development cycle.

**Instruction:** Analyze the collection of defects below and produce a pattern 

analysis report that identifies:

1. Thematic clusters - groups of defects that share a common root cause area 

   (e.g., "input validation," "session management," "third-party integration failures")

2. High-risk modules - which parts of the system have the most/highest severity defects

3. Defect types - distribution across functional/performance/security/usability/data

4. Root cause themes - underlying causes that appear across multiple defects

5. Recommendations - specific, actionable improvements to prevent similar defects

**Input:**

Defect list:

[PASTE DEFECT TITLES, DESCRIPTIONS, SEVERITY RATINGS HERE - one per line or as a table]

**Constraints:**

- Identify at least 3 and no more than 8 distinct pattern clusters

- Be specific in recommendations - "improve input validation" is not specific enough; 

  "add server-side validation for all numeric fields in the payments module" is

- Include a severity-weighted view (a cluster with one Critical defect may matter 

  more than one with five Low defects)

- Keep the executive summary to 4 sentences maximum

**Output Format:**

# Defect Pattern Analysis - [SPRINT/CYCLE NAME]

**Prepared by:** QA | **Date:** [DATE] | **Defects analyzed:** [COUNT]

## Executive Summary

[4 sentences max]

## Defect Clusters

### Cluster [N]: [Cluster Name]

- **Defects in this cluster:** [List defect IDs/titles]

- **Severity distribution:** [X Critical, X High, X Medium, X Low]

- **Common root cause:** [Description]

- **Recommendation:** [Specific action item]

[Repeat for each cluster]

## High-Risk Modules

| Module | Defect Count | Highest Severity | Risk Assessment |

|---|---|---|---|

## Top 3 Recommendations for Next Sprint

1. [Specific recommendation]

2. [Specific recommendation]

3. [Specific recommendation]
```
