from utils import run

def perm(l:list) -> list :
    if len(l) == 1:
        return [l]
    out = []
    for i in range(len(l)):
        for p in perm(l[:i]+l[i+1:]):
            out.append([l[i], *p])
    return out


def solve(data: str) -> str:
    n = int(data.strip())

    perms = perm(list(range(1,n+1)))
    joined = [" ".join(str(x) for x in p) for p in perms]

    return f"{len(perms)}\n{'\n'.join(joined)}"


if __name__ == "__main__":
    run(solve)
