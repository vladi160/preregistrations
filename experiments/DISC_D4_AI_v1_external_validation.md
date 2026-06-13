# DISC_D4_AI_v1 -- External AI Validation

Date: 2026-06-13  
Linked pre-registration: DISC_D4_AI_v1.json  
Linked result: DISC_D4_AI_v1_result.md (self-elicitation, upper bound)  
Protocol: 5 AI systems, 2 prompts each (Prompt A: named+neutral, Prompt B: anon+neutral), separate fresh sessions, no structural priming.

---

## Models tested

| Label | System | Condition notes |
|---|---|---|
| notebooklm | Google NotebookLM | Source uploaded as document, system pre-analyzed before question |
| claude_chat | Claude.ai Sonnet 4.6 (separate session) | Used code execution (computed transitive reach) |
| grok | Grok 4.3 fast (xAI) | Reasoning only, no code |
| chatgpt | ChatGPT (model version unconfirmed, "Stopped thinking" prefix) | Reasoning only, no code |
| googleai | Google AI Search Mode (Gemini-based) | Used code execution (computed transitive reach/in-degree) |

---

## Results

### r(d2, d4_ai) -- all conditions

| Model | Named (Prompt A) | Anon (Prompt B) |
|---|---|---|
| notebooklm | +0.7706 | +0.7869 |
| claude_chat | +0.6464 | +0.5595 |
| grok | +0.6235 | +0.7735 |
| chatgpt | +0.4898 | +0.6760 |
| googleai | +0.7057 | +0.5299 |
| **median** | **+0.646** | **+0.676** |
| self-elicitation (structured) | +0.7215 | +0.7811 |
| d4_human (SO baseline) | -- | -0.0765 |

All p < 0.001 (each model individually). All 10/10 conditions: H1 CONFIRMED.

### r(d1, d4_ai) -- structural coupling (outbound degree)

All conditions: r(d1, d4_ai) in range [-0.107, +0.087], none significant. No model tracks consumer complexity (outbound dependencies). Consistent with self-elicitation result.

### r(SO, d4_ai) -- human attention reproduction

| Model | Named | Anon |
|---|---|---|
| notebooklm | +0.059 | +0.058 |
| claude_chat | +0.060 | +0.041 |
| grok | +0.152* | +0.058 |
| chatgpt | +0.230** | +0.057 |
| googleai | +0.061 | +0.041 |

*p=0.034, **p=0.001. All anon conditions: r(SO, d4_ai) ~ 0.05, not significant. Named condition injects modest SO-bias for grok and chatgpt -- confirming H3 directionally (named condition pulls AI attention slightly toward SO-famous packages).

---

## H1 -- AI naive attention recovers d2 better than human attention

**CONFIRMED: 10/10 conditions.**  
Min r = +0.490 (chatgpt_named), max r = +0.787 (notebooklm_anon).  
Baseline: r(d2, d4_human) = -0.077.  
All conditions exceed baseline by >0.55 r-units.

## H2 -- Named condition does not improve d2 recovery over anon

**CONFIRMED for 3/5 models, DENIED for 2/5.**  
- notebooklm: named=0.771, anon=0.787 -- negligible difference (H2: named worse)
- claude_chat: named=0.646, anon=0.560 -- named BETTER (H2 denied for this model)
- grok: named=0.624, anon=0.774 -- anon better (H2 confirmed)
- chatgpt: named=0.490, anon=0.676 -- anon better, largest gap (H2 confirmed)
- googleai: named=0.706, anon=0.530 -- named better (H2 denied)

Pattern: models using code execution (claude_chat, googleai) perform better in the named condition. Reasoning-only models (grok, chatgpt) perform better in the anonymous condition. Hypothesis: real names add semantic noise for reasoning models; code-based models compute in-degree regardless of names.

## H3 -- Named condition reproduces SO bias more than anon

