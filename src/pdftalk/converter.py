"""Text/PDF to audio conversion using offline TTS (pyttsx3)."""

from pathlib import Path

import pyttsx3

from .extractor import extract_text


def text_to_audio(
    text: str,
    output_path: str | Path,
    rate: int = 170,
    volume: float = 1.0,
    voice_id: str | None = None,
) -> Path:
    """Convert text to an audio file (.wav or .mp3 depending on system support).

    rate: approximate words per minute.
    volume: between 0.0 and 1.0.
    voice_id: system voice id (see pdftalk.converter.list_voices()).
    """
    if not text.strip():
        raise ValueError("The text to convert is empty.")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    engine = pyttsx3.init()
    try:
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)
        if voice_id:
            engine.setProperty("voice", voice_id)

        engine.save_to_file(text, str(output))
        engine.runAndWait()
    finally:
        engine.stop()

    return output


def pdf_to_audio(
    pdf_path: str | Path,
    output_path: str | Path,
    rate: int = 170,
    volume: float = 1.0,
    voice_id: str | None = None,
) -> Path:
    """Extract the text from a PDF and convert it directly to audio."""
    text = extract_text(pdf_path)
    return text_to_audio(text, output_path, rate=rate, volume=volume, voice_id=voice_id)


def list_voices() -> list[dict]:
    """List the voices available on the system (id, name, languages)."""
    engine = pyttsx3.init()
    try:
        voices = engine.getProperty("voices")
        return [
            {"id": v.id, "name": v.name, "languages": v.languages}
            for v in voices
        ]
    finally:
        engine.stop()
