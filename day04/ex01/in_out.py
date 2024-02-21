
def square(x: int | float) -> int | float:
    """Return the square of the given number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return the power of the given number."""
    return x ** x


def outer(x: int | float,  function) -> object:
    """Decorator that limits the number of calls to the function.
     If the function is called more than limit times."""
    count = x

    def inner():
        """Inner function that limits the
         number of calls to the function."""
        nonlocal count
        count = function(count)
        return count

    return inner
