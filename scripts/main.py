from dotenv import load_dotenv
import os
from nbdet.data_ingest import fetch_news
from nbdet.summarizer import summarize
from nbdet.bias_model import detect_bias

load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")

if __name__ == "__main__":
    articles = fetch_news("")

    for article in articles:
        text = article.get("content") or article.get("description") or ""
        summary = summarize(text)
        label, score = detect_bias(summary)
        print(f"\n📰 {article['title']}")
        print("Summary:", summary)
        print(f"Bias: {label} (Confidence: {round(score*100, 2)}%)")
        print("—" * 60)
