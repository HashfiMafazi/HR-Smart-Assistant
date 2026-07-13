"""
Handles the Ollama language model.

Responsibilities:
- Load the LLM only once
- Warm up the model
- Generate responses
"""

from langchain_community.llms import Ollama

from src.config import LLM_MODEL

# Lazy-loaded LLM
_llm = None


def get_llm():
    """
    Load the Ollama model only once.
    """

    global _llm

    if _llm is None:
        print(f"🤖 Loading Ollama model ({LLM_MODEL})...")

        _llm = Ollama(model=LLM_MODEL)

        # Warm-up
        try:
            _llm.invoke("Hello")
        except Exception:
            pass

        print("✅ Ollama model is ready!")

    return _llm


def generate(prompt: str) -> str:
    """
    Send a prompt to the language model.

    Args:
        prompt: Complete prompt text.

    Returns:
        Model response.
    """

    llm = get_llm()

    return llm.invoke(prompt)
