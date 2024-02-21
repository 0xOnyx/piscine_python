from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)
