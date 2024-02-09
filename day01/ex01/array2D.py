
def slice_me(family: list, start: int, end: int) -> list:
    """"slice_me function slices a 2D list and returns a new 2D list"""
    if not all(isinstance(member, list)
               and len(member) == len(family[0]) for member in family):
        raise ValueError("Input is not a valid 2D list")

    original_shape = (len(family), len(family[0]))
    print(f"My shape is : {original_shape}")

    sliced_family = family[start:end]

    new_shape = (len(sliced_family),
                 len(sliced_family[0]) if sliced_family else 0)
    print(f"My new shape is : {new_shape}")

    return sliced_family
