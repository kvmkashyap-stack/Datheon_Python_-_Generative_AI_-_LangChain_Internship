from pathlib import Path
from pypdf import PdfReader

DATA_DIR = (Path(__file__).resolve().parent.parent / "data").resolve()
ALLOWED_EXTENSIONS = {".pdf", ".txt", ".md", ".csv", ".json"}
MAX_FILE_SIZE = 1_000_000


def read_file(filename: str) -> str:
    """Read a supported document from NexusAI's data directory."""
    if not filename or not filename.strip():
        raise ValueError("Filename cannot be empty.")

    # Only accept a filename, not a user-supplied path.
    if Path(filename).name != filename or filename in {".", ".."}:
        raise ValueError("Provide a filename inside the data directory.")

    file_path = (DATA_DIR / filename).resolve()

    if not file_path.is_relative_to(DATA_DIR):
        raise ValueError("Access denied: file must be inside the data directory.")

    if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported file type.")

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {filename}")

    if file_path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("File is too large. Maximum size is 1 MB.")

    if file_path.suffix.lower() == ".pdf":
        reader = PdfReader(str(file_path))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)

        if not text.strip():
            raise ValueError(
                "No extractable text found. Scanned PDFs may require OCR."
            )

        return text

    return file_path.read_text(encoding="utf-8")
