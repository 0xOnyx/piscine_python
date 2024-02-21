from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """Constructor for Baratheon"""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def alive(self):
        """Alive method for Baratheon"""
        return self.is_alive

    def die(self):
        """Die method for Baratheon"""
        self.is_alive = False


class Lannister(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Constructor"""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def alive(self):
        """Alive method"""
        return self.is_alive

    def die(self):
        """Die method"""
        self.is_alive = False

    @staticmethod
    def create_lannister(name, is_alive):
        """Create lannister"""
        return Lannister(name, is_alive)
