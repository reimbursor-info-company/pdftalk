"""Interfaz de linea de comandos: pdftalk archivo.pdf -o salida.wav"""

import argparse
import sys

from .converter import list_voices, pdf_to_audio
from .extractor import PdfTextExtractionError


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pdftalk",
        description="Convierte un PDF en un archivo de audio narrado.",
    )
    parser.add_argument("pdf", nargs="?", help="Ruta al archivo PDF de entrada")
    parser.add_argument(
        "-o", "--output", default="output.wav", help="Ruta del archivo de audio de salida"
    )
    parser.add_argument("--rate", type=int, default=170, help="Velocidad de habla (palabras/min)")
    parser.add_argument("--volume", type=float, default=1.0, help="Volumen entre 0.0 y 1.0")
    parser.add_argument("--voice-id", default=None, help="ID de voz del sistema a utilizar")
    parser.add_argument(
        "--list-voices", action="store_true", help="Lista las voces disponibles y termina"
    )

    args = parser.parse_args()

    if args.list_voices:
        for voice in list_voices():
            print(f"{voice['id']}\t{voice['name']}")
        return

    if not args.pdf:
        parser.error("Debes indicar la ruta del PDF a convertir (o usar --list-voices).")

    try:
        output = pdf_to_audio(
            args.pdf,
            args.output,
            rate=args.rate,
            volume=args.volume,
            voice_id=args.voice_id,
        )
    except PdfTextExtractionError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Audio generado en: {output}")


if __name__ == "__main__":
    main()
