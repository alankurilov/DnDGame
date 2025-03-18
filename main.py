from classes.Sorcerer import Sorcerer
from classes.Rogue import Rogue
from classes.Barbarian import Barbarian
from classes.Bard import Bard
from classes.Cleric import Cleric
from classes.Fighter import Fighter
from classes.Monk import Monk
from classes.Ranger import Ranger
from classes.Warlock import Warlock


# A = Class(12, 21, 21, 12, 21, 21)
Bar = Barbarian()
# print(A)
print("Barbarian")
print(Bar.savingThrow1())
print(Bar.savingThrow2())

print("Rogue")
Rogue = Rogue()
print(Rogue.savingThrow1())
print(Rogue.savingThrow2())

print("Sorcerer")
Sorcerer = Sorcerer()
print(Sorcerer.savingThrow1())
print(Sorcerer.savingThrow2())

print("Bard")
bard = Bard()
print(bard.savingThrow1())
print(bard.savingThrow2())

print("Cleric")
Cleric = Cleric()
print(Cleric.savingThrow1())
print(Cleric.savingThrow2())

print("Fighter")
Fighter = Fighter()
print(Fighter.savingThrow1())
print(Fighter.savingThrow2())

print("Monk")
Monk = Monk()
print(Monk.savingThrow1())
print(Monk.savingThrow2())

print("Ranger")
Ranger = Ranger()
print(Ranger.savingThrow1())
print(Ranger.savingThrow2())

print("Warlock")
Warlock = Warlock()
print(Warlock.savingThrow1())
print(Warlock.savingThrow2())
