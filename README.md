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

### M_EXT — Flask External Validation

| File | Description |
|---|---|
| [`experiments/ext_flask_law.json`](experiments/ext_flask_law.json) | 4 pre-registered hypotheses |
| [`experiments/ext_flask_law.prediction`](experiments/ext_flask_law.prediction) | Hash + timestamp sidecar |

**Hash:** `3879413e12193fd66fc8df8746783dbff47419bfbe73568c02e0eaf5d070870c`
**Registered:** `2026-04-22T15:18:24.029791+00:00` (before any analysis was run)

#### Verdicts (analysis run 2026-04-22)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(imports↔structural_coupling) > r(imports↔co_change) | **CONFIRMED** | 0.6659 > 0.4942 |
| h2 | r(imports↔structural_coupling) ≥ 0.50 | **CONFIRMED** | r=0.6659 (p=0.015) |
| h3 | r(imports↔co_change) < r(imports↔structural_coupling) | **CONFIRMED** | 0.4942 < 0.6659 |
| h4 | app is top hub in imports layer | **CONFIRMED** | app = #1 by degree in imports layer |

---

### M_EXT2 — C. elegans Connectome (True External Validation)

| File | Description |
|---|---|
| [`experiments/celegans_connectome.json`](experiments/celegans_connectome.json) | 2 pre-registered hypotheses |
| [`experiments/celegans_connectome.prediction`](experiments/celegans_connectome.prediction) | Hash + timestamp sidecar |

**Hash:** `5cbf9e5d1edd6c38649dbe62765a760a95a788f67be55365b319e02dc88a489b`
**Registered:** `2026-04-22T23:28:50.565335+00:00` (before any analysis was run)

> **Note on commit history:** Two commits exist for this file — [`d69a159`](https://github.com/vladi160/preregistrations/commit/d69a159) (2026-04-22T18:57:29 UTC) and [`fff8a0b`](https://github.com/vladi160/preregistrations/commit/fff8a0b) (2026-04-22T23:28:50 UTC). The sidecar was regenerated between commits; the `prediction_hash` and all hypothesis content are **identical** in both. Only the auto-generated `committed_at` field differs. The pre-registration was intact before any analysis was run.

#### Verdicts (analysis run 2026-04-22)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(chemical_synapse↔gap_junction) > 0 — both layers encode direct physical neuron coupling | **CONFIRMED** | r=0.7774 (Spearman=0.7796, p=0.004) |
| h2 | AVAL or AVAR is top hub in chemical_synapse layer | **CONFIRMED** | AVAL = #1, AVAR = #2 — consistent with White 1986 / Varshney 2011 |

Both data AND layer definitions are fully independent of IRDME. The chemical/electrical distinction was defined by White et al. (1986) from electron micrograph reconstruction.

---

### M_OSS1 — WordPress wp-includes Hub Shadow

| File | Description |
|---|---|
| [`experiments/wordpress_oss1.json`](experiments/wordpress_oss1.json) | 5 pre-registered hypotheses |
| [`experiments/wordpress_oss1.prediction`](experiments/wordpress_oss1.prediction) | Hash + timestamp sidecar |

**Hash:** `6b22eafc586ef5c27416726e36df7ccc996c0117b14018b391ce9b93c0471b5c`
**Registered:** `2026-04-23T00:51:38.608825+00:00` (before any analysis was run)

#### Verdicts (analysis run 2026-04-23)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(function_coupling↔co_change) > r(include_graph↔co_change) | **CONFIRMED** | 0.5156 > 0.2405 |
| h2 | r(function_coupling↔co_change) > 0, p < 0.05 | **CONFIRMED** | r=0.5156, p=0.012 |
| h3 | post.php: co_change rank ≤ 5 AND include_graph rank ≥ 15 (hub shadow) | **CONFIRMED** | co_change #4, include_graph #19 — hidden maintenance risk invisible to static analysis |
| h4 | functions.php: universal hub, rank #1 or #2 in both co_change and function_coupling | **CONFIRMED** | #1 co_change, #2 function_coupling |
| h5 | cohesion score > 90th null percentile (500 permutations) | **DENIED** | 32nd percentile — power-law degree distribution makes high coherence trivial; gradient+p is the correct metric |

---

### M_OSS2 — Next.js Multilayer (App-Router Transition)

| File | Description |
|---|---|
| [`experiments/nextjs_oss2.json`](experiments/nextjs_oss2.json) | 5 pre-registered hypotheses |
| [`experiments/nextjs_oss2.prediction`](experiments/nextjs_oss2.prediction) | Hash + timestamp sidecar |

**Hash:** `cb0cf4a489dc8a279d611e1d2c35faeee9195dd7dfbdd6756756f6641ccf5150`
**Registered:** `2026-04-23T23:48:48.862515+00:00` (before any analysis was run)

#### Verdicts (analysis run 2026-04-24)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(import_graph↔test_coupling) > r(import_graph↔co_change) | **CONFIRMED** | 0.8995 > 0.5484 — strongest OSS gradient to date (Δr=0.35) |
| h2 | r(import_graph↔test_coupling) > 0, p < 0.05 | **CONFIRMED** | r=0.8995, Spearman=0.7027, p=0.002 |
| h3 | server_app_render in co_change top 5 (hub shadow prediction) | **DENIED** | rank #15 — App Router built cleanly; no hub shadow despite 2-year transition |
| h4 | lib in import_graph top 2 | **DENIED** | rank #3 — server_base (#1) and build (#2) dominate monorepo server infrastructure |
| h5 | cohesion score > 70th null percentile | **DENIED** | 31st percentile — confirms M_OSS1 calibration finding; coherence alone insufficient for software graphs |

Key finding: the three DENIED hypotheses are all informative — server_app_render being a relay node (not a hub shadow) is direct evidence that the Next.js team maintained clean architectural boundaries during the App Router transition.

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
| — | 2026-04-22 15:18 UTC | Pre-registration: `ext_flask_law` (M_EXT — Flask) pushed to public repo |
| — | 2026-04-22 | Analysis run: Flask confirmed, r=0.6659 (p=0.015) |
| — | 2026-04-22 23:28 UTC | Pre-registration: `celegans_connectome` (M_EXT2 — C. elegans) pushed to public repo |
| — | 2026-04-22 | Analysis run: C. elegans confirmed, r=0.7774 (p=0.004) |
| — | 2026-04-23 00:51 UTC | Pre-registration: `wordpress_oss1` (M_OSS1 — WordPress) pushed to public repo |
| — | 2026-04-23 | Analysis run: WordPress 4/5 confirmed, post.php = hub shadow |
| — | 2026-04-23 23:48 UTC | Pre-registration: `nextjs_oss2` (M_OSS2 — Next.js) pushed to public repo |
| — | 2026-04-24 | Analysis run: Next.js 2/5 confirmed (law gradient strongest to date), 3 informative denials |

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
