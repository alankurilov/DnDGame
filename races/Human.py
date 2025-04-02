from abc import abstractmethod
from .Race import Race

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import RaceVisitor


class Human(Race):
    def __init__(self):
        super().__init__(1, 1, 1, 1, 1, 1, 30)

    @abstractmethod
    def accept(self, visitor: "RaceVisitor", action: str):
        pass
