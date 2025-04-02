from typing import TYPE_CHECKING, override

from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Barbarian(Class):
    def __init__(self):
        super().__init__(15, 12, 14, 10, 13, 8)

    def rage(self):
        return "Rage"

    def unarmoredDefence(self):
        return "unarmoreDefence"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitBarbarian(self, action)

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "physique"
