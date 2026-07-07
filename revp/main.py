from pathlib import Path
from utils import run, fasta_to_dict, revc


def max_palindrome_substring(dna: str) -> int:
    rc = revc(dna)
    mp = len(dna)//2
    c = 0
    for i in range(mp):
        if dna[mp-i-1] == rc[mp-i-1] and dna[mp+i] == rc[mp+i]:
            c+=2
        else:
            break
    return c

def solve(data: str) -> str:
    dna = list(fasta_to_dict(data).values())[0]
    out = []

    # 4->10
    for i in range(4,11,2):
        r = max_palindrome_substring(dna[:i])
        if r > 3:
            for j in range(4,r+1,2):
                out.append((i//2-j//2,j))

    for i in range(4,11,2):
        r = max_palindrome_substring(dna[-i:])
        if r > 3:
            for j in range(4, r+1, 2):
                out.append((len(dna)-i//2-j//2,j))

    for i in range(len(dna)-11):
        r = max_palindrome_substring(dna[i:i+12])
        if r > 3:
            for j in range(4, r + 1, 2):
                out.append((i + 6 - j // 2, j))

    return "\n".join([f"{o[0]+1} {o[1]}" for o in out])



if __name__ == "__main__":
    run(solve, default_input=Path(__file__).parent / "inputs" / "sample.txt")
