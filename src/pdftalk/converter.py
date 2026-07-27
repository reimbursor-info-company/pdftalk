"""Conversion de texto/PDF a archivos de audio usando TTS offline (pyttsx3)."""

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
    """Convierte un texto a un archivo de audio (.wav o .mp3 segun soporte del sistema).

    rate: palabras por minuto aproximadas.
    volume: entre 0.0 y 1.0.
    voice_id: id de voz del sistema (ver pdftalk.converter.list_voices()).
    """
    if not text.strip():
        raise ValueError("El texto a convertir esta vacio.")

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
    """Extrae el texto de un PDF y lo convierte directamente a audio."""
    text = extract_text(pdf_path)
    return text_to_audio(text, output_path, rate=rate, volume=volume, voice_id=voice_id)


def list_voices() -> list[dict]:
    """Lista las voces disponibles en el sistema (id, nombre, idiomas)."""
    engine = pyttsx3.init()
    try:
        voices = engine.getProperty("voices")
        return [
            {"id": v.id, "name": v.name, "languages": v.languages}
            for v in voices
        ]
    finally:
        engine.stop()
