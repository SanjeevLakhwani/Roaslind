from pathlib import Path
from utils import run, fasta_to_dict, dna_to_rna, rna_to_prot


def solve(data: str) -> str:
    seqs = fasta_to_dict(data)
    vals = list(seqs.values())
    dna = vals[0]
    introns = vals[1:]
    for i in introns:
        dna = dna.replace(i, "")


    return rna_to_prot(dna_to_rna(dna)).replace("X", "")


if __name__ == "__main__":
    run(solve, default_input=Path(__file__).parent / "inputs" / "sample.txt")
