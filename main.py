from classes.Warlock import Warlock
from hero.Hero import Hero
from races.Elf import Elf
from creeps.Creep import Creep
from visitor.ClassVisitor import ClassVisitor
from visitor.RaceVisitor import RaceVisitor
from dice.Dice import Dice

print(round(((4 - 10 - 0.5) / 2)))

Warlock = Warlock()
print("Warlock")
print(Warlock.otherwordlyPatron())
print(Warlock.spellcasting())
print(Warlock.savingThrow1())

Elf = Elf()
print("Elf")
print(Elf.__str__())

H = Hero(Warlock, Elf)

Creep = Creep(32, 8)

RV = RaceVisitor()
CV = ClassVisitor()
H.acttack(Creep)

# print(Elf.accept(RV, "sneakAttac"))  # RaceVisitor
