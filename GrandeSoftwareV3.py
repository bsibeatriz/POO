from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Guitar:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars
    
def search_guitar(self, builder, model, typeg, back_wood, top_wood):
    for guitar in self.guitars:
        if builder != guitar.get_builder():
            continue
        if model and model != "" and model != guitar.get_model().lower():
            continue
        if typeg != guitar.get_typeg():
            continue
        if back_wood != guitar.get_back_wood():
            continue
        if top_wood != guitar.get_top_wood():
            continue
        return guitar
    return None

class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars

class GuitarSpec:
    def __init__(self, builder, model, typeG, backWood, topWood, numStrings):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
        self.numStrings = numStrings

    def getBuilder(self):
        return self.builder

    def getTypeG(self):
        return self.typeG

    def getModel(self):
        return self.model

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def getNumStrings(self):
        return self.numStrings


