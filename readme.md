# 📰 News Fetcher

A simple Python-powered news summarizer that generates digestible news summaries and morning briefs based on a topic.

This project currently uses hardcoded sample articles (Phase A) for development and testing instead of fetching live news from an external API.

---

## 🚀 Features

- 📂 Phase A — Sample news support:
  Uses a predefined set of sample articles for topics during development.

- 🗞️ Topic-based summary generation:
  Generate a clean, readable summary and briefing based on a topic string.

- 🧠 Clear separation of sample data and API fetch logic to allow easy future upgrades.

---

## 🧩 Project Structure

📦 News-Fetcher
 ┣ 📂 data
 ┃ ┗ sample_articles.py       # Hardcoded sample news articles
 ┣ 📜 config.py               # API keys and configuration
 ┣ 📜 main.py                 # Main application logic
 ┣ 📜 news_fetcher.py         # Fetches articles (sample or live)
 ┗ 📜 summarizer.py           # Summarizes and generates briefs

---

## 📌 How It Works

1. User inputs a topic
2. fetch_articles() returns sample articles (Phase A)
3. summarizer builds a clean news summary & morning brief
4. Output is displayed to the user

Currently, the app uses sample articles defined in data/sample_articles.py.
You can later enable live news fetching by adding a valid NEWSAPI_KEY.

---

## 🛠️ Installation

Clone the repo:

git clone https://github.com/RONIN874/News-Fetcher.git
cd News-Fetcher

Install dependencies:

pip install -r requirements.txt

---

## 🧪 Usage Example

Run the main application:

python main.py

Enter a topic when prompted, e.g.:

Enter topic: climate change

You will then receive:
- A concise summary
- A morning brief based on the sample articles

---

## ⚙️ Configuration

Include your NewsAPI key in config.py if you want to enable Phase B (live API) later:

NEWSAPI_KEY = "YOUR_NEWSAPI_KEY"
MAX_ARTICLES = 5
ARTICLE_MAX_CHARS = 2000

---

## 🔍 Sample Articles (Phase A)

This project includes hardcoded sample articles under:

data/sample_articles.py

These articles are used when use_api=False or when the API key is not provided.

---

## 📦 Dependencies

- requests — HTTP client for live API support
- (optional) Rich — can be added to improve console UI

---

## 📝 Notes

This is a Phase A implementation — live API integration is optional and can be activated by providing a valid NEWSAPI_KEY.

Future improvements:
- Integrate real-time news API
- Add filtering & ranking of articles
- Add better summarization prompts

---
