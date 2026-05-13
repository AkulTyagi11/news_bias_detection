from __future__ import annotations

import argparse
import sys
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

load_dotenv(ROOT / ".env")

from nbdet.data_ingest import fetch_news
from nbdet.summarizer import summarize
from nbdet.bias_model import detect_bias

def parse_args():
    parser = argparse.ArgumentParser(description="News summarizer and bias detection")
    parser.add_argument("--query", default="technology", help="Search topic")
    parser.add_argument("--language", default="en", help="Language code")
    parser.add_argument("--page-size", type=int, default=5, help="Number of articles")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    try:
        articles = fetch_news(args.query, args.language, args.page_size)
    except Exception as exc:
        raise SystemExit(str(exc))

    if not articles:
        print("No articles found.")
        raise SystemExit(0)

    for article in articles:
        title = article.get("title") or "Untitled"
        text = article.get("content") or article.get("description") or ""
        summary = summarize(text)
        label, score = detect_bias(summary)
        print(f"\n📰 {title}")
        print("Summary:", summary)
        print(f"Bias: {label} (Confidence: {round(score * 100, 2)}%)")
        print("-" * 60)
