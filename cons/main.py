from collections import defaultdict
from utils import run, fasta_to_dict

nts = ["A", "C", "G", "T"]

def solve(data: str) -> str:
    d = fasta_to_dict(data)
    m = []
    for r in d.values():
        m.append(r)

    out = ""

    for j in range(len(m[0])):
        c = defaultdict(int)
        for i in range(len(m)):
            c[m[i][j]] += 1

        mn = ""
        mv = 0
        for nt in nts:
            if mv < c[nt]:
                mn = nt
                mv = c[nt]

        out += mn

    return out


if __name__ == "__main__":
    run(solve)
