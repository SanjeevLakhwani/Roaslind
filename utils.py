import argparse
from pathlib import Path
from codon_table import codons


def revc(dna: str) -> str:
    return dna.translate(str.maketrans("ATCG", "TAGC"))[::-1]


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


def run(solve, output_path: Path | None = None,
        default_input: str | Path | None = None, default_text: str | None = None):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=default_input is None and default_text is None)
    group.add_argument("-i", "--input", help="input file")
    group.add_argument("-t", "--text", help="raw input string")
    parser.add_argument("-o", "--output", help="output file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        data = Path(args.input).read_text().strip()
    elif args.text:
        data = args.text.strip()
    elif default_input is not None:
        data = Path(default_input).read_text().strip()
    else:
        data = default_text.strip()

    result = solve(data)

    out = Path(args.output) if args.output else output_path
    if out is None:
        print(result)
    else:
        out.write_text(result + "\n")
        print(result)
