from utils import run, fasta_to_dict


def solve(data: str) -> str:
    seqs = list(fasta_to_dict(data).values())
    # TODO: implement solution
    return ""


if __name__ == "__main__":
    run(solve)
