import sys
from pathlib import Path

INPUTS_DIR = Path(__file__).parent / "inputs"
OUTPUTS_DIR = Path(__file__).parent / "outputs"


def solve(dna: str) -> str:
    # TODO: implement solution
    return ""


def main(input_filename: str) -> None:
    input_path = INPUTS_DIR / input_filename
    dna = input_path.read_text().strip()

    result = solve(dna)

    stem = Path(input_filename).stem
    output_path = OUTPUTS_DIR / f"{stem}.output.txt"
    output_path.write_text(result + "\n")

    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    main(sys.argv[1])
