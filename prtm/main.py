from utils import run


MONOISOTOPIC_MASS = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146,  "H": 137.05891, "I": 111.06841,
    "K": 128.09496, "L": 111.06841, "M": 131.04049, "N": 114.04293,
    "P": 97.05276,  "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841,  "W": 186.07931, "Y": 163.06333,
}


def solve(data: str) -> str:
    protein = data.strip()
    # TODO: implement solution
    return ""


if __name__ == "__main__":
    run(solve)
