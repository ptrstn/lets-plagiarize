import argparse

from plagiarize import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Conceal your plagiarism by translating your groundbreaking dissertation twice"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    return parser.parse_args()


def main():
    args = parse_arguments()


if __name__ == "__main__":
    main()
