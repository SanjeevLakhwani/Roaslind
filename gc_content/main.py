from utils import run


def solve(data: str) -> str:
    d = {}
    ak = False
    for l in data.split('\n'):
        if l[0] == '>':
            ak = l[1:]
            d[ak] = ""
        else:
            d[ak] += l
    print(d)
    return ""


if __name__ == "__main__":
    run(solve)
