from typing import TYPE_CHECKING, override
from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Cleric(Class):
    def __init__(self):
        super().__init__(12, 10, 14, 8, 16, 10)

    @override
    def savingThrow1(self):
        return "wisdom"

    @override
    def savingThrow2(self):
        return "charisma"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitCleric(self, action)

    def spellcasting(self):
        return "spellcasting"

    def divineDomain(self):
        return "divineDomain"
