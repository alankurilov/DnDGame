from abc import ABC


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


"""
    @abstractmethod
    def charUpdate(self):
        pass  # Or add the actual implementation in subclasses
"""
