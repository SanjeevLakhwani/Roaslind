from utils import run, fasta_to_dict


def solve(data: str, k: int = 3) -> str:
    d = fasta_to_dict(data)
    out = ""
    for ok, ov in d.items():
        if len(ov) < k:
            continue
        suf = ov[-k:]
        for ik, iv in d.items():
            if len(iv) < k or ov == iv:
                continue
            pre = iv[:k]
            if suf == pre:
                out += f"{ok} {ik}\n"
    return out


if __name__ == "__main__":
    run(solve)
