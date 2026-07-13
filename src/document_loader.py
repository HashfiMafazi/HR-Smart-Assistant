"""
Document Loader

Responsibilities:
- Find PDF documents
- Load PDF documents
- Split into chunks
"""

import os

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DOCUMENTS_PATH


def find_pdf_files():
    """
    Return all PDF files inside the documents folder.
    """

    if not os.path.exists(DOCUMENTS_PATH):
        raise FileNotFoundError(
            f"Documents folder not found: {DOCUMENTS_PATH}"
        )

    pdf_files = []

    for filename in os.listdir(DOCUMENTS_PATH):

        if filename.lower().endswith(".pdf"):

            pdf_files.append(
                os.path.join(DOCUMENTS_PATH, filename)
            )

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF documents were found."
        )

    return sorted(pdf_files)


def load_documents():
    """
    Load every PDF document.
    """

    documents = []

    pdf_files = find_pdf_files()

    print(f"📚 Found {len(pdf_files)} PDF document(s).")

    for pdf in pdf_files:

        print(f"📄 Loading {os.path.basename(pdf)}")

        loader = PyMuPDFLoader(pdf)

        docs = loader.load()

        documents.extend(docs)

    print(f"✅ Loaded {len(documents)} pages.")

    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    print(f"✂️ Created {len(chunks)} chunks.")

    return chunks


def load_chunks():
    """
    Complete loading pipeline.
    """

    documents = load_documents()

    chunks = split_documents(documents)

    return chunks
