import Die
from Weapon import Weapon

class BasePlayer():

    def __init__(self):

        self.attributes = {'MU':13, 'KL':11, 'IN':14, 'CH':10, 'FF':14, 'GE':14, 'KO':13, 'KK':12}
        self.modifiers = {'MU':0, 'KL':0, 'IN':0, 'CH':0, 'FF':0, 'GE':0, 'KO':0, 'KK':0}

        self.lifepoints = 5 + 2*self.getAttrib('KK')
        self.skills= {'dolche':11}

        self.meleeWeapon = Weapon()
    
    def getAttrib(self, attrib):
        return self.attributes[attrib.upper()] + self.modifiers[attrib.upper()]

    def modifyLife(self, value):
        self.lifepoints += value

    def isAlive(self):
        return self.lifepoints>0

    def getToughness(self):
        return round(-5 + (self.getAttrib('KO')*2 +  self.getAttrib('KK'))/6)

    def getDodge(self):
        return round(self.getAttrib('GE')/2)

    def getInitiative(self):
        r = round((self.getAttrib('MU') + self.getAttrib('GE'))/2)
        print(r)
        return r

    def getSpeed(self):
        return 8 #base value for humans

    def getSkill(self, skill):
        return self.skills[skill.lower()]
    
    def attackMelee(self):
        """returns AT + d20"""
        return self.getSkill(self.meleeWeapon.combatTechnique) + self.meleeWeapon.getModifier('AT') + int((self.getAttrib('MU') -8)/3)# >= Die.d20.roll()

    def makeDamage(self):
        return self.meleeWeapon.makeDamage()
