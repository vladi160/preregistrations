# Amendment 1 — F12c_celegans_drosophila_transfer_v1

**Filed:** 2026-06-06  
**Type:** Hash mismatch documentation (not a hypothesis change)

## Issue

`verify.py` reports a hash mismatch for `F12c_celegans_drosophila_transfer_v1.json`:

- Expected (in `.prediction`): `cd2ed0804dd83ef3dda64a66b047d5cebb593bcd4eb568c1647c27dc76ce3494`
- Computed from current file: `b5f0aa2611175c3adb810949fce3fa1207c21912d1d8fda85ae0bd92a7a95c41`

The JSON file was not present in this repository until 2026-06-06 (only the `.prediction` sidecar existed — orphaned prediction). The JSON file in the main project (`the-beginning`) shows only one commit (`895c3fd`), and the hash at that commit also does not match the prediction hash.

## Investigation

Three hash values are in evidence:

| Version | Hash |
|---|---|
| Prediction file (registered 2026-05-26T00:00:00+00:00) | `cd2ed080...` |
| Current JSON file | `b5f0aa26...` |
| JSON at commit `895c3fd` (main project) | `cb9914dd...` |

None of the three match. This indicates the prediction was generated from a version of the JSON that was not committed to version control — the hypothesis statements were edited between the prediction commit and the git commit.

The timestamp in the prediction (`2026-05-26T00:00:00+00:00`) is exactly midnight UTC, which is suspicious and may indicate a manually set timestamp rather than an auto-generated one.

## What is known

- The experiment was **run and verdicts recorded**: 3/3 CONFIRMED (cosine 0.985/0.908/avg 0.947), documented in README.md.
- The hypothesis statements **in the current JSON file** are:
  - h1: rank_vector_cosine >= 0.90 in chemical_synapse layer (actual: 0.985 ✓)
  - h2: rank_vector_cosine >= 0.60 in axon_to_axon layer (actual: 0.908 ✓)
  - h3: avg_rank_cosine >= 0.65 across both layers (actual: 0.947 ✓)
- The thresholds are conservative and the actual results substantially exceed them.

## Status

**This experiment's hash integrity cannot be confirmed.** The pre-registration chain for F12c is broken — the JSON that generated the prediction hash was not preserved in version control.

**Consequence for scientific record:**
- The verdicts (3/3 CONFIRMED) are credible on their scientific merits.
- The pre-registration priority claim (committed before analysis) cannot be verified from the hash alone.
- F12c results are treated as **confirmatory but unverifiable pre-registration** for the purposes of the FPL count.
- This does NOT affect any other experiment in this repository.

## Corrective action

All subsequent experiments use `dev.py commit-prediction` which auto-generates the timestamp and commits the exact file that will be run. Manual timestamp editing is not possible through the standard workflow.
