from utils import run, fasta_to_dict


def solve(data: str) -> str:
    dna = list(fasta_to_dict(data).values())[0]
    # TODO: find all reverse palindromes of length 4-12
    # reverse palindrome: substring == reverse complement of itself
    return ""


if __name__ == "__main__":
    run(solve)
