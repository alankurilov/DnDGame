from .Race import Race
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from visitor import RaceVisitor


class Elf(Race):
    def __init__(self):
        super().__init__(0, 2, 0, 0, 0, 0, 30)

    def darkVision(self):
        return "Im using darkVision"

    @override
    def accept(self, visitor: "RaceVisitor", action: str):
        return visitor.visitElf(self, action)


"""
    def darkVision(self, opponent: Creep, Distance: float):
        if Distance < 30:
            return f"I can see the {opponent.__class__.__name__}"
        return "i can't see anything"
"""
