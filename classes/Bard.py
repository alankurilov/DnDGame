from typing import override
from .Class import Class


class Bard(Class):
    def __init__(self):
        super().__init__(8, 12, 14, 10, 10, 16)

    def bardicInspiration(self):
        pass

    def spellcasting(self):
        pass

    @override
    def savingThrow1(self):
        return "dexterity"

    @override
    def savingThrow2(self):
        return "charisma"
