from collections import Counter
from utils import run


def solve_1(dna: str) -> str:
    counts = {"A":0, "T":0, "G":0, "C":0}
    for nt in dna:
        counts[nt] += 1
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

def solve_2(dna: str) -> str:
    c = Counter(dna)
    return f"{c['A']} {c['C']} {c['G']} {c['T']}"


if __name__ == "__main__":
    run(solve_2)
