"""
Application configuration.

This file stores all configurable settings in one place.
If you ever want to change models or file locations,
you only need to edit this file.
"""

# ==========================
# Documents
# ==========================

PDF_PATH = "documents/employee_policy.pdf"

# ==========================
# Vector Database
# ==========================

FAISS_PATH = "faiss_index"

# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================
# Ollama
# ==========================

LLM_MODEL = "llama3"

# ==========================
# Text Splitter
# ==========================

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 100

# ==========================
# Retriever
# ==========================

TOP_K = 2

# ==========================
# Conversation Memory
# ==========================

MEMORY_FILE = "conversation_history.json"

SIMILARITY_THRESHOLD = 5.0

DOCUMENTS_PATH = "documents"

VECTORSTORE_PATH = "faiss_index"

MEMORY_FILE = "data/conversation_history.json"

MAX_MEMORY = 20
