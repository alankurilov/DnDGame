from classes.Rogue import Rogue
from hero.Hero import Hero
from races.Elf import Elf
from creeps.Creep import Creep
from visitor.ClassVisitor import ClassVisitor
from visitor.RaceVisitor import RaceVisitor

Rogue = Rogue()
print("Rogue")
print(Rogue.sneakAttac())
print(Rogue.cunningAction())
print(Rogue.savingThrow1())

Elf = Elf()
print("Elf")
print(Elf.__str__())

H = Hero(Rogue, Elf)

Creep = Creep(32)

RV = RaceVisitor()
CV = ClassVisitor()
# print(Elf.accept(RV, "sneakAttac"))  # RaceVisitor
print(H.class_.accept(CV, "sneakAttac"))
print(H.class_.accept(CV, "cunningAction"))
print(H.class_.accept(CV, "savingThrow1"))
print(H.class_.accept(CV, "savingThrow2"))
