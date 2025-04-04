from typing import TYPE_CHECKING, override

from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Sorcerer(Class):
    def __init__(self):
        super().__init__(8, 12, 14, 10, 10, 16)

    def sorcerousOrigin(self):
        return "sorcerousOrigin"

    def sorceryPoints(self):
        return "sorceryPoints"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitSorcerer(self, action)

    @override
    def savingThrow1(self):
        return "physique"

    @override
    def savingThrow2(self):
        return "charisma"
