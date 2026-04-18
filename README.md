# IRDME Pre-registrations

Public record of pre-registered scientific hypotheses for the IRDME (Item · Relation · Dimension · Multilayer · Engine) research project.

## What this repository is

Every experiment in the IRDME project pre-registers its hypotheses before analysis using `dev.py commit-prediction`. This creates two files:

- **`.json`** — the hypothesis file with explicit predictions, rationale, and expected outcomes
- **`.prediction`** — a sidecar file containing a SHA-256[:16] hash of the hypothesis file and a UTC timestamp

The `.prediction` sidecar is the scientific integrity anchor. It proves the hypothesis file existed in its current form at the stated time, before any analysis was run.

## Why this repository exists

The main IRDME codebase is private (patent-pending algorithms). A private repo timestamp proves nothing to an external reviewer — the files could have been written after seeing results and backdated. This public repo provides an independently verifiable timestamp record.

**The rule going forward:** pre-registration files are pushed here **before** analysis is run. The GitHub commit timestamp on this repo is the external anchor.

## I1 — p53 Gene Regulatory Network (Phase I1)

| File | Description |
|---|---|
| [`I1_p53_domain_science.json`](experiments/I1_p53_domain_science.json) | 5 pre-registered hypotheses about the p53 4-layer multilayer network |
| [`I1_p53_domain_science.prediction`](experiments/I1_p53_domain_science.prediction) | SHA-256[:16] hash + UTC timestamp sidecar |

**Pre-registration hash:** `32409dbda299e783`  
**Pre-registration timestamp:** `2026-04-17T23:34:43.121109+00:00`

### Private repo verification

The main repo at `github.com/vladi160/the-beginning` (private) has the following verifiable git history:

| Commit | Date | Action |
|---|---|---|
| `32409dbda299e783` (hash in .prediction) | 2026-04-17 23:34:43 UTC | Pre-registration committed — `I1_p53_domain_science.json` + `.prediction` created |
| `da5a121` | 2026-04-18 | Code fixes committed (display language, methodology documentation) |
| `cfc1bea` | 2026-04-18 | Analysis results committed — `I1_p53_results.json` |
| `5c9697a` | 2026-04-18 | Abstract draft committed to `scaffold.md` |

Pre-registration precedes analysis by commit history. The DENIED result on h1 (ATM ranked 13th, not top 3) further demonstrates that the hypotheses were not written after seeing results.

### I1 hypothesis verdicts (summary)

| Hypothesis | Verdict |
|---|---|
| h1: ATM ranks top 3 by divergence (physical ↔ genetic) | **DENIED** — ATM ranked 13/15. CHEK1 was true top diverger (gap=8). |
| h2: coherence_score > 95th null percentile (n=500) | **CONFIRMED** — 0 of 500 permutations scored higher (p < 0.002) |
| h3: TP53 top hub in ≥ 3 of 4 layers | **CONFIRMED** — TP53 #1 in all 4 layers, divergence=0.000 |
| h4: r(FA,PI) > r(FA,co_expression) | **CONFIRMED** — 0.749 vs 0.679 |
| h5: TP53 depth ≤ 1, MDM2 depth ≥ 2 | **PARTIAL** — TP53 depth=0 confirmed; MDM2 depth=1, not ≥ 2 |

## How to verify

```bash
# Compute the hash yourself and compare to the .prediction sidecar
python -c "
import hashlib, json
with open('experiments/I1_p53_domain_science.json') as f:
    content = f.read()
h = hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]
print('Hash:', h)
print('Expected: 32409dbda299e783')
print('Match:', h == '32409dbda299e783')
"
```

## Pre-registration protocol

All future experiments follow this protocol:
1. Write hypotheses in a `.json` file with explicit predictions and rationale
2. Run `dev.py commit-prediction <file.json>` — creates the `.prediction` sidecar with hash + UTC timestamp
3. Push both files to this public repo **immediately, before any analysis**
4. Run the analysis
5. Record verdicts in `<experiment>_results.json` without modifying the hypotheses file

The hypotheses file must never be edited after the `.prediction` sidecar is created.
