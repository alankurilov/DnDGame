from typing import override
from classes import Class
from races import Race


class Hero:
    def __init__(self, class_: Class, race: Race):
        self.class_: Class = class_
        self.race: Race = race
        self.strength: int = class_.strength + race.strength
        self.dexterity: int = class_.dexterity + race.dexterity
        self.physique: int = class_.physique + race.physique
        self.intelligence: int = class_.intelligence + race.intelligence
        self.wisdom: int = class_.wisdom + race.wisdom
        self.charisma: int = class_.charisma + race.charisma

    @override
    def __str__(self):
        return f"Class: {self.class_.__class__.__name__}, Race: {self.race.__class__.__name__}, strength: {self.strength}, dexterity: {self.dexterity}, physique: {self.physique}, intelligence: {self.intelligence}, wisdom:{self.wisdom}, charisma:{self.charisma}"

    """ 
    def useVisitor(self, opponent: Creep, distance: float, action: str):
        Visitor = RaceVisitor()
    """

