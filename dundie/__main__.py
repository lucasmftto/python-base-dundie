import argparse

def load(filepath):
    """Load a file."""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found: {e}")

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
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print(f"Invalid subcommand")

    
if __name__ == "__main__":
    main() 