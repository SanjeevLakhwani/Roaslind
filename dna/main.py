import sys
from pathlib import Path
from collections import Counter

INPUTS_DIR = Path(__file__).parent / "inputs"
OUTPUTS_DIR = Path(__file__).parent / "outputs"


def solve_1(dna: str) -> str:
    counts = {"A":0, "T":0, "G":0, "C":0}
    for nt in dna:
        counts[nt] += 1
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

def solve_2(dna: str) -> str:
    c = Counter(dna)
    return f"{c['A']} {c['C']} {c['G']} {c['T']}"

def main(input_filename: str) -> None:
    input_path = INPUTS_DIR / input_filename
    dna = input_path.read_text().strip()

    result = solve_2(dna)

    stem = Path(input_filename).stem
    output_path = OUTPUTS_DIR / f"{stem}.output.txt"
    output_path.write_text(result + "\n")

    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    main(sys.argv[1])
