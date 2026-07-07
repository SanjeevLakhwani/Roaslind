from pathlib import Path
from utils import run

def enumerate_strings(out, s, l, a, n):
    s += l
    if len(s) == n:
        out.append(s)
    else:
        for i in a:
            enumerate_strings(out, s, i, a, n)

def solve(data: str) -> str:
    lines = data.split("\n")
    alphabet = lines[0].split()
    n = int(lines[1])
    out = []
    for l in alphabet:
        enumerate_strings(out, "", l, alphabet,n)
    return "\n".join(out)


if __name__ == "__main__":
    run(solve, default_input=Path(__file__).parent / "inputs" / "sample.txt")
