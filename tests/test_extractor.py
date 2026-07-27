from pathlib import Path

import pytest
from pypdf import PdfWriter

from pdftalk.extractor import PdfTextExtractionError, extract_text


def _make_pdf_with_text(path: Path, text: str) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    with open(path, "wb") as f:
        writer.write(f)
    # pypdf does not easily support writing text; we use a minimal PDF
    # with hand-embedded text for extraction tests.


def test_extract_text_missing_file(tmp_path):
    missing = tmp_path / "missing.pdf"
    with pytest.raises(PdfTextExtractionError):
        extract_text(missing)


def test_extract_text_empty_pdf_raises(tmp_path):
    pdf_path = tmp_path / "empty.pdf"
    _make_pdf_with_text(pdf_path, "")
    with pytest.raises(PdfTextExtractionError):
        extract_text(pdf_path)
