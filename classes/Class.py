from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from typing_extensions import override

if TYPE_CHECKING:
    from visitor import ClassVisitor

class Class(ABC):
    def __init__(
        self,
        strength: int,
        dexterity: int,
        physique: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
    ):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.physique: int = physique
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma

    @override
    def __str__(self):
        return f"{self.strength} {self.dexterity} {self.physique} {self.intelligence} {self.wisdom} {self.charisma}"

    @abstractmethod
    def savingThrow1(self) -> str:
        pass

    @abstractmethod
    def savingThrow2(self) -> str:
        pass

    @abstractmethod
    def accept(self, visitor: "ClassVisitor", action: str):
        pass
