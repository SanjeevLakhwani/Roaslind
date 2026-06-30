from utils import run


def solve_1(dna: str) -> str:
    return dna.replace("T", "U")


if __name__ == "__main__":
    run(solve_1)
