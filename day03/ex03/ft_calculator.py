class calculator:
    """calculator class"""
    def __init__(self, data):
        """Constructor"""
        self.data = data

    def __add__(self,  scalar) -> None:
        """Add a scalar to the vector."""
        result = [element + scalar for element in self.data]
        print(result)

    def __sub__(self, scalar) -> None:
        """Subtract a scalar from the vector."""
        result = [element - scalar for element in self.data]
        print(result)

    def __mul__(self, scalar) -> None:
        """Multiply the vector by a scalar."""
        result = [element * scalar for element in self.data]
        print(result)

    def __truediv__(self, scalar):
        """Divide the vector by a scalar."""
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        result = [element / scalar for element in self.data]
        print(result)
