from typing import TYPE_CHECKING, override

from .Class import Class

if TYPE_CHECKING:
    from visitor import ClassVisitor


class Ranger(Class):
    def __init__(self):
        super().__init__(10, 16, 14, 8, 14, 10)

    def favoredEnemy(self):
        return "favoredEnemy"

    def naturalExplorer(self):
        return "naturalExplorer"

    @override
    def accept(self, visitor: "ClassVisitor", action: str):
        return visitor.visitRanger(self, action)

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "dexterity"
