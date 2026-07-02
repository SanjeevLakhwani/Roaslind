from utils import run


def solve(data: str) -> str:
    d = {}
    ak = False
    for l in data.split():
        if l[0] == '>':
            ak = l[1:]
            d[ak] = ""
        else:
            d[ak] += l

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
