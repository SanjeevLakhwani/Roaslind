from utils import run, fasta_to_dict


def solve(data: str) -> str:
    seqs = list(fasta_to_dict(data).values())
    c = set()
    shortest = seqs[0]
    for s in seqs:
        if len(shortest) > len(s):
            shortest = s

    for i in range(len(shortest)):
        for j in range(i+1, len(shortest)):
            c.add(shortest[i:j+1])

    for s in seqs:
        nc = c.copy()
        for v in c:
            if v not in s:
                nc.discard(v)
        c = nc

    out = ""
    for v in c:
        if len(v) > len(out):
            out = v

    return out


if __name__ == "__main__":
    run(solve)
