# Pre-registered hypotheses (Phase 2: Rehearse then Recall)

Status: DRAFT, not committed. Every TBD field below must be fixed and committed BEFORE any evaluation run. Exploratory analyses are labeled as such in reports.

## Setup (fixed)

| Item | Value |
|---|---|
| Data | LongMemEval-S (cleaned, 500 questions; 30 `_abs` variants spread over 4 types) |
| Reader | `meta/llama-3.2-11b-vision-instruct` (NIM free endpoint, text-only input) |
| Judge | `gpt-4o-2024-08-06`, type-specific LongMemEval prompts, temperature 0, max_tokens 10 |
| Test | paired McNemar + bootstrap CI (matched instances) |
| Multiplicity | Holm correction over the confirmatory family below |
| Curve design | token-accuracy curve; B_w fixed at 2 values (TBD), compression ratio R swept |

## Confirmatory family (Holm)

| ID | Hypothesis | Fix before run (TBD) |
|---|---|---|
| H0 (primary) | At equal token budget, verbatim-compressed LTM is not worse than token-matched RAG (non-inferiority) | margin delta = TBD; token budget points = TBD |
| H2 | Loss of compression vs RAG differs by evidence-turn role (assistant vs user): role x method interaction | role classification rule from `has_answer` = TBD (data: user 842 vs assistant 54 turns; SS-assistant questions have 51 assistant-evidence turns, so the assistant group is small and unbalanced) |
| H4 | Thread variant B (topic description + verbatim body) beats A (pointers only) on session-level recall@k at fixed tokens, multi-session questions. Controls: A + meaningless description, or A + representative-sentence key | primary = recall@k (k = TBD), secondary = QA accuracy |
| H5a | At equal tokens, revisit ON beats OFF (beta > 0 condition) | revisit counts forcibly assigned |
| H5b | Within ON, accuracy increases monotonically with revisit count in {0,1,2,4} (dose-response) | monotonic test = TBD |

## Dropped

| ID | Reason |
|---|---|
| H1 | Token savings hold by definition; reported as descriptive statistics only |
| H3 | Merged into H2 |

## Terminology rule

Call the mechanism "repetition/rehearsal" only if BOTH dose-response (H5b) and gain (H5a) appear. Otherwise: "compression inspired by maintenance rehearsal".

## Constraints

| Item | Rule |
|---|---|
| Distillation/scorer training split | by session id (filler sessions are shared across questions: 3,942 of 19,195 unique sessions, max reuse 6) |
| Judge guard | cut sweep points rather than switch judge model |
| Generalization (LoCoMo/BEAM) | optional, exploratory only |
| Fit Over Depth results | read-only, not modified |
