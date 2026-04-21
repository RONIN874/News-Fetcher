"""
LLM Service — Central wrapper for all AI calls via Groq.
Every LLM interaction in the project goes through call_llm().
"""

import time
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL, TEMPERATURE

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)


def call_llm(prompt: str, temperature: float = None, max_retries: int = 3) -> str:
    """
    Send a prompt to Groq API and return the response text.

    Args:
        prompt: The prompt string to send.
        temperature: Override default creativity level.
        max_retries: Retry attempts on failure.

    Returns:
        LLM response as a plain string.
    """
    temp = temperature if temperature is not None else TEMPERATURE

    last_error = None
    for attempt in range(1, max_retries + 1):
        try:
            print("    🤖 Calling Groq API...")
            time.sleep(1) # Delay to prevent rate limits
            
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=temp,
            )
            print("    ✅ Response received")
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            last_error = e
            if attempt < max_retries:
                # 1st retry -> 2 seconds, 2nd retry -> 4 seconds
                wait = 2 * attempt 
                print(f"    ⚠ Groq API failed: {e}")
                print(f"    🔄 Retrying in {wait}s...")
                time.sleep(wait)

    raise RuntimeError(f"Groq LLM failed after {max_retries} attempts: {last_error}")
