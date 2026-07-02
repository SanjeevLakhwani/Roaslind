from utils import run


def solve(data: str) -> int:
    n, y = map(int, data.split())
    imt = [0] * n
    imt[0] = 1
    m = 0
    im = 1
    for i in range(1, n):
        lim = im
        im_y_ago = 0 if i - y < 0 else imt[i-y]

        im = m
        imt[i] = im

        m = lim + ( m - im_y_ago)

    return m + im


if __name__ == "__main__":
    run(solve)
