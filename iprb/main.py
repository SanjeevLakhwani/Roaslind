from utils import run

def solve(data: str) -> float:
    d, m, r = map(int, data.split())
    t = d + m + r
    dd = (d/t) + (m / t * d / (t - 1)) + ((r / t) * (d / (t - 1)))
    mm = m/t * (m-1) / (t-1)
    mr = (m/t*r/(t-1)) + (r/t*m/(t-1))
    return dd + (mm * 0.75) + (mr * 0.5)


if __name__ == "__main__":
    run(solve)
