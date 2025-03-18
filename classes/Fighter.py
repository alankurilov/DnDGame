from typing import override
from .Class import Class


class Fighter(Class):
    def __init__(self):
        super().__init__(16, 12, 14, 8, 10, 10)

    def fightingStyle(self):
        pass

    def secondWind(self):
        pass

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "physique"
