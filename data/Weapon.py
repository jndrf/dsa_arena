import Die

class Weapon():

    def __init__(self):

        self.leadAttrib = 'ge'
        self.length = 'short'

        self.modifiers = {'AT':0, 'PA':-1}

        self.baseDamage = 2

        self.damageDie = Die.d6

        self.combatTechnique = 'dolche'

    def makeDamage(self):
        return self.baseDamage + self.damageDie.roll()

    def getModifier(self, property):
        return self.modifiers[property]
