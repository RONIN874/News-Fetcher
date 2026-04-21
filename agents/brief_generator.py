"""
Brief Generator — Combines summaries into a morning brief + "Why It Matters".
Two simple functions, two LLM calls.
"""

from services.llm_service import call_llm
from utils.prompts import morning_brief_prompt, why_it_matters_prompt


def generate_brief(summaries: list[dict], topic: str) -> str:
    """
    Combine article summaries into a cohesive morning brief.

    Args:
        summaries: List of dicts with 'summary' key.
        topic: The news topic.

    Returns:
        Morning brief as a string.
    """
    print("  🔗 Creating morning brief...")

    # Format summaries for the prompt
    summaries_text = "\n\n".join(
        f"• {s['title']}: {s['summary']}" for s in summaries
    )

    prompt = morning_brief_prompt(summaries_text, topic)
    brief = call_llm(prompt, temperature=0.5)
    return brief


def generate_why_it_matters(brief: str, topic: str) -> str:
    """
    Generate a 'Why It Matters' section based on the brief.

    Args:
        brief: The morning brief text.
        topic: The news topic.

    Returns:
        "Why It Matters" text as a string.
    """
    print("  🧠 Generating 'Why It Matters'...")

    prompt = why_it_matters_prompt(brief, topic)
    why = call_llm(prompt, temperature=0.6)
    return why
