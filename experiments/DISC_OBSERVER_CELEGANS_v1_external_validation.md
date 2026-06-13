# DISC_OBSERVER_CELEGANS_v1 — External Validation Results

Pre-registration: `DISC_OBSERVER_CELEGANS_v1.json`  
Pre-registration hash: `c211d58eaaca17198e7460826e119f45e1c1ae5c987b8123c3ac5e3b01eabb30`  
Amendment (null model + SSPH framing): `DISC_OBSERVER_CELEGANS_v1_amendment.json`  
Date collected: 2026-06-14  
Collector: vladi160  

---

## Protocol

Five AI systems queried in fresh external sessions (no prior context about IRDME or FPL):
- ChatGPT (web version, exact model unknown)
- Grok Fast 4.3
- Claude Sonnet 4.6 (chat, instructed "do not use any tools")
- NotebookLM (source uploaded, then queried)
- Google AI Search Mode

Two prompt conditions (as pre-registered):
- **Prompt A (named)**: C. elegans edge list with real neuron names (AVAR, AVAL, …); question "Which 20 neurons do you think are most important or widely connected?"
- **Prompt B (anon)**: Same edge list with anonymized IDs (nrn_001…nrn_185); question "Which 20 nodes do you think are most important or most widely connected?"

**Tool-use note**: Grok displayed "parsing" and "request" indicators during response, suggesting possible web or code tool activation. Claude chat was explicitly instructed not to use tools. Google AI Search Mode may use internal computation. Results are noted alongside tool-use status.

Network: n=185 neurons, 1,655 chemical synapses (threshold total_degree≥10, Varshney 2011).  
Human baseline (PubMed co-mention, from F12_D4_OBSERVER_v1): r(d2, d4_human) = -0.044, r(d1, d4_human) = -0.008.  
Network property: r(d1, d2) = +0.317 in this subgraph (moderate positive; contrasts with npm where r(d1,d2) = -0.31).

---

## Results

### r(d2, d4_ai) and r(d1, d4_ai) by model and condition

| Model         | Condition | r(d1, d4_ai) | r(d2, d4_ai) | H1 (>0.10) | cmd/10 | H2 (≥6 STRONG) |
|---------------|-----------|:------------:|:------------:|:----------:|:------:|:---------------:|
| ChatGPT       | named     | +0.349       | +0.855       | YES        | 10/10  | STRONG          |
| Grok          | named     | +0.464       | +0.853       | YES        | 9/10   | STRONG          |
| Claude chat   | named     | +0.507       | +0.776       | YES        | 8/10   | STRONG          |
| NotebookLM    | named     | +0.465       | +0.852       | YES        | 9/10   | STRONG          |
| Google AI     | named     | +0.476       | +0.798       | YES        | 8/10   | STRONG          |
| ChatGPT       | anon      | +0.464       | +0.805       | YES        | 8/10   | STRONG          |
| Grok          | anon      | +0.468       | +0.850       | YES        | 9/10   | STRONG          |
| Claude chat   | anon      | +0.450       | +0.854       | YES        | 8/10   | STRONG          |
| NotebookLM    | anon      | +0.458       | +0.857       | YES        | 9/10   | STRONG          |
| Google AI     | anon      | +0.455       | +0.742       | YES        | 6/10   | STRONG          |
| **Human**     | PubMed    | -0.008       | **-0.044**   | —          | —      | —               |

**H1 confirmed: 10/10 conditions.** r(d2, d4_ai) range: [+0.742, +0.857].  
**H2_pred confirmed STRONG: 10/10 conditions.** All models recover ≥6 of 10 locomotion command interneurons in their top-20 (hypergeometric p < 0.001 for k≥6; expected overlap under null = 1.08).

---

### H2 detail: command interneuron overlap in anon top-20

Command interneurons (AVAL, AVAR, AVBL, AVBR, PVCL, PVCR, RIML, RIMR, AVDL, AVDR):

| Model      | Hits | Command interneurons recovered |
|------------|:----:|--------------------------------|
| ChatGPT    | 8/10 | AVAR, AVAL, AVBL, AVBR, AVDL, AVDR, PVCL, PVCR |
| Grok       | 9/10 | AVAR, AVAL, AVBL, AVDR, AVBR, PVCL, PVCR, AVDL, RIMR |
| Claude     | 8/10 | AVAL, AVAR, AVBL, AVBR, AVDR, PVCL, PVCR, AVDL |
| NotebookLM | 9/10 | AVAR, AVAL, AVBL, AVDR, AVBR, PVCL, PVCR, AVDL, RIMR |
| Google AI  | 6/10 | AVAR, AVAL, AVBL, AVDR, AVBR, AVDL |

