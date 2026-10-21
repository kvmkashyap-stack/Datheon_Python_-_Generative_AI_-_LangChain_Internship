import pytest
from tools.file_reader import DATA_DIR, read_file

def test_reads_text_file(tmp_path, monkeypatch):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("NexusAI reads user documents.", encoding="utf-8")

    monkeypatch.setattr("tools.file_reader.DATA_DIR", tmp_path)

    content = read_file("sample.txt")

    assert content == "NexusAI reads user documents."

def test_rejects_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.file_reader.DATA_DIR", tmp_path)

    with pytest.raises(FileNotFoundError):
        read_file("missing.txt")


def test_blocks_path_traversal():
    with pytest.raises(ValueError):
        read_file("../requirements.txt")


def test_rejects_unsupported_extension(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.file_reader.DATA_DIR", tmp_path)

    with pytest.raises(ValueError):
        read_file("sample.exe")


def test_rejects_empty_filename():
    with pytest.raises(ValueError):
        read_file("   ")
