"""
Summarizer Agent — Summarizes individual news articles.
Takes one article → returns a 2-3 line summary via the LLM.
"""

import json
from services.llm_service import call_llm
from utils.prompts import summarize_all_prompt

def summarize_all(articles: list[dict]) -> list[dict]:
    """
    Summarize a list of articles using a single LLM API call.

    Returns:
        List of dicts with title, source, summary.
    """
    print(f"  📝 Summarizing {len(articles)} articles in a single batch...")
    
    # Combine all articles into a single prompt string
    articles_text = ""
    for i, article in enumerate(articles, 1):
        title = article.get("title", "Untitled")
        source = article.get("source", "Unknown")
        content = article.get("content", "")
        # Truncation limits were already handled in news_fetcher
        articles_text += f"---\nArticle {i}:\nTitle: {title}\nSource: {source}\nContent: {content}\n"
    
    prompt = summarize_all_prompt(articles_text)
    
    # Make 1 LLM call instead of N calls
    response_text = call_llm(prompt, temperature=0.3)
    
    # Clean up JSON (Gemini sometimes returns markdown block '```json...```')
    clean_json = response_text.replace("```json", "").replace("```", "").strip()
    
    try:
        results = json.loads(clean_json)
        return results
    except json.JSONDecodeError as e:
        print(f"  ❌ Failed to parse JSON from LLM: {e}\nRaw output was: {response_text}")
        return []
