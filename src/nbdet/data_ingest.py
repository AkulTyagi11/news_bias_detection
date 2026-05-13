from __future__ import annotations

from pathlib import Path
import os
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

API_URL = "https://newsapi.org/v2/everything"

def fetch_news(query: str = "technology", language: str = "en", page_size: int = 10, api_key: str | None = None):
    api_key = api_key or os.getenv("NEWSAPI_KEY")
    if not api_key:
        raise ValueError("Missing NEWSAPI_KEY. Add it to a .env file in the project root or set it as an environment variable.")

    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    try:
        response = requests.get(API_URL, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"News API request failed: {exc}") from exc

    if data.get("status") == "ok":
        return data.get("articles", [])

    raise RuntimeError(f"News API error: {data.get('message', 'Unknown error')}")
