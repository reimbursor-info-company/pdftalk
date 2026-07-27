"""Native text extraction from PDF files."""

from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


class PdfTextExtractionError(Exception):
    """Raised when text cannot be extracted from a PDF."""


def extract_text(pdf_path: str | Path) -> str:
    """Extract the native text from a PDF, page by page.

    Raises PdfTextExtractionError if the file does not exist, is corrupted,
    or contains no extractable text (e.g. a scanned PDF without OCR).
    """
    path = Path(pdf_path)
    if not path.is_file():
        raise PdfTextExtractionError(f"File does not exist: {path}")

    try:
        reader = PdfReader(str(path))
    except PdfReadError as exc:
        raise PdfTextExtractionError(f"Could not read the PDF: {exc}") from exc

    pages_text = [page.extract_text() or "" for page in reader.pages]
    full_text = "\n".join(pages_text).strip()

    if not full_text:
        raise PdfTextExtractionError(
            "No extractable text was found in the PDF. "
            "It may be a scanned document (image) without OCR."
        )

    return full_text
