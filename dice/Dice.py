from random import randint


class Dice(object):
    def __init__(self, sides: int = 6):
        self.sides: int = sides

    def roll(self, number: int = 1):
        result: int = 0
        for i in range(number):
            result += randint(1, self.sides)
        print(str(number) + "d" + str(self.sides))
        print("result: " + str(result))
        return result
