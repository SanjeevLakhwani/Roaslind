import urllib.request
from utils import run


def fetch_fasta(uniprot_id: str) -> str:
    uid = uniprot_id.split("_")[0]
    url = f"https://www.uniprot.org/uniprot/{uid}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def solve(data: str) -> str:
    ids = data.split()
    # TODO: implement solution
    return ""


if __name__ == "__main__":
    run(solve)