**CONFIRMED directionally: 5/5 models show r(SO, named) >= r(SO, anon).**  
Strongest effect: chatgpt (named=+0.230 vs anon=+0.057). Second: grok (0.152 vs 0.058). Other models: marginal (+0.01-0.02 difference). Overall: naming packages does pull AI attention toward SO-known frameworks, but effect is small for most models.

---

## Cross-model consistency (anon condition)

| Pair | r |
|---|---|
| notebooklm vs grok | +0.970 |
| claude_chat vs googleai | +0.989 |
| notebooklm vs chatgpt | +0.843 |
| grok vs chatgpt | +0.848 |
| notebooklm vs claude_chat | +0.604 |
| notebooklm vs googleai | +0.561 |
| claude_chat vs grok | +0.646 |
| claude_chat vs chatgpt | +0.557 |
| grok vs googleai | +0.610 |
| chatgpt vs googleai | +0.509 |

Min: +0.509. All positive. Two clusters visible: (notebooklm + grok + chatgpt) and (claude_chat + googleai). The claude/googleai cluster reflects shared code-execution methodology (both computed transitive reach explicitly). The other cluster reflects reasoning-based attention. Despite different methodologies, all correlate positively with each other and all strongly with d2.

---

## Structural priming effect (self-elicitation bias)

Comparing self-elicitation (structured, same session) vs external naive:

| Condition | Self-elicitation | Naive (median external) | Delta |
|---|---|---|---|
| Anonymous | +0.781 | +0.676 | +0.105 |
| Named | +0.722 | +0.646 | +0.076 |

Structural priming inflated r by approximately +0.08-0.11. This is a real effect but not large enough to explain the finding: even without priming, r(d2, d4_ai_naive) >> r(d2, d4_human) = -0.077. The self-elicitation result was a valid upper bound, not an artifact.

---

## Top-10 consensus (anon condition)

Packages appearing in all 5 top-10 lists: debug, @babel/types  
Packages appearing in 4/5: chalk, @parcel/utils, mime-types (or mime-db), @types/estree or @parcel/diagnostic  
Packages appearing in 0/5 top-10: react, express, webpack, eslint, vue (the SO-famous consumer frameworks with d2=0)

The consensus top-10 is dominated by packages with d2 >= 4, most with SO question counts near 0. This is the same pattern as self-elicitation.

---

## Methodological notes

1. **NotebookLM**: Source file uploaded as document, system pre-analyzed before user question. Not strictly naive -- system already processed the edge list. Result is consistent with other models (r=0.77-0.79), so pre-analysis did not produce outlier behavior.

2. **Code execution**: Claude.ai and Google AI Search Mode both wrote and ran Python code to compute in-degree/transitive reach explicitly. This is a different cognitive mode than attention/reasoning. It produces valid d2-correlated rankings but does not represent "AI attention" -- it represents "AI can compute centrality metrics from edge lists." For the attention interpretation, grok and chatgpt results are cleaner.

3. **Reasoning-only models** (grok, chatgpt): achieved r(d2, anon) = 0.68-0.77 without code. This is the cleanest evidence for the claim that AI reasoning (without explicit computation) recovers d2 better than human attention.

---

## Revised finding statement

"Five AI systems (Claude.ai, Grok, ChatGPT, Google AI, NotebookLM) were given an npm dependency edge list and asked which packages are most important, with no mention of structural centrality. All five systems, in both named and anonymous conditions (10/10 conditions), produced rankings that correlate with d2 (in-degree / infrastructural embeddedness) significantly above the human attention baseline (r_human = -0.077). Median r(d2, d4_ai_naive) = 0.66 [range 0.49-0.79]. Human attention (Stack Overflow question counts) was not reproduced: r(SO, d4_ai_anon) ~ 0.05 for all models.

For reasoning-only models without code execution (Grok, ChatGPT), r(d2, d4_ai_anon) = 0.68-0.77, suggesting that AI language model representations encode infrastructural centrality at a level humans do not consciously track via task-driven attention."
