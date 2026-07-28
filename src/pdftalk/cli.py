"""Command-line interface: pdftalk file.pdf -o output.wav"""

import argparse
import sys

from .converter import list_voices, pdf_to_audio
from .extractor import PdfTextExtractionError


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pdftalk",
        description="Convert a PDF into a narrated audio file.",
    )
    parser.add_argument("pdf", nargs="?", help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output", default="output.wav", help="Path to the output audio file"
    )
    parser.add_argument("--rate", type=int, default=170, help="Speech rate (words/min)")
    parser.add_argument("--volume", type=float, default=1.0, help="Volume between 0.0 and 1.0")
    parser.add_argument("--voice-id", default=None, help="System voice ID to use")
    parser.add_argument(
        "--list-voices", action="store_true", help="List available voices and exit"
    )

    args = parser.parse_args()

    if args.list_voices:
        for voice in list_voices():
            print(f"{voice['id']}\t{voice['name']}")
        return

    if not args.pdf:
        parser.error("You must specify the path to the PDF to convert (or use --list-voices).")

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

    print(f"Audio generated at: {output}")


if __name__ == "__main__":
    main()
