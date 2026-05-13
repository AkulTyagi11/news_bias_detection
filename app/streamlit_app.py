import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import streamlit as st
from nbdet.data_ingest import fetch_news
from nbdet.summarizer import summarize
from nbdet.bias_model import detect_bias

st.set_page_config(page_title="News Summarizer & Bias Detector", page_icon="📰", layout="wide")
st.title("News Summarizer & Bias Detector")

st.info("Add a NEWSAPI_KEY to a .env file in the project root or set it as an environment variable.")

col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    query = st.text_input("Topic", "climate change")
with col2:
    language = st.text_input("Language", "en")
with col3:
    page_size = st.number_input("Articles", min_value=1, max_value=20, value=5, step=1)

@st.cache_data(show_spinner=False, ttl=300)
def _fetch_cached(q: str, lang: str, size: int):
    return fetch_news(q, lang, size)

if st.button("Fetch News"):
    with st.spinner("Fetching articles..."):
        try:
            articles = _fetch_cached(query, language, int(page_size))
        except Exception as exc:
            st.error(str(exc))
            st.stop()

    if not articles:
        st.warning("No articles found. Try a different topic.")
    for article in articles:
        title = article.get("title") or "Untitled"
        source = (article.get("source") or {}).get("name") or "Unknown source"
        text = article.get("content") or article.get("description") or ""
        summary = summarize(text)
        bias, score = detect_bias(summary)

        st.subheader(title)
        st.caption(source)
        st.markdown(f"**Summary:** {summary}")
        st.markdown(f"**Bias:** {bias} ({round(score * 100, 2)}%)")
        st.markdown("---")