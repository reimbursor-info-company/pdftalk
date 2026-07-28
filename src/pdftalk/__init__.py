from .extractor import extract_text, PdfTextExtractionError
from .converter import pdf_to_audio, text_to_audio

__all__ = [
    "extract_text",
    "pdf_to_audio",
    "text_to_audio",
    "PdfTextExtractionError",
]

__version__ = "0.2.3"
