from utils import run, fasta_to_dict
from codon_table import codons


def solve(data: str) -> str:
    dna = list(fasta_to_dict(data).values())[0]
    # TODO: implement solution (check all 6 reading frames: 3 forward, 3 reverse complement)
    return ""


if __name__ == "__main__":
    run(solve)