RIML and RIMR (motor command, lower d2=16-17) are recovered by 2/5 models in anon condition (Grok, NotebookLM). Missed by 3/5. These are the only command neurons below d2=20 in this subgraph.

All 5 models: **0 touch neurons** (PLMR, ALML, AVM) in top-20.  
All 5 models: **0 chemosensory neurons** (AWCL, AWCR, AWAR) in top-20.

---

### H3: Named vs anon — does naming reduce d2 recovery?

| Model      | r(d2) named | r(d2) anon | Named−Anon |
|------------|:-----------:|:----------:|:----------:|
| ChatGPT    | +0.855      | +0.805     | +0.050     |
| Grok       | +0.853      | +0.850     | +0.003     |
| Claude     | +0.776      | +0.854     | -0.078     |
| NotebookLM | +0.852      | +0.857     | -0.005     |
| Google AI  | +0.798      | +0.742     | +0.056     |
| **Mean**   |             |            | **+0.005** |

**H3: NOT CONFIRMED.** Named−Anon mean = +0.005 (near zero). In C. elegans, neuron names (AVAR, AVAL, DVA…) carry no memorized popularity signal — they are lab-specific alphanumeric codes absent from human attention metrics. The semantic priming effect that suppressed ChatGPT's d2 recovery in the npm named condition does not apply here. This null result is informative: the named→anon gap is domain-specific, appearing only when names encode popularity information.

---

### Cross-model correlation matrix (anon condition)

|            | ChatGPT | Grok   | Claude | NbkLM  | Google |
|------------|:-------:|:------:|:------:|:------:|:------:|
| ChatGPT    | +1.000  | +0.946 | +0.951 | +0.944 | +0.778 |
| Grok       | +0.946  | +1.000 | +0.983 | +0.996 | +0.817 |
| Claude     | +0.951  | +0.983 | +1.000 | +0.983 | +0.815 |
| NotebookLM | +0.944  | +0.996 | +0.983 | +1.000 | +0.801 |
| Google AI  | +0.778  | +0.817 | +0.815 | +0.801 | +1.000 |

Min pairwise r = +0.778 (ChatGPT × Google AI). All pairs positive.  
Grok × NotebookLM = +0.996 (near-identical ranking despite different model families).

---

## Summary

**Observer Projection Law confirmed in C. elegans (second domain).**

AI structural attention projects onto d2 (in-degree / how many neurons depend on a node) far more strongly than human scientific literature attention does. Human PubMed attention shows r(d2) = -0.044 in this network; all 5 AI systems in both conditions show r(d2) = +0.74 to +0.86, a gap of ~0.80 r-units.

The AI ranking projection aligns with the lesion-importance distribution (White 1986 ablation ground truth) well above random expectation: 6-9 of 10 locomotion command interneurons recovered in the anonymous condition (expected overlap under null = 1.08; p < 0.001 for k≥6).

Human scientific literature has accumulated near-zero PubMed co-mention counts for AVAL, AVAR, AVBL, AVBR (the primary locomotion command neurons with highest d2 in the subgraph). These neurons are invisible to human attention as measured by co-citation but are recovered by all 5 AI systems without any biological knowledge, from structure alone.

This is not a claim that AI "discovers" function. The correct interpretation (per SSPH framing in the amendment): AI ranking projection and lesion-importance distributions are aligned because both are sensitive to d2 (in-degree), which is the structural proxy for load-bearing position. Human literature attention is not.

---

## Methodological notes

1. **r(d1) positive in all conditions** (~+0.35 to +0.51): Unlike npm where r(d1) and r(d2) were opposing (network bimodality), in C. elegans r(d1,d2)=+0.317. Neurons with high in-degree also tend to have high out-degree. r(d2) exceeds r(d1) in all 10 conditions, confirming d2 dominance, but the gap is smaller than in npm.

2. **Google AI lower r(d2) in anon (+0.742 vs +0.78–0.86 for others)**: Consistent with npm finding that Google AI and code-execution models compute something closer to total degree or transitive reach rather than strict in-degree ranking. Result is still strongly H1-confirmed.

3. **H3 null result is informative**: Semantic name interference (named condition suppressing d2 recovery) occurred in npm but not C. elegans. Condition for the effect: names must encode popularity prior (npm package names carry usage frequency associations; C. elegans neuron names do not).

4. **Tool use**: Grok showed tool-activation indicators. Results are indistinguishable from tool-free models. This suggests the structural d2 signal is recoverable both by pure reasoning and by computational analysis — both routes converge on the same structural dimension.
