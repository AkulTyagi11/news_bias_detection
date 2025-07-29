import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news(query="technology", language="en", page_size=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] == "ok":
        return data["articles"]
    else:
        raise Exception(f"News API Error: {data.get('message')}")
