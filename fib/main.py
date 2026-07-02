from utils import run


def solve(data: str) -> int:
    n, k = map(int, data.split())

    mc = 0
    imc = 1
    for i in range(n-1):
        lm = mc
        lim = imc
        mc = lm + lim
        imc = k * lm

    return mc + imc


if __name__ == "__main__":
    run(solve)
