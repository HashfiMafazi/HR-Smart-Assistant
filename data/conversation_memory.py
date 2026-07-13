import json
import os

MEMORY_FILE = "memory/conversation_log.json"

def load_memory():
    """Load previous conversations from disk."""
    if not os.path.exists("memory"):
        os.makedirs("memory")
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_memory(conversation_history):
    """Save all conversations to disk."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(conversation_history, f, indent=2, ensure_ascii=False)
