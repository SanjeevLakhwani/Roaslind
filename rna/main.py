from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import run


def solve_1(dna: str) -> str:
    return dna.replace("T", "U")

def solve_2(dna: str) -> str:
    pass


if __name__ == "__main__":
    run(Path(__file__).parent, solve_1)
