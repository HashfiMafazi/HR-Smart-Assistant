"""
FAISS Vector Store

Responsibilities
----------------
- Build FAISS index
- Load FAISS lazily
- Retrieve relevant document context
"""

import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from src.config import (
    VECTORSTORE_PATH,
    TOP_K,
)

# =====================================================
# Global Cache
# =====================================================

_embedding = None
_vectordb = None


# =====================================================
# Embedding
# =====================================================

def get_embedding():
    """
    Load embedding model only once.

    Offline mode:
    The model must already exist inside the HuggingFace cache.
    """

    global _embedding

    if _embedding is None:

        print("🧠 Loading embedding model...")

        _embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={
                "local_files_only": True,
            },
        )

    return _embedding


# =====================================================
# Build Vector Store
# =====================================================

def build_vectorstore(chunks):
    """
    Build FAISS index only once.
    """

    index_file = os.path.join(
        VECTORSTORE_PATH,
        "index.faiss",
    )

    if os.path.exists(index_file):

        print("✅ Existing FAISS index found.")

        return

    print("⚙️ Building FAISS index...")

    vectordb = FAISS.from_documents(
        chunks,
        get_embedding(),
    )

    os.makedirs(
        VECTORSTORE_PATH,
        exist_ok=True,
    )

    vectordb.save_local(
        VECTORSTORE_PATH,
    )

    print("💾 FAISS index created.")


# =====================================================
# Load Vector Store
# =====================================================

def get_vectorstore():
    """
    Lazy load FAISS database.
    """

    global _vectordb

    if _vectordb is not None:
        return _vectordb

    print("📂 Loading FAISS index...")

    _vectordb = FAISS.load_local(
        VECTORSTORE_PATH,
        get_embedding(),
        allow_dangerous_deserialization=True,
    )

    return _vectordb


# =====================================================
# Context Retrieval
# =====================================================

def get_context(question):
    """
    Retrieve document context.

    Returns
    -------
    context : str
    sources : list
    """

    vectordb = get_vectorstore()

    docs_with_scores = vectordb.similarity_search_with_score(
        question,
        k=TOP_K,
    )

    contexts = []
    sources = []

    for doc, score in docs_with_scores:

        contexts.append(doc.page_content)

        metadata = doc.metadata

        sources.append(
            {
                "page": metadata.get("page", 0),
                "source": os.path.basename(
                    metadata.get(
                        "source",
                        "Unknown",
                    )
                ),
                "score": float(score),
            }
        )

    context = "\n\n".join(contexts)

    return context, sources
