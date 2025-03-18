from typing import override
from .Class import Class


class Cleric(Class):
    def __init__(self):
        super().__init__(12, 10, 14, 8, 16, 10)

    @override
    def savingThrow1(self):
        return "wisdom"

    @override
    def savingThrow2(self):
        return "charisma"

    def spellcasting(self):
        pass

    def divineDomain(self):
        pass
