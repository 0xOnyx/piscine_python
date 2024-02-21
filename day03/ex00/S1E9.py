from abc import ABC, abstractmethod


class Character(ABC):
    """docstring for Class"""

    def __init__(self, name, is_alive):
        """docstring for Constructor"""
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def alive(self):
        """docstring for Abstract Method"""
        pass

    @abstractmethod
    def die(self):
        """docstring for Abstract Method"""
        pass


class Stark(Character):
    """docstring for Class"""
    def __init__(self, name, is_alive=True):
        """docstring for Constructor"""
        super().__init__(name, is_alive)

    def alive(self):
        """docstring for Method"""
        return self.is_alive

    def die(self):
        """docstring for Method"""
        self.is_alive = False
