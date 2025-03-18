from typing import override
from .Class import Class


class Monk(Class):
    def __init__(self):
        super().__init__(10, 16, 14, 8, 14, 10)

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "dexterity"

    def martialArts(self):
        pass

    def unarmoredMovement(self):
        pass
