from classes.Barbarian import Barbarian


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

    """
    def visitBard(self, bard: Bard, action: str):
        if action =="""
