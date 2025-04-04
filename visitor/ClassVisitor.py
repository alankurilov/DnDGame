from classes.Barbarian import Barbarian
from classes.Bard import Bard
from classes.Cleric import Cleric
from classes.Fighter import Fighter
from classes.Monk import Monk
from classes.Ranger import Ranger
from classes.Rogue import Rogue
from classes.Sorcerer import Sorcerer
from classes.Warlock import Warlock


class ClassVisitor:
    def visitBarbarian(self, barbarian: Barbarian, action: str):
        if action == "rage":
            return barbarian.rage()
        elif action == "unarmoredDefence":
            return barbarian.unarmoredDefence()
        elif action == "savingThrow2":
            return barbarian.savingThrow1()
        elif action == "savingThrow2":
            return barbarian.savingThrow1()
        raise ValueError("Unknown action")

    def visitBard(self, bard: Bard, action: str):
        if action == "bardicInspiration":
            return bard.bardicInspiration()
        elif action == "spellcasting":
            return bard.spellcasting()
        elif action == "savingThrow1":
            return bard.savingThrow1()
        elif action == "savingThrow2":
            return bard.savingThrow2()
        raise ValueError("unknown action")

    def visitCleric(self, cleric: Cleric, action: str):
        if action == "spellcasting":
            return cleric.spellcasting()
        elif action == "divineDomain":
            return cleric.divineDomain()
        elif action == "savingThrow1":
            return cleric.savingThrow1()
        elif action == "savingThrow2":
            return cleric.savingThrow2()
        raise ValueError("unknown action")

    def visitFighter(self, fighter: Fighter, action: str):
        if action == "fightingStyle":
            return fighter.fightingStyle()
        elif action == "secondWind":
            return fighter.secondWind()
        elif action == "savingThrow1":
            return fighter.savingThrow1()
        elif action == "savingThrow2":
            return fighter.savingThrow2()
        raise ValueError("unknown action")

    def visitMonk(self, monk: Monk, action: str):
        if action == "martialArts":
            return monk.martialArts()
        elif action == "unarmoredMovement":
            return monk.unarmoredMovement()
        elif action == "savingThrow1":
            return monk.savingThrow1()
        elif action == "savingThrow2":
            return monk.savingThrow2()
        raise ValueError("unknown action")

    def visitRanger(self, ranger: Ranger, action: str):
        if action == "favoredEnemy":
            return ranger.favoredEnemy()
        elif action == "naturalExplorer":
            return ranger.naturalExplorer()
        elif action == "savingThrow1":
            return ranger.savingThrow1()
        elif action == "savingThrow2":
            return ranger.savingThrow2()
        raise ValueError("unknown action")

    def visitRogue(self, rogue: Rogue, action: str):
        if action == "sneakAttac":
            return rogue.sneakAttac()
        elif action == "cunningAction":
            return rogue.cunningAction()
        elif action == "savingThrow1":
            return rogue.savingThrow1()
        elif action == "savingThrow2":
            return rogue.savingThrow2()
        raise ValueError("unknown action")

    def visitSorcerer(self, sorcerer: Sorcerer, action: str):
        if action == "sorcerousOrigin":
            return sorcerer.sorcerousOrigin()
        elif action == "sorceryPoints":
            return sorcerer.sorceryPoints()
        elif action == "savingThrow1":
            return sorcerer.savingThrow1()
        elif action == "savingThrow2":
            return sorcerer.savingThrow2()
        raise ValueError("unknown action")

    def visitWarlock(self, warlock: Warlock, action: str):
        if action == "otherwordlyPatron":
            return warlock.otherwordlyPatron()
        elif action == "spellcasting":
            return warlock.spellcasting()
        elif action == "savingThrow1":
            return warlock.savingThrow1()
        elif action == "savingThrow2":
            return warlock.savingThrow2()
        raise ValueError("unknown action")
