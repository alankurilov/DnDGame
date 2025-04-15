from typing import override
from classes.Class import Class
from races.Race import Race
from creeps.Creep import Creep
from dice.Dice import Dice


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

    def acttack(self, creep: Creep):
        dice = Dice(20)
        attack = dice.roll(1)
        attack += round(((self.class_.strength - 10 - 0.5) / 2))
        if attack >= creep.criticalAttack:
            creep.HP -= attack
            print("You hit,", attack)
            print("Creep has", creep.HP, "left")
        else:
            print("miss")
