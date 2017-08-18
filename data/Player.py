class Player():

    __init__(self, attributes, modifiers):
    """
Takes a dictionary containing the attributes and one withthe modifers
    """

    self.attributes = attributes
    self.modifiers = modifiers
    def getAttrib(self, attrib):
        return self.attributes[attrib.upper()] + self.modifiers[attrib.upper()]

    def getToughness(self):
        return round(-5 + (self.getAttrib['KO']*2 +  self.getAttrib['KK'])/6)

    def getDodge(self):
        return round(self.getAttrib['GW']/2)

    def getInitiative(self):
        return round((self.getAttrib['MU'] + self.getAttrib['GE'])/2)

    def getSpeed(self):
        return 8 #base value for humans
