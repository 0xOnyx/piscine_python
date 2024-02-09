import sys
import string


def get_nbr_upper_case(s: str) -> int:
    """get the number of upper case characters in a string."""
    return sum(1 for c in s if c.isupper())


def get_nbr_lower_case(s: str) -> int:
    """"get the number of lower case characters in a string."""
    return sum(1 for c in s if c.islower())


def get_nbr_punctuation(s: str) -> int:
    """get the number of punctuation characters in a string."""
    return sum(1 for c in s if c in string.punctuation)


def get_nbr_space(s: str) -> int:
    """get the number of space characters in a string."""
    return sum(1 for c in s if c.isspace())


def get_nbr_digits(s: str) -> int:
    """"get the number of digits in a string."""
    return sum(1 for c in s if c.isdigit())


def main():
    """'main' documentation."""

    msg = ""
    if len(sys.argv) != 2:
        # read from standard input
        msg = input("Please enter the message:\n")
    else:
        msg = sys.argv[1]
    print(f"The text contains {len(msg)} characters:")
    print(f"{get_nbr_upper_case(msg)} upper letters")
    print(f"{get_nbr_lower_case(msg)} lower letters")
    print(f"{get_nbr_punctuation(msg)} punctuation marks")
    print(f"{get_nbr_space(msg)} spaces")
    print(f"{get_nbr_digits(msg)} digits")


if __name__ == "__main__":
    main()
