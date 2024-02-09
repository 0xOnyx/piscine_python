def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        """"give_bmi function calculates the BMI of a list of people"""
        raise AssertionError("must have the same length")
    return [w / (h ** 2) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
