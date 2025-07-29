from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize (text, max_len=150):
    if not text or len(text.split()) < 30:
        return "Text is too short to summarize."
    summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']
