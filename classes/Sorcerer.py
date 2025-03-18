from typing import override
from .Class import Class


class Sorcerer(Class):
    def __init__(self):
        super().__init__(8, 12, 14, 10, 10, 16)

    def sorcerousOrigin(self):
        pass

    def sorceryPoints(self):
        pass

    @override
    def savingThrow1(self):
        return "physique"

    @override
    def savingThrow2(self):
        return "charisma"
