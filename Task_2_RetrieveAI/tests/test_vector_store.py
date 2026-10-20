import pytest
from langchain_core.documents import Document

from retrieval import vector_store


def test_empty_documents_rejected():
    with pytest.raises(ValueError, match="no documents"):
        vector_store.create_vector_store([])


def test_missing_api_key_rejected(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    with pytest.raises(EnvironmentError, match="GEMINI_API_KEY"):
        vector_store.create_vector_store(
            [Document(page_content="Example", metadata={"source": "sample.txt"})]
        )


def test_reindex_replaces_only_matching_source(monkeypatch, tmp_path):
    class FakeEmbeddings:
        def __init__(self, **kwargs):
            pass

    class FakeChroma:
        collections = {}

        def __init__(self, collection_name, embedding_function, persist_directory):
            self.collection = self.collections.setdefault(collection_name, {})

        def get(self, where=None):
            items = self.collection
            if where:
                key, value = next(iter(where.items()))
                items = {
                    item_id: item
                    for item_id, item in items.items()
                    if item["metadata"].get(key) == value
                }

            return {
                "ids": list(items),
                "metadatas": [item["metadata"] for item in items.values()],
            }

        def delete(self, ids):
            for item_id in ids:
                self.collection.pop(item_id, None)

        def add_documents(self, documents, ids):
            for document, item_id in zip(documents, ids):
                self.collection[item_id] = {
                    "metadata": dict(document.metadata),
                    "content": document.page_content,
                }

    FakeChroma.collections = {}

    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    monkeypatch.setattr(
        vector_store, "GoogleGenerativeAIEmbeddings", FakeEmbeddings
    )
    monkeypatch.setattr(vector_store, "Chroma", FakeChroma)

    path_a = tmp_path / "a.txt"
    path_b = tmp_path / "b.txt"

    vector_store.create_vector_store(
        [Document(page_content="Document A version 1", metadata={"source": "a.txt"})],
        persist_directory=str(tmp_path / "db"),
        source_path=str(path_a),
    )
    vector_store.create_vector_store(
        [Document(page_content="Document B", metadata={"source": "b.txt"})],
        persist_directory=str(tmp_path / "db"),
        source_path=str(path_b),
    )
    vector_store.create_vector_store(
        [Document(page_content="Document A version 2", metadata={"source": "a.txt"})],
        persist_directory=str(tmp_path / "db"),
        source_path=str(path_a),
    )

    stored = list(FakeChroma.collections["rag_documents"].values())
    contents = {item["content"] for item in stored}

    assert "Document A version 1" not in contents
    assert "Document A version 2" in contents
    assert "Document B" in contents
    assert len(stored) == 2
