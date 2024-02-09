import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
}


def main(argv):
    if len(argv) != 2:
        raise AssertionError("more than one argument is provided")
    if not all(c.isalnum() or c.isspace() for c in argv[1]):
        raise AssertionError("the argument is bad")
    print("".join([NESTED_MORSE[c] for c in argv[1].upper()]))


if __name__ == "__main__":
    main(sys.argv)
