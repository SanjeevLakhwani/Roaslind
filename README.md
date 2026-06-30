# Roaslind

[Rosalind](https://rosalind.info) problem solutions in Python.

## Structure

```
roaslind/
├── utils.py          # shared runner
├── <problem>/
│   ├── main.py       # solution
│   └── inputs/       # input files
```

## Usage

Run from project root using module syntax:

```bash
# file input
python -m dna.main -i dna/inputs/rosalind_dna.txt

# raw string input
python -m dna.main -t "AGCTTTTCATTCTGACTGCAAC"

# write output to file
python -m dna.main -i dna/inputs/rosalind_dna.txt -o dna/outputs/result.txt
```

## Problems

| Problem | Description |
|---------|-------------|
| [DNA](dna/main.py) | Counting DNA nucleotides |
| [RNA](rna/main.py) | Transcribing DNA into RNA |
| [REVC](revc/main.py) | Complementing a strand of DNA |
