from utils import run


def solve_1(dna: str) -> str:
    c = str.maketrans({"A": "T", "T": "A", "G": "C", "C": "G"})
    return dna.translate(c)[::-1]


if __name__ == "__main__":
    run(solve_1)
