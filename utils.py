import sys
from pathlib import Path


def run(solve, output_path: Path | None = None):
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file> [output_file]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    data = input_path.read_text().strip()
    result = solve(data)

    out = Path(sys.argv[2]) if len(sys.argv) >= 3 else output_path
    if out is None:
        print(result)
    else:
        out.write_text(result + "\n")
        print(result)
