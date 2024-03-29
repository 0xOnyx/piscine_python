from abc import ABC, abstractmethod


class Character(ABC):
    """Character class."""

    def __init__(self, name, is_alive, family_name, eyes, hairs):
        """docstring for Constructor"""
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @abstractmethod
    def alive(self):
        """docstring for Abstract Method"""
        pass

    @abstractmethod
    def die(self):
        """docstring for Abstract Method"""
        pass

    def __str__(self):
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))

    def __repr__(self):
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))


class Stark(Character):
    """docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)

    def alive(self):
        """docstring for Method"""
        return self.is_alive

    def die(self):
        """docstring for Method"""
        self.is_alive = False
