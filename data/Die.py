import random

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides+1)

d6 = Die()
d20 = Die(20)

