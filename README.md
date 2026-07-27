# pdftalk

Converts PDF files into audio files (text-to-speech), designed to help
visually impaired people access the content of a PDF.

- Native text extraction from the PDF (does not support scanned/image PDFs without OCR).
- **Offline** speech synthesis, using the voices installed on the operating system
  (via [`pyttsx3`](https://pypi.org/project/pyttsx3/)), with no internet connection
  or API keys required.

## Installation

From the repository (while not published on PyPI):

```bash
pip install git+https://github.com/reimbursor-info-company/pdftalk.git
```

For local development:

```bash
git clone https://github.com/reimbursor-info-company/pdftalk.git
cd pdftalk
pip install -e ".[dev]"
```

## Usage as a library

```python
from pdftalk import pdf_to_audio

pdf_to_audio("document.pdf", "document.wav")
```

```python
from pdftalk import extract_text, text_to_audio

text = extract_text("document.pdf")
text_to_audio(text, "document.wav", rate=160, volume=1.0)
```

## Usage from the command line

```bash
pdftalk document.pdf -o document.wav
pdftalk --list-voices
pdftalk document.pdf -o document.wav --rate 150 --voice-id "<voice-id>"
```

## Known limitations

- Only extracts native text from the PDF; scanned (image) PDFs will not
  produce audio because OCR is not applied.
- Voice quality and availability depend on the operating system
  (SAPI5 on Windows, NSSpeechSynthesizer on macOS, espeak on Linux).

## License

MIT
