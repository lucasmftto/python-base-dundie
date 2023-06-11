import argparse
from dundie.core import load

def main():
    parser = argparse.ArgumentParser(
        description="Dundie is a CLI tool.",
        epilog="Enjoy and use with cautious.",
    )

    parser.add_argument(
        "subcommand",
        type=str,
        help="Subcommand to run.",
        choices=("load", "show", "add", "send"),
    )

    parser.add_argument(
        "filepath",
        type=str,
        help="File Path  to load.",
    )

    args = parser.parse_args()
    
    try:
       print(*globals()[args.subcommand](args.filepath), sep="\n")
    except KeyError:
        print(f"Invalid subcommand")

