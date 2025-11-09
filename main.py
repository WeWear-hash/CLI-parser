import argparse
import pytest
from app.parse_file import count_rows

def main():
    parser = argparse.ArgumentParser(
        prog="CSV Parser CLI",
        description="This tool parses CSV files and optionally runs tests."
    )

    parser.add_argument(
        "--file",
        required=True,
        type=str,
        help="Path to the CSV file to parse"
    )

    parser.add_argument(
        "--parse",
        action="store_true",
        help="Parse and count the number of lines in the file"
    )

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run all unit tests using pytest"
    )

    args = parser.parse_args()

    # Handle parse command
    if args.parse:
        try:
            rows = count_rows(args.file)
            print(f"File '{args.file}' has {rows} rows.")
        except Exception as e:
            print(f"Error while parsing file: {e}")

    # Handle test command
    if args.test:
        print("Running tests with pytest...\n")
        pytest.main(["-v"])  # Run pytest in verbose mode

if __name__ == "__main__":
    main()
