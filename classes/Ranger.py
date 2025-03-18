from typing import override
from .Class import Class


class Ranger(Class):
    def __init__(self):
        super().__init__(10, 16, 14, 8, 14, 10)

    def favoredEnemy(self):
        pass

    def naturalExplorer(self):
        pass

    @override
    def savingThrow1(self):
        return "strength"

    @override
    def savingThrow2(self):
        return "dexterity"
