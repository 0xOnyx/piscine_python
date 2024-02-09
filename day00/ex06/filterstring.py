import sys
from ft_filter import ft_filter


def main(arg):
    """"main"""
    # Check if the number of arguments is correct and types are appropriate
    assert len(arg) == 3 and arg[2].isdigit(), "the arguments are bad"

    # Parse arguments
    s = arg[1]
    n = int(arg[2])

    # Filter words and print the result
    filtered_words = ft_filter(s.split(), lambda x: len(x) > n)
    print(filtered_words)


if __name__ == "__main__":
    main(sys.argv)
