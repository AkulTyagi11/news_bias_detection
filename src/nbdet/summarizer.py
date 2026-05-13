from __future__ import annotations

from functools import lru_cache
from transformers import pipeline

MODEL_NAME = "facebook/bart-large-cnn"

@lru_cache(maxsize=1)
def _get_summarizer():
    return pipeline("summarization", model=MODEL_NAME)

def summarize(text: str, max_len: int = 150, min_len: int = 30):
    if not text or len(text.split()) < min_len:
        return "Text is too short to summarize."
    summarizer = _get_summarizer()
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False, truncation=True)
    return summary[0]["summary_text"]
