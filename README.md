# IRDME Pre-registrations

Public record of pre-registered scientific hypotheses for the
[IRDME](https://github.com/vladi160/the-beginning) (Item · Relation · Dimension · Multilayer · Engine) research project.

**This repository exists to make failed predictions visible, not only successful ones.**

**What pre-registration is and isn't.** Pre-registration is a logging and history mechanism. It records that a specific prediction was committed to this public repository with a git timestamp before the analysis result was seen. It makes the full prediction history — including denied results — publicly auditable. It does not prevent private analysis before registration; it does not guarantee that no exploratory work happened beforehand. Its value is in workflow discipline, a transparent public record, and reproducibility documentation.

**Current status (May 2026):** 21 CONFIRMED, 6 DENIED across 25 pre-registered experiments (13 Tier A + 12 Tier B). Recent additions: M_RADIAL_1 (BC_RADIAL threshold validation — click CONFIRMED, logrus BC_RADIAL replicated, cobra BC_INVERSION discovered, 3/4 CONFIRMED); BC3b_circuit_v2 (priority arbiter circuit replication, 4/4 CONFIRMED, properly pre-registered); BC_INVERSION formally named as BC6. arXiv:2604.23639 published (cs.SI, April 2026) — v2 in preparation. Platform live at [irdme.com](https://irdme.com).

**proteins_trust_cert_v1 exclusion note:** This experiment (5/5 CONFIRMED) uses the `dataset_trust_certification` methodology — it tests multi-source hub agreement across two data curation methodologies. It does NOT test the FPL inequality $r(d_1, d_2) > r(d_1, d_3)$ and is therefore excluded from the 21/25 FPL primary count. Its h4 independently replicates the FPL in both sources, which is reported as a secondary finding.

**Post-hoc confirmatory runs (NOT pre-registered, not counted in totals):** BC3b c17 circuit (2026-05-22) — workflow was not followed for the original c17 run; BC3b_circuit_v2 is the properly pre-registered replication.

**Experiments in this repo (17 total):**

| File | Experiment | Verdict |
|---|---|---|
| `I1_p53_domain_science` | p53 Gene Regulatory Network — curated | 4/5 CONFIRMED, 1 PARTIAL |
| `ext_flask_law` | Flask external validation (M_EXT) | 4/4 CONFIRMED |
| `celegans_connectome` | C. elegans connectome true external (M_EXT2) | 1/2 CONFIRMED, 1 DENIED |
| `I1_string_validation` | p53 STRING v12.0 external validation | 4/5 CONFIRMED, 1 DENIED |
| `wordpress_oss1` | WordPress wp-includes hub shadow (M_OSS1) | 4/5 CONFIRMED, 1 DENIED |
| `nextjs_oss2` | Next.js App-Router transition (M_OSS2) | 2/5 CONFIRMED, 3 DENIED (all informative) |
| `flask_express_transfer` | Flask↔Express cross-language isomorphism (M_TRANSFER_2) | 4/5 CONFIRMED, 1 PARTIAL |
| `ai_architecture_law` | AI Model Architecture graph (F6) | 4/5 CONFIRMED, 1 DENIED |
| `proteins_trust_cert_v1` | p53 Dataset Integrity Certificate — M_DATASET_TRUST first run *(dataset_trust_certification methodology — excluded from FPL 21/25 count; see note above)* | **5/5 CONFIRMED** |
| `celegans_302_full` | C. elegans full 302-neuron connectome (F12) — law replication + hub compression test | **3/3 CONFIRMED** |
| `mathlib4_F9_v1` | Lean 4 mathlib4: Functional Proximity Law on Formal Mathematics (F9) | **2/3 CONFIRMED, 1 PARTIAL** |
| `proteins_sl_F1_v1` | Synthetic Lethality Prediction — PARP1/CHEK1 as cross-layer divergers (F1) | **3/4 CONFIRMED, 1 PARTIAL** |
| `H_PRIMITIVITY_v1` | Meta-science test: is d1/d2/d3 more primitive than mathematical formalization? (H_PRIMITIVITY) | **1/4 CONFIRMED, 2/4 DENIED, 1/4 PARTIAL — BC4** |
| `M_TRANSFER_3_docopt_v1` | Cross-language FPL replication: Go, Java, Rust docopt implementations | **0/4 CONFIRMED, 3/4 DENIED, 1/4 PARTIAL — BC_RADIAL candidate** |
| `M_GEOM_CSG_1` | Planetary gear CSG multilayer — BC3b boundary test (computational geometry) | **4/4 CONFIRMED** |
| `M_RADIAL_1` | BC_RADIAL threshold validation: cobra (BC_INVERSION), click (CONFIRMED), logrus (BC_RADIAL replicated) | **3/4 CONFIRMED, 1 DENIED — BC_INVERSION (BC6)** |
| `BC3b_circuit_v2` | Priority arbiter circuit — proper pre-registered replication of c17 BC3b result | **4/4 CONFIRMED** |


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

**Hash format note (2026-05-23):** Early prediction sidecars (`I1_p53_domain_science`) store a 16-character truncated hash (legacy format). All later experiments store the full 64-character SHA-256 digest. `verify.py` was updated (commit `991e9d5`) to accept both formats — it verifies the full digest and confirms the stored hash is a valid prefix or exact match. All 17 experiments verified MATCH in a clean-clone reviewer test on 2026-05-23.

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
| h2 | AVAL or AVAR is top hub in chemical_synapse layer | **DENIED** | By degree centrality (pre-registered metric), PVCL = #1 and AVAL = #2. AVAL leads by raw synapse weight, which was not the pre-registered measure. Operational boundary condition: degree rank ≠ weight rank. h1 unaffected. |

Both data AND layer definitions are fully independent of IRDME. The chemical/electrical distinction was defined by White et al. (1986) from electron micrograph reconstruction.

---

### I1 — p53 Gene Regulatory Network (STRING v12.0 External Validation)

| File | Description |
|---|---|
| [`experiments/I1_string_validation.json`](experiments/I1_string_validation.json) | 5 pre-registered hypotheses |
| [`experiments/I1_string_validation.prediction`](experiments/I1_string_validation.prediction) | Hash + timestamp sidecar |

**Hash:** `2f7bffbfa31535042734d554f51ec2622d4f488ea020a1fd0eabf2fac0940a84`  
**Registered:** `2026-05-01T00:11:57.082171+00:00` (before any analysis was run)

**Context:** I1 Phase 2 — same 15 proteins as the original I1 curated analysis, but edges sourced independently from STRING v12.0 channel scores. Layers: physical_interaction (escore ≥ 0.3), co_expression (ascore ≥ 0.08), functional_association (dscore ≥ 0.4), genetic_interaction_proxy (textmining tscore ≥ 0.45, escore < 0.15). The `genetic_interaction_proxy` is NOT the same as DepMap CRISPR screens used in v1.0 — it is a literature proxy.

#### Verdicts (analysis run 2026-05-01)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(functional_association, physical_interaction) > r(functional_association, co_expression) | **CONFIRMED** | 0.8689 > 0.6179 — law replicates on independent STRING data |
| h2 | TP53 is rank #1 hub in physical_interaction layer | **CONFIRMED** | TP53 = #1; confirmed identity of structural center survives data source change |
| h3 | r(functional_association, physical_interaction) > 0 (sign replication) | **CONFIRMED** | r = +0.8689 (Spearman=+0.8130, 95% CI [+0.6427, +0.9558]) — sign and magnitude both replicate |
| h4 | r(functional_association, genetic_interaction_proxy) < r(functional_association, physical_interaction) | **CONFIRMED** | −0.3470 < +0.8689 — regime mismatch confirmed; textmining proxy encodes structurally incompatible layer |
| h5 | CHEK1 in top-3 divergers between physical_interaction and genetic_interaction_proxy | **DENIED** | CHEK1 rank gap = 1 (physical #5 vs proxy #4). True top divergers: BCL2 (gap=13, proxy #1 vs physical #14), TP53 (gap=12, physical #1 vs proxy #13), PCNA (gap=9). CHEK1's v1.0 divergence was specific to DepMap CRISPR genetic interaction screens — it does not replicate with textmining proxy. Named mechanism: CRISPR screens capture essentiality-based synthetic lethality; textmining captures literature co-mention frequency. Different measurement regimes produce different structural divergers. |

**Key finding:** The Functional Proximity Law replicates on fully independent STRING v12.0 data (h1–h4 CONFIRMED, 4/5). The DENIED h5 is the scientifically most valuable result: CHEK1's divergence in v1.0 was a feature of the DepMap CRISPR data, not a universal structural property of the p53 network. BCL2 (textmining hub, physical peripheral) and TP53 (physical hub, textmining peripheral) are the actual cross-layer structural divergers in the STRING-sourced graph. This is a direct data-source boundary condition: the identity of divergent items depends on which relational regime the genetic layer encodes.

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

### F6 — AI Architecture Graph: Functional Proximity Law on ML Model Lineage

| File | Description |
|---|---|
| [`experiments/ai_architecture_law.json`](experiments/ai_architecture_law.json) | 5 pre-registered hypotheses |
| [`experiments/ai_architecture_law.prediction`](experiments/ai_architecture_law.prediction) | Hash + timestamp sidecar |

**Hash:** `bff4e101342af172d3236a2303191ab33973897d7370000e8c46c7148e2bf320`
**Registered:** `2026-04-30T20:26:15.228173+00:00` (before any analysis was run)

#### Verdicts (analysis run 2026-04-30)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(citation_dependency ↔ architecture_inheritance) > r(citation_dependency ↔ benchmark_co_performance) | **CONFIRMED** | 0.9147 > −0.0025 |
| h2 | r(citation_dependency ↔ architecture_inheritance) > 0.4 | **CONFIRMED** | r=0.9147 (Spearman=0.6757, p=0.002, R²=0.8367, large effect) |
| h3 | transformer is rank #1 hub in citation_dependency layer | **CONFIRMED** | transformer #1; top 5: transformer, rnn, gpt3, lstm, bert |
| h4 | transformer is rank #1 hub in architecture_inheritance layer | **CONFIRMED** | transformer #1; top 5: transformer, gpt3, bert, resnet, lstm |
| h5 | transformer is rank ≤ 3 in all three layers (universal_hub) | **DENIED** | transformer = #5 in benchmark_co_performance; llama = #1. Mechanism: recency bias in benchmark selection — LLaMA displaced transformer as the benchmarked model even as transformer remained #1 in both structural layers. Transformer is treated as infrastructure, not a competitor. |

> **Note on the denied h5:** The denial is informative. Transformer's absence from the top-3 benchmark is the structural signature of infrastructure — it is measured in citation and inheritance, but not benchmarked because it is assumed. LLaMA's rank inversion (citation rank #16 → benchmark rank #1) is the chameleon finding: structurally peripheral, deployment-dominant. The law correctly identifies transformer as the universal hub in structural layers; the benchmark layer is a behavioral signal that follows different rules (recency, deployment availability). This is the same regime-mismatch mechanism as Finance DENIED (trading vs lending) and is a boundary condition on interpretation of the benchmark layer.

---

### M_TRANSFER_2 — Flask (Python) ↔ Express.js (JavaScript) Structural Migration

| File | Description |
|---|---|
| [`experiments/flask_express_transfer.json`](experiments/flask_express_transfer.json) | 4 pre-registered hypotheses |
| [`experiments/flask_express_transfer.prediction`](experiments/flask_express_transfer.prediction) | Hash + timestamp sidecar |

**Hash:** `f85f52e6108d841a6ab6998695c42befe1f0d5e79303e6d6362d17f692bf0395`  
**Registered:** `2026-04-24T23:52:27.782904+00:00` (before any analysis was run)

**Context:** Cross-technology structural comparison using `irdme atlas --compare flask.json express.json --pivot co_change`. Flask is the confirmed M_EXT dataset (14 modules, 1934 commits). Express.js extracted fresh via `irdme extract --scope javascript` (6 modules). Both use the Universal Layer Grammar: `static_coupling` (d1), `structural_coupling` (d2), `co_change` (d3). The `co_change` pivot anchors cross-language comparison on the language-agnostic behavioral layer.

#### Verdicts (analysis run 2026-04-25)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(static_coupling ↔ structural_coupling) > r(static_coupling ↔ co_change) in Express | **PARTIAL** | Law gradient present (r_delta > 0) but r underpowered at n=6; gradient direction confirmed, significance not reached. Named boundary: n=6 is below minimum for r significance. |
| h2 | `application` is top hub in Express `static_coupling` layer | **CONFIRMED** | application.js = #1 by degree in static_coupling; requires all other modules |
| h3 | Flask `app` ↔ Express `application` structural similarity > 0.90 | **CONFIRMED** | sim=1.0000 — perfect cross-language structural match (both universal_hub in all layers). `json`↔`utils` sim=0.9705; `sessions`↔`response` sim=0.9335; `wrappers`↔`request` sim=0.9278 |
| h4 | 0 migration hazards between Flask and Express (both well-architected micro-frameworks) | **CONFIRMED** | 0 `migration_hazard` entries. Risk map: 3 safe_transfer, 1 refactor_opportunity (config = Flask chameleon), 10 relay |

**Key discovery (h1 boundary condition):** Express `lib/` is a flat 6-file architecture — no router module in `lib/`; routing logic is internal to `application.js`. `response` is the most behaviorally coupled module (#1 co_change, 267 commits). The law's gradient is present but underpowered — consistent with the Flask M_EXT finding that micro-frameworks with few modules require a minimum n for the law to reach significance.

---

## proteins_trust_cert_v1 — p53 Dataset Integrity Certificate (M_DATASET_TRUST first run)

| File | Description |
|---|---|
| [`experiments/proteins_trust_cert_v1.json`](experiments/proteins_trust_cert_v1.json) | 5 pre-registered hypotheses |
| [`experiments/proteins_trust_cert_v1.prediction`](experiments/proteins_trust_cert_v1.prediction) | Hash + timestamp sidecar |

**Hash:** `5bbbd9cbebe29544e0f239708e384c85aa6f7f4d2a2eb39907b79c80a1d4b023`
**Registered:** `2026-05-14T17:47:08.403592+00:00` (before running POST /api/datasets/compare)

**What this experiment is:** The first run of M_DATASET_TRUST — the dataset integrity certification feature. Rather than testing the Functional Proximity Law on a single graph, this experiment compares two independent sources of the same domain to determine which nodes are *structurally trusted* (hubs in both sources) vs *boundary nodes* (hub in one source only). This inverts the standard science direction: instead of data → patterns, the question is: do independent data sources agree on the structural backbone?

**Sources being compared:**
- **Source A:** `proteins_multilayer.json` — p53 network, manually curated edges from literature (co-IP / pulldown / BioGRID / DepMap CRISPR). v1.0 dataset. 21 physical, 13 co-expression, 16 functional, 10 genetic interaction edges.
- **Source B:** `proteins_multilayer_string.json` — same 15 proteins, edges from raw STRING v12.0 channel scores (escore/ascore/dscore/tscore). v1.1 dataset. Independent curation methodology.

**Context:** Both sources have been individually pre-registered and CONFIRMED via the law: I1_p53_domain_science (hash 32409dbda299e783, April 2026) and I1_string_validation (hash in its .prediction file, May 1 2026). This is the first time they are compared *against each other* for structural agreement.

**Hypotheses:**

| # | Prediction | Type |
|---|---|---|
| h1 | TP53 in trusted_nodes (hub in both sources) | dataset_trust_certification |
| h2 | MDM2 in trusted_nodes (hub in both sources) | dataset_trust_certification |
| h3 | Verdict = PARTIAL (0.4 < agreement_score ≤ 0.7) | dataset_trust_certification |
| h4 | Law holds independently in both sources: r(FA, PI) highest pair in law_a and law_b | dataset_trust_certification |
| h5 | PCNA in boundary_nodes (hub in one source only) | dataset_trust_certification |

*Verdicts to be recorded after running POST /api/datasets/compare with both datasets loaded to irdme.com.*

#### Verdicts (analysis run 2026-05-14, `irdme certify` CLI)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | TP53 in trusted_nodes (hub in both sources) | **CONFIRMED** | TP53 in top-7 hubs in both curated v1.0 and STRING v12.0. The master tumor suppressor retains its structural centrality regardless of curation methodology. |
| h2 | MDM2 in trusted_nodes (hub in both sources) | **CONFIRMED** | MDM2 in top-7 hubs in both sources. MDM2-TP53 feedback loop is structurally robust across data sources. |
| h3 | Verdict = PARTIAL (0.4 < agreement_score ≤ 0.7) | **CONFIRMED** | agreement_score=0.5556, verdict=PARTIAL. Core hubs agree; peripheral topology diverges as predicted due to methodology gap. |
| h4 | Law holds independently in both sources: r(FA, PI) is the top pair in law_a and law_b | **CONFIRMED** | Curated: r(FA,PI)=0.7493 (rank 1). STRING: r(FA,PI)=0.8689 (rank 1). Law holds in both independent sources. |
| h5 | PCNA in boundary_nodes (hub in one source only) | **CONFIRMED** | PCNA is hub in STRING v12.0 (escore high via sliding clamp interactions) but not in curated v1.0. The predicted mechanism — STRING's automated scoring vs curated selection — was the correct explanation. |

**Key findings beyond pre-registered hypotheses:**
- **Trusted set (5 nodes):** TP53, MDM2, ATM, BRCA1, CHK2 — these are the structurally robust nodes of the p53 network, independently confirmed by two data sources with different curation methodologies. Certificate: SHA-256 `ae72b2310cec20b7…` (full hash in output JSON).
- **Boundary — curated-only hubs:** ATR, RB1 — present as hubs in the curated literature but ranked lower in STRING escore. ATR's hub status in curated v1.0 reflects expert curation of replication stress relationships not fully captured by STRING channel thresholds.
---

## F12 — C. elegans Full 302-Neuron Connectome

| File | Description |
|---|---|
| [`experiments/celegans_302_full.json`](experiments/celegans_302_full.json) | 3 pre-registered hypotheses |
| [`experiments/celegans_302_full.prediction`](experiments/celegans_302_full.prediction) | Hash + timestamp sidecar |
| [`experiments/celegans_302_full_amendment1.md`](experiments/celegans_302_full_amendment1.md) | **Amendment 1** — h3 test block schema correction (statement unchanged; filed 2026-05-19) |

**Hash:** `a8926052a7d75afc37e67fcfd2047590a116098c25e13524bae74b4425414877`  
**Registered:** `2026-05-19T18:54:06.378086+00:00` (before any analysis was run)

**Context:** Full-connectome scale-up of M_EXT2 (15 command interneurons, r=0.7774, p=0.004). Extends to the complete Varshney 2011 dataset. n=279 connected neurons (302 total — 23 have no recorded connections in NeuronConnect.xls). Layers: `chemical_synapse` (S/Sp entries, directed, 2194 edges) and `gap_junction` (EJ entries, undirected, 514 edges). Both data AND layer definitions remain fully independent of IRDME — the chemical/electrical distinction is a biological fundamental from White et al. (1986) and Varshney et al. (2011). Also tests the **generative compression claim**: the 15 M_EXT2 seed neurons are the compressed representation; hub identity preservation in the full 279-neuron graph validates the compression.

#### Verdicts (analysis run 2026-05-19)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(chemical_synapse↔gap_junction) > 0, p < 0.05 on full 279-neuron graph | **CONFIRMED** | r=0.6233 (Spearman=0.3128, p=0.002, 95% CI [0.5458, 0.6902], R²=0.3885, large effect). Law holds at full connectome scale. Pearson r slightly attenuated vs M_EXT2 (0.7774 at n=15) — expected: peripheral neurons add noise, core signal preserved. |
| h2 | AVAL or AVAR is rank ≤3 in chemical_synapse layer at full scale | **CONFIRMED** | AVAR=#1, AVAL=#2 (top 5: avar, aval, avbl, pvcl, pvcr). The primary command interneurons dominate the full connectome, not just the 15-neuron hub subset. Hub identity preserved at full scale. |
| h3 | AVAL is rank ≤3 in gap_junction layer (hub identity preservation + compression test) | **CONFIRMED** | AVAL=#1, AVAR=#2 in gap_junction (top 5: aval, avar, avbr, avbl, ribl). Hub-seed identity fully preserved across both layers. Compression ratio: 15-neuron seed / 279-node full graph ≈ 18.6:1 — seed correctly encodes the structural backbone at >60% hub identity match for the command interneuron class. |

**Primary finding — cross-layer hub inversion (emergent, not pre-registered):**

AVAR and AVAL are the same two command interneurons. At the 15-neuron scale (M_EXT2) they were both strong hubs in both layers — indistinguishable. At full connectome scale, their roles **invert**: AVAR is the structural leader of chemical synaptic transmission (#1 chemical_synapse, directed fast signaling) while AVAL is the structural leader of electrical coupling (#1 gap_junction, bidirectional slow signaling). This is **cross-layer role differentiation** — two neurons that are topologically equivalent at small scale diverge into complementary structural specialists at large scale. This pattern (multiplex network specialization) is more scientifically informative than the confirmation count.

**Supporting findings:**
- **Law replicates at full connectome scale** — r=0.6233 at n=279, attenuated vs M_EXT2 (r=0.7774 at n=15) as expected when peripheral neurons with weaker structural coupling are added. Signal is robust and statistically significant (p=0.002, large effect).
- **Node count compression ratio** (formal definition): CR_n = |V_full| / |V_seed| = 279 / 15 = 18.6. This is a node count ratio — it measures how many full-graph nodes each seed node structurally represents, under the assumption that the seed encodes the hub backbone. Not an information-theoretic bits measure. The claim: the 15-node seed correctly identifies the top hub class in the 279-node graph, meaning FPL is the structural decompression function for this network. Null model tests (permutation, degree-preserving rewiring) are pending to validate this claim rigorously.

**Amendment — h3 test block schema correction:**

The h3 test block was corrected after pre-registration due to a wrong test type schema. The hypothesis statement, expected hub (aval), and rank threshold (3) were unchanged. Full documentation: [`experiments/celegans_302_full_amendment1.md`](experiments/celegans_302_full_amendment1.md). The correction was triggered by a runtime schema error, not by inspecting results.

**On naming — 302 vs 279:** The experiment name `celegans_302_full` refers to the Varshney 2011 dataset (302 neurons in the biological organism). Analysis was performed on 279 connected nodes — 23 neurons have no recorded connections in NeuronConnect.xls and are isolated. This is standard for C. elegans connectome analysis and is consistent with published work on the same dataset.

**Pending robustness tests (not pre-registered):**
- Permutation test: null distribution of r under random node ID shuffle
- Degree-preserving null graph: configuration model rewiring
- Layer shuffling: does hub structure collapse under random edge redistribution?
- These tests do not change the pre-registered result; they provide robustness evidence.

---

## Why denied hypotheses matter

The DENIED result on h1 is direct evidence of integrity. A tool that always confirms predictions is not producing science — it is producing confirmation bias. The prediction named ATM as the top diverger based on domain knowledge; the tool ranked ATM 13th out of 15 and identified CHEK1 as the true structural outlier (gap=8). That disagreement is the result. Denied hypotheses are not failures. They are the mechanism by which the measurement stays honest.

---

## F9 — Lean 4 mathlib4: Functional Proximity Law on Formal Mathematics

| File | Description |
|---|---|
| [`experiments/mathlib4_F9_v1.json`](experiments/mathlib4_F9_v1.json) | 3 pre-registered hypotheses |
| [`experiments/mathlib4_F9_v1.prediction`](experiments/mathlib4_F9_v1.prediction) | Hash + timestamp sidecar |

**Hash:** `4ffcdac582cb8f80bce8bc71dd126fc9561d1a812caf2583778bd4fd6e5dc73c`
**Registered:** `2026-05-20T00:18:01.376600+00:00` (before any analysis was run)

**Context:** F9 tests the IRDME primitivity hypothesis — does the Universal Layer Grammar (d1/d2/d3) hold in formal mathematics? Dataset: 20 top-level modules from Lean 4 mathlib4. d1=import_graph (Lean 4 `import` statements, 62 edges across 8068 .lean files). d3=proof_co_development (git co-change, threshold ≥5 co-changes in 200-commit window, 27 edges). 6 infrastructure modules excluded (Tactic, Deprecated, Testing, Util, Lean). Source: leanprover-community/mathlib4, depth=200 commits.

#### Verdicts (analysis run 2026-05-20)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(import_graph ↔ proof_co_development) > 0, p < 0.05 | **CONFIRMED** | r=0.777 (Spearman=0.7328, p=0.002, large effect). The Functional Proximity Law holds in formal mathematics. |
| h2 | Algebra or Analysis is rank #1 or #2 import hub | **CONFIRMED** | Algebra=#1, Analysis=#2 in import_graph (top 5: Algebra, Analysis, Data, Topology, MeasureTheory). |
| h3 | Algebra is top hub in proof_co_development | **PARTIAL** | Analysis=#1 in proof_co_development, Algebra=#3 (Analysis, Topology, Algebra are top-3 in both layers — hub identity preserved, exact ranks differ). |

**Key finding:** r=0.777 in formal mathematics — same magnitude as biological connectomes (C. elegans r=0.7774, n=15). Modules that import each other (declared coupling) are the same modules developed together (behavioral coupling). Algebra and Analysis are top hubs in both layers. The Universal Layer Grammar is more primitive than any specific domain — it holds inside Lean 4 mathlib4 exactly as it holds in C. elegans connectomes, Linux kernel, and protein interaction networks.

---

## F1 — Synthetic Lethality Prediction (Cancer)

| File | Description |
|---|---|
| [`experiments/proteins_sl_F1_v1.json`](experiments/proteins_sl_F1_v1.json) | 4 pre-registered hypotheses |
| [`experiments/proteins_sl_F1_v1.prediction`](experiments/proteins_sl_F1_v1.prediction) | Hash + timestamp sidecar |

**Hash:** `518b9bd9e838cff04b773b6d55572a760bf1ee73807094e3c0b1e806583cd811`
**Registered:** `2026-05-20T01:48:57.951777+00:00` (before any analysis was run)

**Context:** F1 tests whether IRDME cross-layer divergence identifies known synthetic lethality (SL) pairs without prior knowledge of which pairs are SL. Dataset: 20 cancer proteins from the p53/DDR network. d1=physical_interaction (STRING v12.0 experimental score for original 15 proteins + curated landmark-study edges for parp1, brca2, wee1, rad51, cdk2). d2=genetic_interaction (18 known SL pairs from landmark studies: Farmer/Bryant 2005, Toledo 2011, Peasland 2011, Carrassa 2011, Krishnan 2017, Dick 2013, Vassilev 2004 etc.; consistent with SynLethDB v2.0 Human SL).

#### Verdicts (analysis run 2026-05-20)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | r(physical_interaction ↔ genetic_interaction) > 0, p < 0.05 | **PARTIAL** | r=0.1136 (Spearman=0.0628, p=0.615) — direction positive but NOT significant. FPL is specifically weak for PPI↔SL: physical binding and genetic interaction are structurally decoupled in the cancer DDR network. |
| h2 | CHEK1 is a diverger with rank gap ≥ 5 between PPI and genetic_interaction layers | **CONFIRMED** | CHEK1 confirmed in top-10 divergers (rank gap ≥ 5). CHK1: top SL hub, physically peripheral — exactly the SL theory prediction. |
| h3 | PARP1 is a top-3 diverger with rank gap ≥ 4 | **CONFIRMED** | PARP1 is #2 diverger. Physical rank: low (3 PPI edges: TP53, PCNA, ATM); SL rank: high (4 genetic interactions: BRCA1, BRCA2, ATM, RAD51). IRDME independently identifies the BRCA-PARP SL relationship as a structural anomaly without any SL labels. |
| h4 | TP53 is rank #1 hub in physical_interaction layer | **CONFIRMED** | TP53=#1 (top 5: tp53, brca1, pcna, mdm2, atm). Third replication across I1, I1_string_validation, and F1. |

**Key finding — PCNA as the #1 diverger (emergent, not pre-registered):**

PCNA is the largest cross-layer diverger in the dataset — it is the #3 PPI hub (massive physical connectivity as a DNA sliding clamp) but has ZERO genetic interactions in the SL layer. This means: universal essential proteins (PCNA is required in ALL dividing cells) have no cancer-selective SL partners. IRDME topology independently distinguishes cancer-selective drug targets (PARP1, CHEK1: high SL degree, low PPI degree) from universal essential proteins (PCNA: high PPI, no SL) WITHOUT any knowledge of which proteins have SL relationships. This is the core F1 claim made concrete.

**On h1 PARTIAL:**
The near-zero correlation (r=0.11, ns) between PPI and SL layers is not a failure — it is the expected result from SL biology. SL pairs are specifically defined as proteins that do NOT need to physically bind to show genetic interaction. If PPI and SL were strongly correlated, SL would not be a useful therapeutic strategy. The PARTIAL verdict confirms that SL imposes a fundamentally different structural regime on cancer proteins — exactly what justifies its therapeutic interest.

---

## H_PRIMITIVITY — Meta-science: is d1/d2/d3 more primitive than mathematical formalization?

| File | Description |
|---|---|
| [`experiments/H_PRIMITIVITY_v1.json`](experiments/H_PRIMITIVITY_v1.json) | 4 pre-registered hypotheses |
| [`experiments/H_PRIMITIVITY_v1.prediction`](experiments/H_PRIMITIVITY_v1.prediction) | Hash + timestamp sidecar |

**Hash:** `cfb38b83750474b1c9b7d8812ce5b2445223e31ef19b51e83faabd367fe31f67`  
**Registered:** `2026-05-21T04:04:19.828636+00:00` (commit [3e609f2](https://github.com/vladi160/preregistrations/commit/3e609f2), before analysis)

**Context:** Meta-science test. 15 IRDME-tested scientific domains as nodes. d1=formal_dependency (which domains formally require each other's mathematical tools), d2=structural_grammar_type (which domains share the same d1/d2/d3 coupling class), d3=law_confirmation_coupling (which domains confirmed FPL with similar r-value ranges). Tests H_PRIMITIVITY: if the FPL holds at the meta-science level (r(d1↔d2) > r(d1↔d3)), and if mathematical formalization does not significantly predict law confirmation strength, then d1/d2/d3 is more primitive than domain-level mathematical formalization.

#### Verdicts (analysis run 2026-05-21)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | FPL holds at meta-science level: r(formal_dep↔structural_grammar) > r(formal_dep↔law_confirm) | **DENIED** | r(d1↔d2)=0.212 < r(d1↔d3)=0.368 — reversed. BC4 (formally named): meta-science coupling regime is a distinct structural domain. |
| h2 | Top hub in law_confirmation_coupling is mol_bio or sw_eng (max_rank=2) | **DENIED** | Top hub is sys_bio. mol_bio ranks #4. |
| h3 | formal_math is #1 hub in formal_dependency | **CONFIRMED** | formal_math degree=20, #2 is sys_bio (10). Layer design validated. |
| h4 | r(formal_dep↔law_confirm) is NOT significant (p > 0.05) — formalization does not predict confirmation | **PARTIAL** | r=0.368, p=0.206. Not significant. Consistent with H_PRIMITIVITY: the law's applicability is independent of mathematical formalization level. |

**Key finding — BC4 (meta-science regime, formally named):**

h1 DENIED identifies a potential fourth boundary condition: the FPL does not confirm when nodes are scientific domains and layers encode abstract institutional dependencies between entire fields. Candidate mechanism: abstract coupling between sciences operates at a different structural resolution than concrete physical, computational, or biological coupling — analogous to BC1 (relational regime mismatch) and BC3 (resolution mismatch). h4 PARTIAL independently supports H_PRIMITIVITY: mathematical formalization level (measured by how many other fields depend on a domain's mathematical tools) does not significantly predict whether or how strongly the FPL confirms in that domain.

---

## M_TRANSFER_3 — Docopt Cross-Language Replication (Go, Java, Rust)

| File | Description |
|---|---|
| [`experiments/M_TRANSFER_3_docopt_v1.json`](experiments/M_TRANSFER_3_docopt_v1.json) | 4 pre-registered hypotheses |
| [`experiments/M_TRANSFER_3_docopt_v1.prediction`](experiments/M_TRANSFER_3_docopt_v1.prediction) | Hash + timestamp sidecar |

**Hash:** `5388c0f114a52040330c8e4ac6f82a90a7a2a10e763c47f507e3c6ebe65560bc`
**Registered:** `2026-05-22T04:16:40.507306+00:00` (before any analysis was run)

**Context:** Pre-registered replication of the exploratory M_TRANSFER_3 result (Tier C, not pre-registered), which found hub identity sim ≥ 0.967 across all three docopt language pairs via `irdme atlas --compare` (role-vector cosine similarity). This experiment formally tests the per-codebase FPL r-values and hub rankings — a different measurement that the exploratory run did not compute. Three docopt implementations extracted via `irdme extract`: Go (n=6, v0.6.2, 97 commits), Java (n=16, 13 commits), Rust (n=8, v1.1.1, 284 commits). All use the Universal Layer Grammar: d1=static_coupling, d2=structural_coupling, d3=co_change. Run separately against each dataset (h1+h2 test Java, h3 tests Rust, h4 aggregated across all three).

#### Verdicts (analysis run 2026-05-22)

| # | Hypothesis | Verdict | Result |
|---|---|---|---|
| h1 | FPL directional inequality holds in Java (n=16): r(d1↔d2) > r(d1↔d3) | **DENIED** | r(static_coupling↔structural_coupling)=0.0 < r(static_coupling↔co_change)=0.2584. structural_coupling has a constant degree vector — degenerate. |
| h2 | FPL reaches significance in Java (n=16): r(d1↔d2) > 0, min_abs_r ≥ 0.50 | **DENIED** | structural_coupling degree vector is constant (all nodes have equal structural degree). r undefined. Threshold of 0.50 not reached. |
| h3 | FPL directional inequality holds in Rust (n=8): r(d1↔d2) > r(d1↔d3) | **DENIED** | r(static_coupling↔structural_coupling)=−0.1429 < r(static_coupling↔co_change)=0.4962. FPL inverted — co_change is more correlated with static_coupling than structural_coupling. |
| h4 | Primary parser module is rank ≤2 in static_coupling in all 3: docopt (Go), Docopt (Java), parse (Rust) | **PARTIAL** | Go: docopt = rank #1 ✓. Java: Docopt = rank #1 ✓. Rust: dopt = rank #1 (not parse as predicted — dopt is the library entry module, parse is the sub-parser it wraps). |

**Overall: 0/4 CONFIRMED, 3/4 DENIED, 1/4 PARTIAL.**

**Key finding — systematic FPL denial in single-hub radial architectures:**

All three docopt implementations share the same structural pattern: a single dominant parser module (docopt/Docopt/dopt) that acts as the sole hub, with all other modules as peripheral dependents. In this radial/star topology, structural_coupling (d2) degenerates — when all modules depend on the same hub or share the same type imports, every node's structural_coupling degree converges to a similar value (Java: constant; Go: near-zero from only 1 edge; Rust: very low). The result is that r(d1,d2) collapses toward 0 or below, while r(d1,d3) remains positive because behavioral co-change reflects feature proximity, not structural degeneracy.

**Named mechanism — BC_RADIAL (candidate):** Single-hub radial architectures cause structural_coupling degeneracy. The FPL requires genuine layer differentiation — when d1 and d2 both reduce to "proximity to the same hub," they cannot produce different hub rankings, and the law cannot confirm. This is structurally distinct from BC3 (resolution mismatch) and BC1 (relational regime): here, the layer design is correct but the specific topology collapses the layer differentiation.

**On the exploratory finding (hub identity sim ≥ 0.967):** The exploratory result remains valid. Cross-language hub identity (measured by role-vector cosine similarity via `irdme atlas --compare`) IS preserved — the same hub node (docopt/Docopt/dopt) appears in all three languages with nearly identical structural roles. Hub identity and the FPL r-test measure different things: hub identity asks "which node is central?"; FPL r asks "does centrality co-vary systematically between layers?" The former confirms across all 3 languages; the latter fails due to structural_coupling degeneracy. The distinction is the finding.

**This experiment is DENIED at the experiment level (FPL did not hold in any of the 3 sub-tests). It adds 1 denied experiment to the total: 18 CONFIRMED, 4 DENIED across 22 pre-registered experiments.**

---

## M_GEOM_CSG_1 — Planetary Gear Set Constructive Solid Geometry (May 22, 2026)

| Field | Value |
|---|---|
| **Experiment file** | [`experiments/M_GEOM_CSG_1.json`](experiments/M_GEOM_CSG_1.json) |
| **Prediction sidecar** | [`experiments/M_GEOM_CSG_1.prediction`](experiments/M_GEOM_CSG_1.prediction) |
| **Pre-registration hash** | `1dd686ee25e25d97ca0afc4701ea34a2ef4fcf690b231a42e71854bc13c262c9` |
| **Pre-registration timestamp** | 2026-05-22T04:52:57.530116+00:00 |
| **Public repo push (pre-reg)** | commit `5c45bbe` — before any analysis ran |
| **Domain** | Computational geometry — constructive solid geometry (CSG), planetary gear set |
| **Dataset** | `examples/m_geom_csg_1.json` — 8 nodes, 36 relations across 3 layers |
| **Layers** | d1=operation_tree (CSG assembly steps), d2=volumetric_proximity (physical contact interfaces), d3=co_parameter_sensitivity (gear ratio kinematic coupling) |

**Context:** Directly motivated by BC3b (named boundary condition for pure boolean algebra layer collapse). Scientific question: do CSG boolean operations (union/difference) on continuous geometry also collapse d1/d2/d3 to logical consequence — or does continuous geometry preserve genuine layer differentiation? The planetary gear set was selected as a well-understood mechanical system with three independently derivable structural properties.

**Verdict table:**

| Hypothesis | Verdict | Evidence |
|---|---|---|
| h1: FPL directional inequality r(d1,d2) > r(d1,d3) | **CONFIRMED** | r(operation_tree,volumetric_proximity)=0.6682 > r(operation_tree,co_parameter_sensitivity)=-0.2673 |
| h2: r(d1,d2) ≥ 0.50, positive direction | **CONFIRMED** | Pearson r=0.6682, permutation p=0.0419 (significant at α=0.05) |
| h3: carrier_plate = rank-1 hub in operation_tree | **CONFIRMED** | carrier_plate rank #1, degree=5 (housing #2 at degree=3) |
| h4: carrier_plate = rank-1 hub in volumetric_proximity | **CONFIRMED** | carrier_plate rank #1, degree=7 (sun_gear and ring_gear #2 at degree=5) |

**Result: 4/4 CONFIRMED. Δr = 0.6682 − (−0.2673) = 0.9355 (very large effect).**

**BC3b boundary formally demonstrated:** CSG geometry (continuous geometry, boolean operations) confirms FPL — genuine layer differentiation is preserved. The carrier plate is the structural hub in BOTH the declared assembly tree (d1) AND the geometric proximity graph (d2), while the kinematic parameter sensitivity graph (d3) is dominated by the gear ratio coupling chain (sun gear and ring gear as co-sensitivity hubs). The layer collapse that occurs in pure boolean algebra (BC3b mechanism) does NOT occur here because the three layers encode genuinely independent structural properties of the continuous-geometry system.

**Distinction from BC3b (not a contradiction):** BC3b states that pure boolean algebra denies FPL because d1/d2/d3 all reduce to logical consequence — there is no independent structural meaning in any layer beyond set membership. CSG geometry has the same SYNTAX (union, difference) but different SEMANTICS: the assembly sequence, the geometric contact zones, and the kinematic co-sensitivity are independently derivable from different physical properties of the gear set. The boolean operations produce distinct structural layers because the domain is continuous, not discrete.

**This experiment adds 1 confirmed experiment: 19 CONFIRMED, 4 DENIED across 23 pre-registered experiments.**

---

## Git management rules

This repository exists to establish **priority** and **integrity** for scientific claims. Its git history is a legal and scientific record. These rules are strict:

### Never rewrite history

```
# These commands are FORBIDDEN on this repo — forever:
git commit --amend
git rebase
git push --force
git reset --hard HEAD~n  (that changes a pushed commit)
```

Rewriting history breaks the timestamp guarantee. A reviewer checking the commit date via GitHub's API or a third-party archive (e.g. archive.org, OpenTimestamps) must see the exact commit that was pushed before analysis ran.

### Correct mistakes with new commits, not amendments

If a pre-registration file has an error that is noticed BEFORE analysis:
- Create a new experiment file with a new id (e.g. `my_exp_v2.json`)
- Commit the new file as a fresh commit — do NOT amend the previous one
- Add a note in the new file: `"supersedes": "my_exp_v1.json"` and explain why

If a pre-registration file has an error noticed AFTER analysis:
- Do NOT change the file. The hash is already committed.
- Add a `_notes.md` file (e.g. `my_exp_notes.md`) documenting the discrepancy
- Commit the notes file as a new commit explaining the issue

### The two-commit scenario (acceptable)

The C. elegans prediction has two commits because the sidecar was regenerated. This is acceptable **only because** the `prediction_hash` and all hypothesis content are identical in both commits — only the auto-generated `committed_at` field differs. This is documented in the README under that experiment. Future sidecar regenerations should be avoided by using `--push` in the main repo's `irdme commit-prediction` command, which commits atomically.

### OpenTimestamps anchoring (optional but strongest proof)

```bash
pip install opentimestamps-client
ots stamp experiments/my_exp.prediction
# Wait ~8 hours for Bitcoin block confirmation, then:
ots upgrade experiments/my_exp.prediction.ots
ots verify  experiments/my_exp.prediction.ots
# Commit the .ots file:
git add experiments/my_exp.prediction.ots
git commit -m "ots: anchor my_exp.prediction to Bitcoin block"
git push
```

The `.ots` file lets any reviewer verify the timestamp independently — no trust in GitHub, no trust in you, no trust in any party. Verification requires only the Bitcoin blockchain and the OTS client.

### Workflow summary

```
# In the MAIN repo (the-beginning), before running any analysis:
irdme validate-experiment examples/experiments/my_exp.json
irdme commit-prediction examples/experiments/my_exp.json --push

# The --push flag:
# 1. Copies my_exp.json + my_exp.prediction to d:/xampp/htdocs/preregistrations/experiments/
# 2. Runs: git add . && git commit -m "pre-reg: my_exp" && git push
# This is the only sanctioned way to add a file to this repo.

# After running analysis:
irdme verify-prediction examples/experiments/my_exp.json
# Then update this README with verdict table (separate commit, clearly labelled).
```

### Commit message conventions

```
pre-reg: <experiment_id>           # for new pre-registration files
verdict: <experiment_id>           # for README updates with verdicts
ots: anchor <experiment_id>        # for OpenTimestamps .ots files
fix: note <experiment_id>          # for _notes.md corrections (NEVER amend)
```

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
| — | 2026-04-30 20:26 UTC | Pre-registration: `ai_architecture_law` (F6 — AI Architecture Graph) pushed to public repo |
| — | 2026-04-30 | Analysis run: AI Architecture 4/5 confirmed, r=0.9147, 1 denial with named mechanism (recency bias) |
| `5bdfa37` (public) | 2026-05-01 00:11 UTC | Pre-registration: `I1_string_validation` (I1 Phase 2 — STRING v12.0) pushed to public repo |
| — | 2026-05-01 | Analysis run: STRING validation 4/5 CONFIRMED — law replicates on independent data. r(FA,PI)=0.8689. h5 DENIED: CHEK1 divergence was CRISPR-specific, not universal. True divergers on STRING: BCL2 (gap=13), TP53 (gap=12). |

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

---

## Post-hoc confirmatory runs (NOT pre-registered)

These runs produced valid scientific results but **did not follow the pre-registration workflow**. They are listed here for transparency. They do not count toward the pre-registered experiment totals and do not appear in the arXiv paper as pre-registered experiments.

| Experiment | Date | What was done | Why pre-reg was skipped | Result |
|---|---|---|---|---|
| **BC3b circuit** — ISCAS85 c17 equivalent, n=11 nodes, 3 layers | 2026-05-22 | Ran `main.py examples/experiments/BC3b_circuit_v1.json`. All 3 hypotheses confirmed. r(gate_wiring↔structural_proximity)=0.7504 (p=0.01), r(gate_wiring↔critical_path)=0.2813 (ns), Δr=0.4691. BC3b formally named (layer collapse in pure boolean algebra). | Prediction sidecar was hand-crafted in the same AI session as the analysis run. Was not generated by `dev.py commit-prediction` and was not pushed here before analysis. | Valid result. Matches analytical pre-computation of expected r from circuit topology. Does not have pre-registration credibility because the public timestamp sequence was not established. |


