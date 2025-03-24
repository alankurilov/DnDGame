from classes import Class
from races import Race


class Hero:
    def __init__(self, class_: Class, race: Race):
        self.class_ = class_
        self.race = race

    def __str__(self):
        return f"Class: {self.class_.__class__.__name__}, Race: {self.race.__class__.__name__}"
