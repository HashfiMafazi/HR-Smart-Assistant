"""
Conversation Memory
"""

import json
import os

from src.config import MEMORY_FILE, MAX_MEMORY


def load_memory():
    """
    Load conversation history safely.
    """

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:

        print("⚠ Memory file is corrupted.")

        return []

    except Exception as e:

        print(f"⚠ Failed to load memory: {e}")

        return []


def save_memory(history):
    """
    Save conversation history.
    """

    history = history[-MAX_MEMORY:]

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False,
        )


def add_memory(history, question, answer):
    """
    Add one conversation.
    """

    history.append(
        {
            "question": question,
            "answer": answer,
        }
    )

    return history[-MAX_MEMORY:]


def format_memory(history, limit=3):
    """
    Convert memory into prompt text.
    """

    if not history:
        return "No previous conversation."

    history = history[-limit:]

    formatted = []

    for item in history:

        formatted.append(
            f"User: {item['question']}"
        )

        formatted.append(
            f"Assistant: {item['answer']}"
        )

    return "\n".join(formatted)
