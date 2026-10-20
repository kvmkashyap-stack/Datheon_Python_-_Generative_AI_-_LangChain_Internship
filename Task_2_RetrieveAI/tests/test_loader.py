import pytest

from ingestion.loader import load_document


def test_load_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("RAG stands for Retrieval-Augmented Generation.", encoding="utf-8")

    documents = load_document(str(file_path))

    assert len(documents) == 1
    assert "Retrieval-Augmented Generation" in documents[0].page_content
    assert documents[0].metadata["source"] == "sample.txt"


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_document("missing_file.txt")


def test_unsupported_file_type(tmp_path):
    file_path = tmp_path / "sample.docx"
    file_path.write_text("Unsupported", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported file type"):
        load_document(str(file_path))
