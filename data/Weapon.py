import Die

class Weapon():

    def __init__(self):

        leadAttrib = 'ge'
        length = 'short'

        modifiers = {'AT':0, 'PA':-1}

        baseDamage = 2

        damageDie = Die.d6

    def makeDamage(self):
        return baseDamage + damagedie.roll()
