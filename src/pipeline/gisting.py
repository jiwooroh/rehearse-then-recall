"""Sentence splitting, ported from fit-over-depth's gisting.py. Only
split_into_sentences survives the port — the rest of that module
(embed_chunks, score_chunk_sentences) is document-chunk-specific and has no
equivalent here, since a conversation turn is already the natural unit;
there's no chunking problem to solve.
"""

from __future__ import annotations

from nltk.tokenize import sent_tokenize


def split_into_sentences(text: str) -> list[str]:
    sentences = sent_tokenize(text)
    return sentences if sentences else [text]
