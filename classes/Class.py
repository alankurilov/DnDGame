from abc import ABC, abstractmethod


class Class(ABC):
    def __init__(self, strength, dexterity, physique, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.physique = physique
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return f"{self.strength} {self.dexterity} {self.physique} {self.intelligence} {self.wisdom} {self.charisma}"

    @abstractmethod
    def savingThrow1(self) -> str:
        pass

    @abstractmethod
    def savingThrow2(self) -> str:
        pass
