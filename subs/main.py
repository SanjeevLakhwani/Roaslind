from utils import run


def solve(data: str) -> str:
    s, t = data.split()
    lt = len(t)
    out = ""
    for i in range(len(s)-lt):
        if s[i:i+lt] == t:
            out+=f" {i+1}"

    return out.lstrip()

if __name__ == "__main__":
    run(solve)
