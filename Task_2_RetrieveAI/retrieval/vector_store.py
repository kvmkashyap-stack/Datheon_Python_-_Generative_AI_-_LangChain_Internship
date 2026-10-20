import hashlib
import os
from pathlib import Path

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document


DB_DIRECTORY = "chroma_db"
COLLECTION_NAME = "rag_documents"


def _get_source_id(source_path: str) -> str:
    """Create a stable ID for the original document path."""
    resolved_path = str(Path(source_path).resolve())
    return hashlib.sha256(resolved_path.encode("utf-8")).hexdigest()


def create_vector_store(
    documents: list[Document],
    persist_directory: str = DB_DIRECTORY,
    source_path: str | None = None,
) -> Chroma:
    """Index a document, replacing only its previously indexed chunks."""
    if not documents:
        raise ValueError("Cannot create a vector store with no documents.")

    if not os.getenv("GEMINI_API_KEY"):
        raise EnvironmentError(
            "GEMINI_API_KEY is missing. Add it to your .env file."
        )

    original_path = source_path or documents[0].metadata.get("source", "unknown")
    source_id = _get_source_id(original_path)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(Path(persist_directory)),
    )

    # Remove legacy chunks that predate source-specific IDs.
    existing = vector_store.get()
    existing_ids = existing.get("ids", [])
    existing_metadata = existing.get("metadatas", [])

    legacy_ids = [
        chunk_id
        for chunk_id, metadata in zip(existing_ids, existing_metadata)
        if not metadata or "source_id" not in metadata
    ]

    if legacy_ids:
        vector_store.delete(ids=legacy_ids)

    # Replace chunks belonging only to this document.
    previous = vector_store.get(where={"source_id": source_id})
    previous_ids = previous.get("ids", [])

    if previous_ids:
        vector_store.delete(ids=previous_ids)

    chunk_ids = []

    for index, document in enumerate(documents):
        document.metadata["source_id"] = source_id

        unique_value = (
            f"{source_id}:{index}:{document.page_content}"
        )
        chunk_ids.append(
            hashlib.sha256(unique_value.encode("utf-8")).hexdigest()
        )

    vector_store.add_documents(documents, ids=chunk_ids)

    return vector_store


def load_vector_store(
    persist_directory: str = DB_DIRECTORY,
) -> Chroma:
    """Reconnect to the existing persisted ChromaDB collection."""
    if not os.getenv("GEMINI_API_KEY"):
        raise EnvironmentError(
            "GEMINI_API_KEY is missing. Add it to your .env file."
        )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(Path(persist_directory)),
    )

