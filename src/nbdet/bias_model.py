from __future__ import annotations

from functools import lru_cache
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = "newsmediabias/UnBIAS-classifier"

@lru_cache(maxsize=1)
def _get_classifier():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
        truncation=True,
    )

LABEL_MAP = {
    "LABEL_0": "Highly Biased",
    "LABEL_1": "Slightly Biased",
    "LABEL_2": "Neutral",
}

def detect_bias(text: str, max_len: int = 512):
    if not text:
        return "Unknown", 0.0
    classifier = _get_classifier()
    result = classifier(text[:max_len])[0]
    friendly = LABEL_MAP.get(result["label"], result["label"])
    return friendly, round(result["score"], 3)