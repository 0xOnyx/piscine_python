from abc import ABC, abstractmethod


class Character(ABC):
    """Character class for Game of Thrones."""

    @abstractmethod
    def __init__(self, name, is_alive):
        """__init__ method for Character"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def alive(self):
        """Alive method for Baratheon"""
        pass

    @abstractmethod
    def die(self):
        """Die method for Baratheon"""
        pass

    def __str__(self):
        """"__str__ method"""
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))

    def __repr__(self):
        """__repr__ method"""
        return ("Vector: ('{}', '{}', '{}')"
                .format(self.first_name, self.eyes, self.hairs))

    def set_eyes(self, color):
        """eye method"""
        self.eyes = color

    def set_hairs(self, color):
        """hair method"""
        self.hairs = color

    def get_eye(self):
        """Eye method"""
        return self.eyes

    def get_hair(self):
        """Hair method"""
        return self.hairs


class Stark(Character):
    """Stark class"""
    def __init__(self, name, is_alive=True):
        """Constructor"""
        super().__init__(name, is_alive)

    def alive(self):
        """Alive method"""
        return self.is_alive

    def die(self):
        """Die method"""
        self.is_alive = False
