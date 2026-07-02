from utils import run


def solve(data: str) -> float:
    n1, n2, n3, n4, n5, n6 = map(int, data.split())
    # n1=AA-AA, n2=AA-Aa, n3=AA-aa, n4=Aa-Aa, n5=Aa-aa, n6=aa-aa
    return 2 * (n1 + n2 + n3 + n4 * 0.75 + n5 * 0.5)

if __name__ == "__main__":
    run(solve)
