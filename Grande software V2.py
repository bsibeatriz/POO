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

#Classe Guitar
class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood
    
# Classe Inventory
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar_spec = GuitarSpec(builder, model, typeg, back_wood, top_wood)
        guitar = Guitar(serial_number, price, guitar_spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_spec):
        for guitar in self.guitars:
            if search_spec.get_builder() != guitar.get_spec().get_builder():
                continue
            
            model = search_spec.get_model().lower()
            if model and model != "" and model != guitar.get_spec().get_model().lower():
                continue
            
            if search_spec.get_typeg() != guitar.get_spec().get_typeg():
                continue
            if search_spec.get_back_wood() != guitar.get_spec().get_back_wood():
                continue
            if search_spec.get_top_wood() != guitar.get_spec().get_top_wood():
                continue
            return guitar
        return None

    
#Houve alteração aqui!

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

# Classe GuitarSpec
class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_typeg(self):
        return self.typeg

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood

# Testando o Sistema

inventory = Inventory()
inventory.add_guitar("123", 1000, "Fender", "Stratocaster", "Electric", "Maple", "Alder")
inventory.add_guitar("456", 1500, "Gibson", "Les Paul", "Electric", "Mahogany", "Maple")

search_spec = GuitarSpec("Fender", "Stratocaster", "Electric", "Maple", "Alder")
found_guitar = inventory.search_guitar(search_spec)
if found_guitar:
    print("Guitarra encontrada:")
    print("Número de Serial:", found_guitar.get_serial_number())
    print("Preço:", found_guitar.get_price())
else:
    print("Guitarra não encontrada.")

def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)
    
    #spec2 = GuitarSpec(Builder.MARTIN, "D-18", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("122784", 5495.95, spec2)
    #inventory.addGuitar("76531", 6295.95, Builder.MARTIN, "OM-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("70108276", 2295.95, Builder.GIBSON, "Les Paul", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("77023", 6275.95, Builder.MARTIN, "D-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
 

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.getSpec()
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:\n{guitarSpec.getBackWood().value} na traseira e laterais,\n{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()

def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)
    
    #spec2 = GuitarSpec(Builder.MARTIN, "D-18", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("122784", 5495.95, spec2)
    #inventory.addGuitar("76531", 6295.95, Builder.MARTIN, "OM-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("70108276", 2295.95, Builder.GIBSON, "Les Paul", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("77023", 6275.95, Builder.MARTIN, "D-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
 

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.getSpec()
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:\n{guitarSpec.getBackWood().value} na traseira e laterais,\n{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()