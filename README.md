# pdftalk

Convierte archivos PDF en archivos de audio (texto a voz), pensado para ayudar
a personas con discapacidad visual a acceder al contenido de un PDF.

- Extraccion de texto nativo del PDF (no soporta PDFs escaneados/imagenes sin OCR).
- Sintesis de voz **offline**, usando las voces instaladas en el sistema operativo
  (via [`pyttsx3`](https://pypi.org/project/pyttsx3/)), sin necesidad de internet
  ni API keys.

## Instalacion

Desde el repositorio (mientras no este publicado en PyPI):

```bash
pip install git+https://github.com/juliette-martel/pdftalk.git
```

Para desarrollo local:

```bash
git clone https://github.com/juliette-martel/pdftalk.git
cd pdftalk
pip install -e ".[dev]"
```

## Uso como libreria

```python
from pdftalk import pdf_to_audio

pdf_to_audio("documento.pdf", "documento.wav")
```

```python
from pdftalk import extract_text, text_to_audio

texto = extract_text("documento.pdf")
text_to_audio(texto, "documento.wav", rate=160, volume=1.0)
```

## Uso desde la linea de comandos

```bash
pdftalk documento.pdf -o documento.wav
pdftalk --list-voices
pdftalk documento.pdf -o documento.wav --rate 150 --voice-id "<id-de-voz>"
```

## Limitaciones conocidas

- Solo extrae texto nativo del PDF; los PDFs escaneados (imagenes) no
  produciran audio porque no se aplica OCR.
- La calidad y disponibilidad de voces depende del sistema operativo
  (SAPI5 en Windows, NSSpeechSynthesizer en macOS, espeak en Linux).

## Licencia

MIT
