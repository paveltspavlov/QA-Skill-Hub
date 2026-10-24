---
name: defect-pattern-analysis
description: "Analyze a defect dataset for clusters, trends, recurring failure modes, and risk areas. Use when multiple defects are available and trend analysis is requested."
---

# Defect Pattern Analysis

## When to Use
Use when multiple defects are available and the goal is to identify concentration, recurrence, release trends, escape patterns, or test priorities. This is descriptive analysis and hypothesis generation, not causal proof.

## Required Inputs
Request a data file/table with field definitions, time range, project/release/sprint context, inclusion/exclusion rules, severity/status taxonomy, component mapping, root-cause provenance, exposure/usage denominators when available, and the decision the analysis should support. Preserve IDs and sensitive fields; redact unnecessary personal or customer data.

## Procedure
1. Profile row count, fields, date range, missingness, duplicate IDs, invalid categories, and sampling/selection bias. Report exact cleaning rules; retain raw records unchanged.
2. Normalize labels only through a documented mapping. Separate counts from rates; only compare modules/releases when appropriate denominator (users, changes, executions, exposure, or period) exists. If absent, describe raw counts as such.
3. Tabulate clusters by component × symptom/failure mode × severity/status; inspect trend by period and discovery stage (test/production) when data supports it. Show numerator and denominator for each rate.
4. Select representative records by ID and evidence. Treat recorded root cause as an attribute of the dataset, not verified causation. Label inferred causes as hypotheses and identify evidence needed to confirm.
5. Prioritize follow-up by impact, exposure, recurrence, and confidence in the observation. Recommend concrete regression/exploratory work tied to patterns. Avoid arbitrary “top 3” if ties or coverage make ranking misleading.
6. Reconcile all reported totals to cleaned data and list exclusions. Do not infer statistical significance unless an appropriate method and sample basis are provided.

## Output Contract
Return `Dataset and method`; summary table `Metric | Count/rate | Numerator/denominator | Period | Caveat`; pattern table `Rank | Component | Pattern | Evidence IDs | Count/rate | Impact | Hypothesis status | Follow-up`; `Limitations`; and `Next-cycle test focus`. Example: `1 | payments | timeout reports cluster in release R | D-14,D-19 | 2/40 payment changes (if denominator supplied) | payment completion | hypothesis: dependency latency; not established | inspect timeout telemetry and add controlled timeout regression`.

## Quality Gate
Dataset scope and exclusions are explicit; all totals reconcile; rate denominators are valid; duplicates and missingness handled transparently; examples trace back to source IDs; hypotheses never presented as root cause; recommendations follow evidence.

## Evidence and Uncertainty
Use the supplied dataset, documented transforms, and actual calculations; show source rows/IDs and method. Apply evidence readiness via four supported checks—clear scope, traceable claims, complete deliverable, relevant verification—25 points each. Below 75/100, ask, qualify, or abstain; no guessed confidence percentages. Critical privacy, authorization, safety, or acceptance failures block readiness regardless of score.
