from utils import run, fasta_to_dict


def solve(data: str) -> str:
    d = fasta_to_dict(data)

    hk = ""
    hp = 0
    for k, v in d.items():
        p = v.count("G") + v.count("C")
        p /= len(v)
        if p > hp:
            hk, hp = k, p

    return f"{hk}\n{hp*100}"


if __name__ == "__main__":
    run(solve)
