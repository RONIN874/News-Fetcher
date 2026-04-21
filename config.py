"""
Configuration — Loads API keys and project settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# --- API Keys ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")

# --- LLM Settings ---
GROQ_MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0.7
MAX_TOKENS = 1024

# --- News Settings ---
MAX_ARTICLES = 2
ARTICLE_MAX_CHARS = 3000


def validate_config():
    """Ensure required keys are set before running."""
    if not GROQ_API_KEY:
        raise ValueError(
            "❌ GROQ_API_KEY not found!\n"
            "   Add it to your .env file.\n"
            "   Get a free key at: https://console.groq.com/keys"
        )
