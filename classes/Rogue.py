from typing import override
from .Class import Class


class Rogue(Class):
    def __init__(self):
        super().__init__(8, 16, 14, 10, 12, 10)

    def sneakAttac(self):
        pass

    def cunningAction(self):
        pass

    @override
    def savingThrow1(self):
        return "dexterity"

    @override
    def savingThrow2(self):
        return "intelligence"
