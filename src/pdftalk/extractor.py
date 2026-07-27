"""Extraccion de texto nativo desde archivos PDF."""

from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


class PdfTextExtractionError(Exception):
    """Se lanza cuando no se puede extraer texto de un PDF."""


def extract_text(pdf_path: str | Path) -> str:
    """Extrae el texto nativo de un PDF, pagina por pagina.

    Lanza PdfTextExtractionError si el archivo no existe, esta corrupto,
    o no contiene texto extraible (por ejemplo, un PDF escaneado sin OCR).
    """
    path = Path(pdf_path)
    if not path.is_file():
        raise PdfTextExtractionError(f"El archivo no existe: {path}")

    try:
        reader = PdfReader(str(path))
    except PdfReadError as exc:
        raise PdfTextExtractionError(f"No se pudo leer el PDF: {exc}") from exc

    pages_text = [page.extract_text() or "" for page in reader.pages]
    full_text = "\n".join(pages_text).strip()

    if not full_text:
        raise PdfTextExtractionError(
            "No se encontro texto extraible en el PDF. "
            "Puede ser un documento escaneado (imagen) sin OCR."
        )

    return full_text
