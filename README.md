# News Summarizer and Bias Detector

A small Python app that fetches news articles, summarizes them, and estimates political bias using pretrained Hugging Face models. The project includes a Streamlit UI and a simple CLI.

## Features

- Fetch news from NewsAPI by topic and language
- Generate concise summaries with a transformer model
- Classify summaries for bias with a pretrained classifier
- Streamlit UI for interactive use
- CLI for quick terminal runs

## Tech Stack

- Python 3.10+
- Streamlit
- Transformers + Torch
- NewsAPI

## Project Structure

```
app/
  streamlit_app.py
scripts/
  main.py
src/
  nbdet/
    __init__.py
    data_ingest.py
    summarizer.py
    bias_model.py
```

## Setup

1) Create a virtual environment (recommended)

```
python -m venv .venv
.\.venv\Scripts\activate
```

2) Install dependencies

```
pip install -r requirements.txt
```

If you prefer using the pyproject, you can also install with:

```
pip install -e .
```

3) Add your NewsAPI key

Create a .env file in the project root:

```
NEWSAPI_KEY=your_api_key_here
```

You can get an API key at https://newsapi.org/

## Usage

### Streamlit app

```
streamlit run app/streamlit_app.py
```

Open the app in your browser, enter a topic and language, then click "Fetch News".

### CLI

```
python scripts/main.py --query "climate change" --language en --page-size 5
```

## Models

- Summarization: facebook/bart-large-cnn
- Bias classification: newsmediabias/UnBIAS-classifier

The first run will download model weights, which can take time depending on your connection.

## Notes and Limitations

- This project depends on NewsAPI, which has rate limits and usage policies.
- Bias detection is a best-effort classification and should not be treated as ground truth.
- Long articles are truncated by the models.

## Troubleshooting

- Missing API key: make sure NEWSAPI_KEY is set in .env or in your environment.
- Model download issues: check your network and that you can access Hugging Face.
- Slow inference: the models are large; CPU inference can be slow.

## License

Add a license if you plan to open-source this project.

## Acknowledgements

- NewsAPI for article data
- Hugging Face for pretrained models
