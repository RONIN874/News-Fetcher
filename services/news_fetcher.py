"""
News Fetcher — Retrieves news articles.
Phase A: Returns hardcoded sample articles.
Phase B: Fetches live articles from NewsAPI.
"""

import requests
from config import NEWSAPI_KEY, MAX_ARTICLES, ARTICLE_MAX_CHARS
from data.sample_articles import SAMPLE_ARTICLES


def fetch_articles(topic: str, use_api: bool = False) -> list[dict]:
    if use_api and NEWSAPI_KEY:
        return _fetch_from_api(topic)
    return _fetch_samples(topic)


def _fetch_samples(topic: str) -> list[dict]:
    print("  📂 Using sample articles (Phase A)")

    topic_lower = topic.lower()

    filtered = [
        a for a in SAMPLE_ARTICLES
        if topic_lower in a["title"].lower()
        or topic_lower in a["content"].lower()
    ]

    if not filtered:
        filtered = SAMPLE_ARTICLES

    return filtered[:MAX_ARTICLES]


def _fetch_from_api(topic: str) -> list[dict]:
    """Phase B: Fetch articles from NewsAPI."""
    print(f"  🌐 Fetching from NewsAPI: '{topic}'")

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": MAX_ARTICLES,
        "apiKey": NEWSAPI_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        articles = []
        for item in data.get("articles", [])[:MAX_ARTICLES]:
            content = item.get("content") or item.get("description") or ""
            articles.append({
                "title": item.get("title", "Untitled"),
                "source": item.get("source", {}).get("name", "Unknown"),
                "content": content[:ARTICLE_MAX_CHARS],
            })

        print(f"  ✅ Got {len(articles)} articles")
        return articles

    except requests.RequestException as e:
        print(f"  ❌ API failed: {e}")
        print("  📂 Falling back to sample articles")
        return _fetch_samples()
