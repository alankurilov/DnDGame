from classes.Barbarian import Barbarian
from hero.Hero import Hero
from races.Elf import Elf
from creeps.Creep import Creep
from visitor.ClassVisitor import ClassVisitor
from visitor.RaceVisitor import RaceVisitor

# A = Class(12, 21, 21, 12, 21, 21)
Bar = Barbarian()
# print(A)
print("Barbarian")
print(Bar.savingThrow1())
print(Bar.savingThrow2())

Elf = Elf()
print("Elf")
print(Elf.__str__())

H = Hero(Bar, Elf)
print(H)

Creep = Creep(32)

RV = RaceVisitor()
CV = ClassVisitor()
print(Elf.accept(RV, "darkVision"))
print(Bar.accept(CV, "rage"))
print(H.class_.accept(CV, "savingThrow2"))
