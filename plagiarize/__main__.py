import argparse

from plagiarize import __version__
from plagiarize.core import plagiarize


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Conceal your plagiarism by translating your groundbreaking dissertation multiple times"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("text", help="Text to be plagiarized")
    parser.add_argument(
        "--language", help="Language of your text. Default: English", default="EN"
    )
    parser.add_argument(
        "--by",
        nargs="+",
        help="Bypass languages to use. Default: Chinese, German, Russian",
        default=["ZH", "DE", "RU"],
    )
    parser.add_argument(
        "--silent",
        help="Do not display bypass texts.",
        action="store_true",
        default=False,
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    print(
        plagiarize(
            text=args.text,
            source_language=args.language,
            bypass_languages=args.by,
            silent=args.silent,
        )
    )


if __name__ == "__main__":
    main()
