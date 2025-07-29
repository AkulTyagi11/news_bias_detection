import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

import streamlit as st
from nbdet.data_ingest import fetch_news
from nbdet.summarizer import summarize
from nbdet.bias_model import detect_bias

st.title("📰 News Summarizer & Bias Detector")

query = st.text_input("Enter topic", "climate change")
if st.button("Fetch News"):
    articles = fetch_news(query)
    for a in articles:
        st.subheader(a['title'])
        st.caption(a['source']['name'])
        summary = summarize(a['content'] or a['description'] or "")
        bias, score = detect_bias(summary)
        st.markdown(f"**Summary:** {summary}")
        st.markdown(f"**Bias:** {bias} ({round(score*100, 2)}%)")
        st.markdown("---")