from utils import run, fasta_to_dict, dna_to_rna, rna_to_prot

def find_all(s:str, char: str) -> list:
    result, i = [], s.find(char)
    while i != -1:
        result.append(i)
        i = s.find(char, i + 1)
    out = []
    for si in result:
        out.append(s[si:])
    return out


def subsections(prot:str):
    splits = prot.split("X")
    if prot[-1] != "X":
        splits.pop()

    out = []
    for split in splits:
        out.extend(find_all(split, "M"))
    return out


def solve(data: str) -> str:
    dna = list(fasta_to_dict(data).values())[0]
    rc_dna = dna.translate(str.maketrans("ATCG", "TAGC"))[::-1]
    rfs = [dna, dna[1:], dna[2:], rc_dna, rc_dna[1:], rc_dna[2:]]
    prots = list(map(lambda x: rna_to_prot(dna_to_rna(x)), rfs))
    out = []
    for prot in prots:
        out.extend(subsections(prot))
    d_out = list(set(out))
    return "\n".join(d_out)


if __name__ == "__main__":
    run(solve)
