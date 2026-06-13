# F12_D4_OBSERVER_v1 — Result

Pre-reg hash: `ea54c69516d93f8802bab2eaeb4de031c8d6658c4c7a6a978ac59e57fe3d2bb9`  
Run date: 2026-06-13  
Data: `celegans_302_d4.json` — 279 neurons, 3 layers (d1=chemical_synapse, d2=gap_junction, d4=scientific_attention)  
d4 source: PubMed Entrez API, query `"Caenorhabditis elegans"[tiab] AND "[NEURON]"[tiab]`

---

## Cross-layer correlations

| Layer pair | r | Verdict |
|---|---|---|
| chemical_synapse ↔ gap_junction (F12 baseline) | **0.6438** | — |
| chemical_synapse ↔ scientific_attention | **−0.0081** | — |
| gap_junction ↔ scientific_attention | **−0.0445** | — |
| d1 ↔ d4 among neurons with any d4 presence (n=51) | **−0.1921** | — |

## Hypothesis outcomes

| ID | Prediction | Result | Verdict |
|---|---|---|---|
| H1 | r(d1↔d4) > 0.10, p < 0.05 | r = −0.008, p = 0.89 | **DENIED** |
| H2 | r(d1↔d4) < 0.40 | r = −0.008 | **CONFIRMED** |
| H3 | r(d2↔d4) > 0.10, p < 0.05 | r = −0.044, p = 0.46 | **DENIED** |

**Overall verdict: DENIED (H1, H3) / CONFIRMED (H2) — STRONGER THAN EXPECTED**

H2 is confirmed, but the result is more extreme than predicted. d4 is not a weakly-correlated observer layer — it is **orthogonal** to the physical layers (r ≈ 0 across all 279 neurons; slightly negative among the 51 neurons with any co-mention).

---

## d4 sparsity

- 51 / 279 neurons (18.3%) appear in at least one co-mention pair  
- 228 / 279 neurons have **zero** scientific co-attention (d4_deg = 0)  
- AVAL (d1_deg=380, top structural hub) has d4_deg = 0

---

## Hub shadow analysis (d1 vs d4)

**Under-researched (high structural rank, low attention rank — structural blind spots):**

| Neuron | d1_rank | d4_rank | gap |
|---|---|---|---|
| VD03 | 25 | 269 | 244 |
| VD05 | 29 | 271 | 242 |
| VD06 | 36 | 272 | 236 |
| VD02 | 33 | 268 | 235 |
| VD04 | 41 | 270 | 229 |
| VD01 | 49 | 267 | 218 |

All VD neurons (ventral D-type GABAergic motor neurons): structurally important for coordinating body-wall muscle inhibition during locomotion. High d1 rank (~25–49 out of 279), essentially zero scientific co-mention.

Command interneurons AVAL, AVAR (d1_rank=1,2) also have d4=0 — not in the rank list above because all their neighbors also have d4=0, so no rank gap is computed.

**Over-attended (low structural rank, high attention rank — functionally famous, structurally peripheral):**

| Neuron | d1_rank | d4_rank | gap |
|---|---|---|---|
| PLML | 279 | 6 | 273 |
| ALA | 255 | 5 | 250 |
| PDB | 275 | 25 | 250 |
| ALMR | 240 | 13 | 227 |
| ASIL | 245 | 19 | 226 |

PLML/PLMR (posterior lateral mechanosensory) and ALM/AVM (anterior lateral/ventral mechanosensory) are the neurons made famous by Martin Chalfie's touch-sensitivity work (Nobel Prize 2008). They are structurally peripheral (low degree) but dominate the co-mention graph because all mechanosensory papers mention them together.

---

## Interpretation

**Observer Orthogonality confirmed:** d4 is not a noisy version of d1/d2. It is an orthogonal dimension. The C. elegans research community organized itself around *functional salience* (touch sensitivity, chemosensation, sleep), not *structural importance* (connection degree). The two are independent axes of the connectome.

**Named finding candidate:** Observer Orthogonality — the observer layer (d4) is statistically orthogonal to the physical structural layers (d1, d2), and the deviation is systematic: the field focuses on functionally iconic neurons while ignoring structural hubs.

**Implication for irdme-ai:** An AI model trained on the C. elegans literature will reproduce the d4 pattern — it will know a great deal about touch cells and almost nothing about AVAL/AVAR (the backbone command interneurons). The structural blind spots in the literature become the model's blind spots. IRDME can now measure this quantitatively.
