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

class Mandolin:
    def __init__(self, serial_number, price, builder, model, typeg, numStrings, style):
        self.serial_number = serial_number
        self.price = price
        self.spec = MandolinSpec(builder, model, typeg, numStrings, style)

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def get_builder(self):
        return self.spec.get_builder()

    def get_model(self):
        return self.spec.get_model()

    def get_typeg(self):
        return self.spec.get_typeg()

    def get_numStrings(self):
        return self.spec.get_numStrings()

    def get_style(self):
        return self.spec.get_style()


"""
2)Após a implementação analise o Diagrama de Classes e Código implementados e aponte os problemas encontrados nessa forma de implementação.

Problemas encontrados:

         A classe MandolinSpec está faltando informações específicas sobre as madeiras utilizadas (como back_wood e top_wood) em sua 
         implementação. 

         A classe Mandolin não possui métodos getters para acessar as informações específicas do mandolim, como get_builder, get_model,
        get_typeg, get_numStrings e get_style.

        A classe Mandolin não tem o método matches para realizar a comparação de especificações com outro objeto MandolinSpec.
        
        Além disso, é necessário atualizar a classe Inventory para permitir a adição e pesquisa de mandolins no inventário, 
        similar ao que foi feito para as guitarras. Isso envolveria adicionar métodos add_mandolin e search_mandolin na classe Inventory, 
        semelhantes aos métodos existentes para as guitarras.

    
"""

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


