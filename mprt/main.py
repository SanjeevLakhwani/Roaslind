import urllib.request
from utils import run
import re


def fetch_fasta(uniprot_id: str) -> str:
    uid = uniprot_id.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{uid}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def solve(data: str) -> str:
    ids = data.split()
    r = re.compile(r"(?=(N[^P][ST][^P]))")
    out = []
    for uid in ids:
        seq = fetch_fasta(uid)
        indexes = [m.start()+1 for m in r.finditer(seq)]
        if indexes:
            out.append(uid)
            out.append(" ".join(map(str, indexes)))
    return "\n".join(out)

if __name__ == "__main__":
    run(solve)
