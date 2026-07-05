import argparse
from pathlib import Path
from codon_table import codons


def dna_to_rna(dna: str) -> str:
    return dna.replace("T", "U")


def rna_to_prot(rna: str) -> str:
    out = ""
    till = len(rna) - (len(rna) % 3)
    for i in range(0, till, 3):
        aa = codons.get(rna[i:i+3], "")
        out += "X" if aa == "Stop" else aa
    return out


def fasta_to_dict(data: str) -> dict[str, str]:
    d = {}
    ak = None
    for l in data.split('\n'):
        if l.startswith('>'):
            ak = l[1:]
            d[ak] = ""
        elif ak:
            d[ak] += l
    return d


def run(solve, output_path: Path | None = None):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", help="input file")
    group.add_argument("-t", "--text", help="raw input string")
    parser.add_argument("-o", "--output", help="output file (default: stdout)")
    args = parser.parse_args()

    data = Path(args.input).read_text().strip() if args.input else args.text.strip()

    result = solve(data)

    out = Path(args.output) if args.output else output_path
    if out is None:
        print(result)
    else:
        out.write_text(result + "\n")
        print(result)
