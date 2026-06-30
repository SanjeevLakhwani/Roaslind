import argparse
from pathlib import Path


def run(solve, output_path: Path | None = None):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", help="input file")
    group.add_argument("-t", "--text", help="raw input string")
    parser.add_argument("-o", "--output", help="output file (default: stdout)")
    args = parser.parse_args()

    data = Path(args.input).read_text().strip() if args.input else args.text.strip()

    result = solve(data)

    out = Path(args.output) if args.output else output_path
    if out is None:
        print(result)
    else:
        out.write_text(result + "\n")
        print(result)
