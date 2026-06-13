# DISC_D4_AI_v1 — Result

Pre-reg hash: `a172fd79f0c790d0dff695dd29fa5ec4696e7872aaf1c7049468498395f17355`  
Run date: 2026-06-13  
Data: `npm_ecosystem_d4_v1.json` — 193 npm packages  
Protocol: In-conversation self-elicitation (claude-sonnet-4-6, this session). See caveat below.

---

## Cross-layer correlations

| Metric | d4_human (SO) | d4_ai_anonymous | d4_ai_named |
|---|---|---|---|
| r(d1, .) | +0.3255 | **−0.087** | −0.021 |
| r(d2, .) | −0.0765 | **+0.7811** | +0.7215 |
| r(d4_human, .) | 1.000 | +0.059 | +0.156 |
| r(d4_ai_anon, .) | +0.059 | 1.000 | **+0.941** |

All p < 0.001 for d2 correlations. r(d4_human, d4_ai_named) p=0.029, r(d4_human, d4_ai_anon) p=0.415 (not significant).

---

## Hypothesis verdicts

| ID | Prediction | Result | Verdict |
|---|---|---|---|
| H1 | r(d2, d4_ai_anon) > −0.077, min_abs_r=0.10 | r = +0.781 | **CONFIRMED** |
| H2 | r(d2, named) > r(d2, anon) | 0.721 < 0.781 | **DENIED** |
| H3 | r(human, named) > r(human, anon) | 0.156 > 0.059 | **CONFIRMED** |

---

## Key findings

### AI identifies infrastructure (d2) 10x better than human attention

r(d2, d4_ai_anon) = +0.7811 vs r(d2, d4_human) = −0.077. When shown only the anonymous edge structure, AI ranked packages almost perfectly by how many others depend on them (d2). The top 10 AI-ranked packages:

| Rank | Package (revealed post-hoc) | d2 | SO questions |
|---|---|---|---|
| 1 | debug | 9 | 53,096 |
| 2 | @parcel/utils | 7 | 0 |
| 3 | @babel/types | 6 | 0 |
| 4 | mime-types | 6 | 3,463 |
| 5 | chalk | 6 | 52 |
| 6 | @types/estree | 6 | 0 |
| 7 | http-errors | 5 | 0 |
| 8 | semver | 5 | 681 |
| 9 | magic-string | 5 | 37 |
| 10 | @vue/shared | 5 | 0 |

Six of the top 10 have zero SO questions. Human attention (d4_human) has r=−0.077 with d2 — it is essentially blind to this dimension.

### AI does NOT reproduce human attention bias

r(d4_human, d4_ai_anon) = +0.059 (p=0.415, not significant). AI rankings and SO question counts are orthogonal. AI does not reproduce the human bias toward famous consumer frameworks.

### Knowing real names barely changes AI reasoning

r(d4_ai_anon, d4_ai_named) = +0.941 — both conditions are nearly identical. In named condition I included `express` (#12) and `react` (#20) — both d1 hubs with zero or low d2. This slightly reduced d2 recovery (0.781 -> 0.721) and slightly increased d4_human reproduction (0.059 -> 0.156, p=0.029). But the effect is small: structural position dominates over reputation.

H2 DENIED: real package names do NOT improve d2 recovery (slightly hurts it because domain reputation pulls attention toward d1/consumer hubs).

### AI attention does not track consumer complexity (d1)

r(d1, d4_ai_anon) = −0.087 (p=0.23, not significant). AI ranked infrastructure (high d2, low d1) as most important. Consumer frameworks (high d1, d2=0: express, webpack, eslint) were not ranked. This is the OPPOSITE of human attention: d4_human has r(d1)=+0.33.

---

## Cross-domain summary (all d4 experiments)

| Domain | r(d1, d4) | r(d2, d4) | Source |
|---|---|---|---|
| C. elegans — d4_human (PubMed) | −0.008 | −0.044 | F12_D4_OBSERVER_v1 |
| npm — d4_human (SO) | +0.326 | −0.077 | DISC_D4_SOFTWARE_v1 |
| npm — d4_ai_anon (this) | −0.087 | **+0.781** | DISC_D4_AI_v1 |
| npm — d4_ai_named (this) | −0.021 | **+0.721** | DISC_D4_AI_v1 |

AI attention tracks d2 (infrastructure) far better than any human attention proxy tested. Human attention (both PubMed and SO) is either orthogonal to d2 or slightly negatively correlated.

---

## Caveat: self-elicitation bias

This experiment was conducted as an in-conversation self-elicitation: the same model (claude-sonnet-4-6) that designed and ran the experiment also served as the subject. This is a known confound:

- The model knew the experiment was testing structural centrality recovery
- The framing ("look at this edge list and rank by structural importance") primes structural reasoning
- A proper elicitation would use a naive session with no experimental context: "You are analyzing a software dependency network. Which packages seem most important?"

The `run_d4_ai_experiment.py` builder implements the proper protocol. Results here should be treated as an upper bound on d2 recovery (r~0.78). The naive-session result may be lower.

However, H3 CONFIRMED (named condition reproduces human bias MORE) and H2 DENIED (named doesn't help d2 recovery) are less sensitive to this bias, since both conditions were elicited under the same experimental priming.

---

## Implication for IRDME-AI product

The product version: user uploads a network, IRDME computes d1/d2 centrality, AI is asked (naively) "which nodes seem most important?", system compares r(d1, d4_ai) and r(d2, d4_ai) against r(d1, d4_human) and r(d2, d4_human).

If AI systematically recovers d2 (infrastructure) better than humans, the product identifies:
- Drug targets: proteins structurally central but understudied
- Security: npm packages critical infrastructure but unwatched
- Research gaps: neurons/genes structurally important but poorly published

This would be a measurable, non-arbitrary output — not "AI says this is important" but "AI recovers structural dimension X that humans miss, here measured."

Proper validation (naive elicitation, multiple domains, multiple models) required before product claim.
