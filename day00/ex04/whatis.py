import sys


def check_number(arg):
    try:
        num = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    else:
        check_number(sys.argv[1])