"""
Prompt Manager — All prompt templates in one place.
Easy to edit and iterate without touching any logic.
"""


def summarize_all_prompt(articles_text: str) -> str:
    """Prompt to summarize multiple articles at once and return JSON."""
    return f"""You are a news analyst. Below is a list of news articles. 
Summarize EACH article in exactly 2-3 concise sentences. Focus on key facts.

Return your response ONLY as a valid JSON array of objects, with no markdown formatting.
Each object must have exactly these keys: "title", "source", "summary".

Articles:
{articles_text}"""


def morning_brief_prompt(summaries_text: str, topic: str) -> str:
    """Prompt to combine summaries into a clean morning brief."""
    return f"""You are a news editor creating a morning brief about "{topic}".

Below are summaries of today's top stories:

{summaries_text}

Write a short, engaging morning brief (4-6 sentences) that ties these stories together.
Write it as a cohesive paragraph, not as a list. Make it sound like a professional news anchor.

Morning Brief:"""


def why_it_matters_prompt(brief_text: str, topic: str) -> str:
    """Prompt to generate a 'Why It Matters' section."""
    return f"""Based on this morning news brief about "{topic}":

{brief_text}

Write a "Why It Matters" section in exactly 2-3 sentences.
Explain why an average reader should care about these developments.
Focus on real-world impact — jobs, daily life, future implications.

Why It Matters:"""
