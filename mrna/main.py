from collections import defaultdict

from utils import run
from codon_table import codons


def reverse_codon_count() -> dict:
    c = defaultdict(int)
    for v in codons.values():
        c[v] += 1
    return c

def solve(data: str) -> int:
    protein = data.strip()
    # TODO: implement solution (answer mod 1_000_000)
    c = reverse_codon_count()
    t = 1
    for aa in protein:
        t *= c[aa]
        t %= 1000000
    return (t * 3) % 1000000


if __name__ == "__main__":
    run(solve)
