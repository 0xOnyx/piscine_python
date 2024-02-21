from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print the statistics of the given data."""
    result = {"mean": 0, "median": 0, "quartile": [0, 0], "std": 0, "var": 0}

    if len(args) != 0:
        result["mean"] = sum(args) / len(args)
        if len(args) % 2 == 0:
            result['median'] = (sorted(args)[len(args) // 2]
                                + sorted(args)[len(args) // 2 - 1]) / 2
        else:
            result['median'] = sorted(args)[len(args) // 2]

        result['quartile'] = [
            args[(3 * len(args) + 1) // 4 - 1],
            args[len(args) + 3 // 4 - 1]
        ]
        result["var"] = (sum((x - result['mean']) ** 2
                             for x in args) / len(args))
        result["std"] = result["var"] ** 0.5

    for key, value in kwargs.items():
        if value in result:
            if len(args) == 0:
                print("ERROR")
            else:
                print(f"{value}: {result[value]}")
