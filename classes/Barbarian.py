from typing import override
from .Class import Class


class Barbarian(Class):
    def __init__(self):
        super().__init__(15, 12, 14, 10, 13, 8)

    def Rage(self):
        pass

    def unarmoredDefence(self):
        pass

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "physique"
