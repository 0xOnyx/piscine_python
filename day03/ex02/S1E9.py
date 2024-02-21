from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, name, is_alive):
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def alive(self):
        """Your docstring for Abstract Method"""
        pass

    @abstractmethod
    def die(self):
        """Your docstring for Abstract Method"""
        pass

    def __str__(self):
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))

    def __repr__(self):
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))

    def set_eyes(self, color):
        """Your docstring for Method"""
        self.eyes = color

    def set_hairs(self, color):
        """Your docstring for Method"""
        self.hairs = color

    def get_eye(self):
        """Your docstring for Method"""
        return self.eyes

    def get_hair(self):
        """Your docstring for Method"""
        return self.hairs


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)

    def alive(self):
        """Your docstring for Method"""
        return self.is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
