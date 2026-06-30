import sys
from pathlib import Path


def run(problem_dir: Path, solve):
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    data = (problem_dir / "inputs" / input_file).read_text().strip()
    result = solve(data)

    stem = Path(input_file).stem
    (problem_dir / "outputs" / f"{stem}.output.txt").write_text(result + "\n")
    print(result)
