import pytest
from langchain_core.documents import Document

from ingestion.chunker import split_documents


def test_split_documents_preserves_metadata():
    document = Document(
        page_content="A " * 100,
        metadata={"source": "sample.txt"},
    )

    chunks = split_documents([document], chunk_size=50, chunk_overlap=10)

    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 50 for chunk in chunks)
    assert all(chunk.metadata["source"] == "sample.txt" for chunk in chunks)


def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        split_documents([Document(page_content="Example")], chunk_size=0)


def test_invalid_chunk_overlap():
    with pytest.raises(ValueError):
        split_documents([Document(page_content="Example")], chunk_size=10, chunk_overlap=10)
