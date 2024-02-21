import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random id"""
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=15))


@dataclass
class Student:
    """class Student with name, surname, active, login and id attributes"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: int = field(default=True)
    login: str = field(init=False)
    id: list = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Post-init method to set the login attribute"""
        self.login = self.name[0].capitalize() + self.surname.lower()
