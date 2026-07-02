from utils import run
from codon_table import codons


def solve(data: str) -> str:
    out = ""
    for i in range(0, len(data), 3):
        if i+3 < len(data):
            out += codons[data[i:i+3]]
    return out


if __name__ == "__main__":
    run(solve)
