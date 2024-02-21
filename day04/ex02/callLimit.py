from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of calls to the function.
        If the function is called more than limit times,
        it will print an error message."""
    count = 0

    def callLimiter(function):
        """Inner function that limits the number of calls to the function."""
        def limit_function(*args: Any, **kwargs: Any):
            """Inner function that limits the number
            of calls to the function."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
