# IRDME Pre-registrations

Public record of pre-registered scientific hypotheses for the
[IRDME](https://github.com/vladi160/the-beginning) (Item · Relation · Dimension · Multilayer · Engine) research project.

**This repository exists to make failed predictions visible, not only successful ones.**

---

## Quick verification

Clone this repo and run one command:

```bash
git clone https://github.com/vladi160/preregistrations.git
cd preregistrations
python verify.py experiments/I1_p53_domain_science.json
```

Expected output:

```
  Experiment : I1_p53_domain_science
  Registered : 2026-04-17T23:34:43.121109+00:00
  Expected   : 32409dbda299e783
  Computed   : 32409dbda299e783
  MATCH — pre-registration intact.
```

`verify.py` works on **Python 3.6+** with no external dependencies. It finds the `.prediction` sidecar automatically from the `.json` path.

---

## Experiments

### I1 — p53 Gene Regulatory Network

| File | Description |
|---|---|
| [`experiments/I1_p53_domain_science.json`](experiments/I1_p53_domain_science.json) | 5 pre-registered hypotheses |
| [`experiments/I1_p53_domain_science.prediction`](experiments/I1_p53_domain_science.prediction) | Hash + timestamp sidecar |

**Hash:** `32409dbda299e783`  
**Registered:** `2026-04-17T23:34:43.121109+00:00` (before any analysis was run)

#### Verdicts (analysis run 2026-04-18)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | ATM ranks top 3 divergers between physical ↔ genetic layers | **DENIED** | ATM ranked 13/15 (gap=1). True top diverger: CHEK1 (gap=8). |
| h2 | coherence_score > 95th null percentile (n=500 permutations) | **CONFIRMED** | 0 of 500 permutations scored higher — p < 0.002 |
| h3 | TP53 is top hub in ≥ 3 of 4 layers | **CONFIRMED** | TP53 ranked #1 in all 4 layers, divergence=0.000 |
| h4 | r(functional_association, physical_interaction) > r(functional_association, co_expression) | **CONFIRMED** | 0.749 vs 0.679 |
| h5 | TP53 depth ≤ 1 and MDM2 depth ≥ 2 in functional_association layer | **PARTIAL** | TP53 depth=0 ✓ · MDM2 depth=1 ✗ (predicted ≥ 2) |

---

## Why denied hypotheses matter

The DENIED result on h1 is direct evidence of integrity. A tool that always confirms predictions is not producing science — it is producing confirmation bias. The prediction named ATM as the top diverger based on domain knowledge; the tool ranked ATM 13th out of 15 and identified CHEK1 as the true structural outlier (gap=8). That disagreement is the result. Denied hypotheses are not failures. They are the mechanism by which the measurement stays honest.

---

## How the hash works

The hash covers **only the `id` and `statement` fields** of each hypothesis — not the full file. This keeps the hash stable if metadata (rationale text, graph paths, analysis notes) is updated, while locking the falsifiable predictions.

Algorithm (same as `dev.py commit-prediction`):

```python
import hashlib, json

with open('experiments/I1_p53_domain_science.json', encoding='utf-8') as f:
    data = json.load(f)

hypotheses = data.get('hypotheses', [])
statements = [
    {'id': h.get('id', f'h{i}'), 'statement': h.get('statement', '')}
    for i, h in enumerate(hypotheses)
]
canonical = json.dumps(statements, sort_keys=True, ensure_ascii=False)
result = hashlib.sha256(canonical.encode()).hexdigest()[:16]
print(result)  # 32409dbda299e783
```

> **Common mistake:** hashing the raw file bytes (`open(...).read()`) or
> concatenating fields as strings will produce a different hash. Always use
> `json.load()` + `json.dumps(sort_keys=True)` as shown above, or just run
> `python verify.py <file.json>`.

---

## Private repo timeline

The main codebase at `github.com/vladi160/the-beginning` is private. Its git
history is the internal anchor; this public repo is the external one. The two
together prove the pre-registration preceded the analysis.

| Commit (private repo) | Date | Event |
|---|---|---|
| `da5a121` | 2026-04-17 23:34:43 UTC | Pre-registration: `I1_p53_domain_science.json` + `.prediction` created |
| `cfc1bea` | 2026-04-18 | Analysis results: `I1_p53_results.json` committed |
| `5c9697a` | 2026-04-18 | Abstract draft committed |

---

## Pre-registration protocol

All experiments follow this workflow:

1. Write hypotheses in `<experiment>.json` with explicit, falsifiable predictions
2. Run `python dev.py commit-prediction <experiment>.json` in the main repo — creates `<experiment>.prediction` with hash + UTC timestamp
3. Push **both files** to this public repo **before running any analysis**
4. Run the analysis
5. Record verdicts honestly; do not modify the hypotheses file

The `.json` hypotheses file must never be edited after the `.prediction` sidecar is created.

---

## Repository structure

```
experiments/
    <name>.json         hypothesis file (pre-registered predictions)
    <name>.prediction   sidecar (hash + timestamp, auto-generated)
verify.py               standalone verification script (no dependencies)
README.md               this file
```

## Why this repository exists

The main IRDME codebase is private (proprietary implementation details). A private repo timestamp proves nothing to an external reviewer — files could have been written after seeing results. This public repo provides an independently verifiable external timestamp. The rule: pre-registration files are pushed here **before** analysis is run.
