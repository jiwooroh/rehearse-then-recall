# Rehearse Then Recall

Does a memory mechanism grounded in human rehearsal theory (Craik & Watkins, 1973) improve an LLM's
long-term memory across multi-session conversations?

## Origin

This project forks its core mechanism — not its codebase — from
[`fit-over-depth`](../fit-over-depth) ("Fit Over Depth"), which applied the same rehearsal-theory
lineage (maintenance vs. elaborative rehearsal, C-DIC's thread-memory retrieval) to long *document*
compression. That project's own repo used to be called `rehearse-then-recall` before it renamed itself
to `fit-over-depth` once it settled on document compression as its focus — this project reclaims that
name for its original, closer fit: rehearsal (the mechanism) → recall (what
[LongMemEval](https://arxiv.org/abs/2410.10813) actually measures).

The elaborative-rehearsal / `ThreadMemory` mechanism (`src/pipeline/thread_memory.py`,
`src/pipeline/embeddings.py`) is C-DIC (Jung et al., ICML 2026, arXiv:2606.12411) transposed from
latent slots to text slots — built for dialogue turns, then transposed onto document chunks in
`fit-over-depth`, where it collapsed under generative rewriting (see that project's
`ANALYSIS_REPORT.md` §4.3.3). This project tests it in the domain it was actually designed for.

## Research question

Is `ThreadMemory`'s collapse under generative rewriting a property of the *mechanism*, or an artifact
of the *document-chunk transposition*? Testing natively on multi-session chat — where C-DIC's own
retrieve/revise/write-back loop is the native operation, not an adaptation — should tell them apart.

## Status

Scaffolding only (2026-09-18) — no experiments run yet. Ported: `thread_memory.py`, `embeddings.py`,
`notebook_setup.py`, a trimmed `gisting.py` (just `split_into_sentences` — no document-chunking
dependency needed here). Not yet built: LongMemEval data loading, the QA harness, baseline conditions
(closed-book / full-history / recency-window / `ThreadMemory`).

## Setup

```
pip install -r requirements.txt
cp .env.example .env   # fill in NVIDIA_NIM_API_KEY
```

## Data

[LongMemEval](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) (Wu et al., ICLR 2025,
MIT license) — 500 questions embedded in timestamped, session-structured chat histories. Fields per
question: `question_type` (single-session / multi-session / temporal-reasoning / knowledge-update /
abstention), `haystack_sessions` (turns as `{role, content}`, evidence turns marked `has_answer: true`).
Not yet downloaded into `data/`.
