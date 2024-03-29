from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """docstring for Constructor"""
        super().__init__(name, is_alive, "Baratheon", "brown", "dark")

    def alive(self):
        """docstring for Method"""
        return self.is_alive

    def die(self):
        """docstring for Method"""
        self.is_alive = False


class Lannister(Character):
    """docstring for Class"""
    def __init__(self, name, is_alive=True):
        """docstring for Constructor"""
        super().__init__(name, is_alive, "Lannister", "blue",  "light")

    def alive(self):
        """docstring for Method"""
        return self.is_alive

    def die(self):
        """ docstring for Method"""
        self.is_alive = False

    @staticmethod
    def create_lannister(name, is_alive):
        return Lannister(name, is_alive)
