from classes.Warlock import Warlock
from hero.Hero import Hero
from races.Elf import Elf
from creeps.Creep import Creep
from visitor.ClassVisitor import ClassVisitor
from visitor.RaceVisitor import RaceVisitor

Warlock = Warlock()
print("Warlock")
print(Warlock.otherwordlyPatron())
print(Warlock.spellcasting())
print(Warlock.savingThrow1())

Elf = Elf()
print("Elf")
print(Elf.__str__())

H = Hero(Warlock, Elf)

Creep = Creep(32)

RV = RaceVisitor()
CV = ClassVisitor()
# print(Elf.accept(RV, "sneakAttac"))  # RaceVisitor
print(H.class_.accept(CV, "otherwordlyPatron"))
print(H.class_.accept(CV, "spellcasting"))
print(H.class_.accept(CV, "savingThrow1"))
print(H.class_.accept(CV, "savingThrow2"))
