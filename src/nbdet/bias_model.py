from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

_MODEL = "newsmediabias/UnBIAS-classifier"

tokenizer  = AutoTokenizer.from_pretrained(_MODEL)
model      = AutoModelForSequenceClassification.from_pretrained(_MODEL)

classifier = pipeline(
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
    result = classifier(text[:max_len])[0]
    friendly = LABEL_MAP.get(result["label"], result["label"])
    return friendly, round(result["score"], 3)