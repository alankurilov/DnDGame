from classes.Sorcerer import Sorcerer
from classes.Rogue import Rogue
from classes.Barbarian import Barbarian
from classes.Bard import Bard
from classes.Cleric import Cleric
from classes.Fighter import Fighter
from classes.Monk import Monk
from classes.Ranger import Ranger
from classes.Warlock import Warlock
from races.Human import Human
from races.Race import Race
from hero.Hero import Hero


# A = Class(12, 21, 21, 12, 21, 21)
Bar = Barbarian()
# print(A)
print("Barbarian")
print(Bar.savingThrow1())
print(Bar.savingThrow2())

Hu = Human()
print("Human")
print(Hu.__str__())

H = Hero(Bar, Hu)
print(H.class_.savingThrow1())
