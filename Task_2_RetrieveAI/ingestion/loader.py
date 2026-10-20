from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document


def load_document(file_path: str) -> list[Document]:
    """Load a PDF or text file into LangChain documents."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        documents = PyPDFLoader(str(path)).load()
    elif suffix == ".txt":
        documents = TextLoader(
            str(path),
            encoding="utf-8",
        ).load()
    else:
        raise ValueError(
            f"Unsupported file type: {suffix}. Use PDF or TXT."
        )

    # Keep the source filename for later citations.
    for document in documents:
        document.metadata["source"] = path.name

    return documents
