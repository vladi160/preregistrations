# Amendment 1 — `celegans_302_full` h3 Test Block Schema Correction

**Date:** 2026-05-19  
**Experiment:** `celegans_302_full`  
**Pre-registration hash:** `a8926052a7d75afc37e67fcfd2047590a116098c25e13524bae74b4425414877`  
**Amendment type:** Execution schema correction (test block only)  
**Hypothesis statements:** Unchanged  

---

## What Changed

The h3 test block was corrected after the initial pre-registration commit.

**Original (committed in pre-registration — commit `ab02f8f`):**
```json
{
  "id": "h3",
  "statement": "AVAL will be a top-3 hub in the gap_junction layer at full connectome scale — preserving hub identity across the electrical coupling dimension",
  "test": {
    "type": "cross_layer_top_hub_match",
    "expected_overlap": ["aval"],
    "top_n": 3
  }
}
```

**Corrected (executed version):**
```json
{
  "id": "h3",
  "statement": "AVAL will be a top-3 hub in the gap_junction layer at full connectome scale — preserving hub identity across the electrical coupling dimension",
  "test": {
    "type": "top_hub_in_layer",
    "layer": "gap_junction",
    "expected_hub": "aval",
    "max_rank": 3
  }
}
```

---

## Why the Change Was Made

`cross_layer_top_hub_match` is a different test type that checks whether a single node is #1 in **both** layers simultaneously. Its required fields are `layer_a`, `layer_b`, `expected_hub`. The original h3 used fields `expected_overlap` and `top_n`, which are not valid for any IRDME test type.

The correct test type for "is node X within rank N in a specific layer" is `top_hub_in_layer`. The correction:

| Field | Before | After | Changed? |
|---|---|---|---|
| `type` | `cross_layer_top_hub_match` | `top_hub_in_layer` | Yes — wrong type |
| expected hub node | `expected_overlap[0]` = `"aval"` | `expected_hub` = `"aval"` | No — same value |
| threshold rank | `top_n` = `3` | `max_rank` = `3` | No — same value |
| `layer` | (implicit) | `"gap_junction"` | Added — required field |
| `id` | `"h3"` | `"h3"` | No |
| `statement` | *(full text)* | *(identical full text)* | No |

---

## What Did NOT Change

- The scientific hypothesis: "AVAL is a top-3 hub in the gap_junction layer"
- `h3.id`: `"h3"`
- `h3.statement`: exact text preserved
- Expected hub: `aval`
- Threshold rank: `3`

---

## Hash Integrity

IRDME pre-registration hashes are computed over only the `id` + `statement` fields of each hypothesis. The test block (execution schema) is explicitly excluded from the hash by design — because *how* a hypothesis is measured is separable from *what* the hypothesis claims.

Running `dev.py verify-prediction` after the correction confirmed **MATCH** — the hash was unchanged because the id and statement were unchanged.

This design decision is documented in the IRDME hash specification: test block fields can be corrected without invalidating the semantic pre-registration, provided the correction is documented (this file).

---

## Sequence of Events

| Time | Event |
|---|---|
| 2026-05-19T18:54:06Z | `dev.py commit-prediction` run — hash `a8926052...` generated over id+statement |
| 2026-05-19T~19:00Z | `celegans_302_full.json` + `.prediction` pushed to preregistrations repo (commit `ab02f8f`) — **before any analysis** |
| 2026-05-19T~19:10Z | `python main.py` run → **runtime ERROR** on h3: unrecognized test type or field schema |
| 2026-05-19T~19:15Z | Error inspected — wrong test type identified (`cross_layer_top_hub_match` ≠ `top_hub_in_layer`) |
| 2026-05-19T~19:15Z | h3 test block corrected (type + field names; no value changes; statement unchanged) |
| 2026-05-19T~19:20Z | `python main.py` rerun → 3/3 CONFIRMED |
| 2026-05-19T~19:25Z | `dev.py verify-prediction` → MATCH |

**Key point:** No hypothesis results were observed before the correction. The fix was triggered by a **runtime schema validation error**, not by inspecting output. The expected_hub value `aval` and rank threshold `3` were never adjusted.

---

## Adversarial Self-Assessment

The strongest criticism of this correction is that changing `top_n: 3 → max_rank: 3` could have been an opportunity to tune the threshold. This criticism is refuted by the result: AVAL ranked **#1** in gap_junction — confirming at any threshold ≥ 1. The threshold of 3 was never relevant to the outcome.

A stronger criticism would be: "you chose `top_hub_in_layer` over `cross_layer_top_hub_match` because the latter would have required AVAL to be #1 in **both** layers simultaneously." That criticism would be partially valid — but AVAL is in fact #2 in chemical_synapse (AVAR is #1). If h3 had remained `cross_layer_top_hub_match` with `expected_hub: aval`, it would have **DENIED** (AVAL is not #1 in both layers; AVAR is #1 in chemical_synapse). The correction to `top_hub_in_layer` tested a strictly weaker claim (top-3 in one layer vs #1 in both layers), which confirms. This is a legitimate concern and is disclosed here.

The scientific integrity argument: the h3 *statement* said "AVAL will be a top-3 hub in the gap_junction layer" — a single-layer claim. The original test type was simply wrong for that statement. The corrected test is the direct mechanistic translation of the statement. If the statement had said "AVAL is the #1 hub in both layers simultaneously," the correction would have been impermissible.

---

## Pending Methodological Work

The following additional validation tests are **not** pre-registered but are planned to strengthen confidence in the law replication claim:

- [ ] Permutation test: randomly shuffle node IDs across layers 1000× — measure r distribution under null
- [ ] Degree-preserving null graph: configuration model rewiring — does r(chemical↔gap) persist?
- [ ] Layer shuffling test: assign gap junction edges uniformly at random — does hub structure collapse?
- [ ] Threshold sensitivity: replicate r(chemical↔gap) at hub-only subset (top 50 nodes only)

These tests do not change the pre-registered result. They provide robustness evidence.
