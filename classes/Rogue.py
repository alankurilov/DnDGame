from typing import TYPE_CHECKING, override

from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Rogue(Class):
    def __init__(self):
        super().__init__(8, 16, 14, 10, 12, 10)

    def sneakAttac(self):
        return "sneakAttac"

    def cunningAction(self):
        return "cunningAction"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitRogue(self, action)

    @override
    def savingThrow1(self):
        return "dexterity"

    @override
    def savingThrow2(self):
        return "intelligence"
