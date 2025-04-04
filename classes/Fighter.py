from typing import TYPE_CHECKING, override

from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Fighter(Class):
    def __init__(self):
        super().__init__(16, 12, 14, 8, 10, 10)

    def fightingStyle(self):
        return "fightingStyle"

    def secondWind(self):
        return "secondWind"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitFighter(self, action)

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "physique"
