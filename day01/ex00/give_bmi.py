def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi function calculates the BMI of a list of people"""
    if len(height) != len(weight):
        raise AssertionError("must have the same length")
    return [w / (h ** 2) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit function applies a limit to a list of BMI"""
    return [b > limit for b in bmi]
