from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import RaceVisitor


class Race(ABC):
    def __init__(
        self,
        strength: int,
        dexterity: int,
        physique: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
        speed: int,
    ):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.physique: int = physique
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma
        self.speed: int = speed

    @abstractmethod
    def accept(self, visitor: "RaceVisitor", action: str):
        pass
