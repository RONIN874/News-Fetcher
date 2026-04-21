"""
AI Morning News Brief — Main Pipeline
Orchestrates the full workflow: fetch → summarize → brief → format.

Usage:
    python main.py                          # Interactive (asks for topic)
    python main.py "AI in healthcare"       # Direct with topic
    python main.py --api "climate change"   # Use live NewsAPI
"""

import sys

# Force UTF-8 output for emojis on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from config import validate_config
from services.news_fetcher import fetch_articles
from agents.summarizer import summarize_all
from agents.brief_generator import generate_brief, generate_why_it_matters
from utils.formatter import format_output


def run(topic: str, use_api: bool = False) -> None:
    """Run the full morning brief pipeline."""

    print(f"\n{'='*50}")
    print(f"  🗞️  AI MORNING NEWS BRIEF")
    print(f"  Topic: {topic}")
    print(f"  Mode: {'Live API' if use_api else 'Sample Articles'}")
    print(f"{'='*50}\n")

    # Step 1: Fetch articles
    print("📰 Step 1: Fetching articles...")
    articles = fetch_articles(topic, use_api=use_api)
    if not articles:
        print("❌ No articles found. Exiting.")
        return
    print(f"   → {len(articles)} articles found\n")

    # Step 2: Summarize each article
    print("📝 Step 2: Summarizing articles...")
    summaries = summarize_all(articles)
    print(f"   → {len(summaries)} summaries ready\n")

    # Step 3: Generate morning brief
    print("📰 Step 3: Creating morning brief...")
    brief = generate_brief(summaries, topic)
    print("   → Brief ready\n")

    # Step 4: Generate "Why It Matters"
    print("🧠 Step 4: Generating 'Why It Matters'...")
    why = generate_why_it_matters(brief, topic)
    print("   → Done\n")

    # Step 5: Format and display
    print("🎨 Step 5: Rendering output...\n")
    format_output(
        topic=topic,
        summaries=summaries,
        brief=brief,
        why_it_matters=why,
    )

    print("✅ Pipeline complete!\n")


def main():
    """Entry point — handles CLI arguments."""
    validate_config()

    use_api = "--api" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--api"]

    if args:
        topic = " ".join(args)
    else:
        topic = input("🎯 Enter a news topic: ").strip()
        if not topic:
            print("❌ No topic provided. Exiting.")
            return

    run(topic, use_api=use_api)


if __name__ == "__main__":
    main()
