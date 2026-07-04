from math import comb
from utils import run

def solve(data: str) -> float:
    k, n = map(int, data.split())
    t = 2 ** k
    c = 0
    for i in range(n):
        c += comb(t, i) * (0.25 ** i) * (0.75 ** (t - i))
    return 1 - c

if __name__ == "__main__":
    run(solve)
