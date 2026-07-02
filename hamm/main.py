from utils import run


def solve(data: str) -> int:
    s, t = data.split()
    c = 0
    for sbp, tbp in zip(s, t):
        if sbp != tbp:
            c += 1

    return c

if __name__ == "__main__":
    run(solve)
