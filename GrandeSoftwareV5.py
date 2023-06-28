class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"
class SaxophoneSpec:
    def __init__(self, builder, model, typeg, numStrings):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.numStrings = numStrings

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_typeg(self):
        return self.typeg

    def get_numStrings(self):
        return self.numStrings

class Saxophone:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def get_spec(self):
        return self.spec

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

    def add_saxophone(self, serial_number, price, spec):
        saxophone = Saxophone(serial_number, price, spec)
        self.inventory.append(saxophone)

    def get_instrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec):
        matching_instruments = []
        for instrument in self.inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments

def initialize_inventory_saxophones(inventory):
    properties = {
        "instrumentType": InstrumentType.SAX.value,
        "builder": Builder.YAMAHA.value,
        "model": "YAS-62",
        "type": Type.ACOUSTIC.value,
        "numstrings": None
    }
    inventory.add_saxophone("7890123", 4500.0, SaxophoneSpec(properties))

def main():
    inventory = Inventory()
    initialize_inventory(inventory)
    initialize_inventory_saxophones(inventory)

    properties = {
        "builder": Builder.YAMAHA.value,
        "model": "YAS-62",
        "typeg": Type.ACOUSTIC.value
    }
    client_spec = SaxophoneSpec(properties)
    matching_instruments = inventory.search(client_spec)
    if matching_instruments:
        print("Talvez você goste desses saxofones:")
        for instrument in matching_instruments:
            spec = instrument.get_spec()
            print(spec.get_property("instrumentType"), "com as seguintes propriedades:")
            for property_name, property_value in spec.get_properties().items():
                if property_name == "instrumentType":
                    continue
                print(property_name + ":", property_value)
            print("Ele pode ser seu por apenas $", instrument.get_price())
            print()
    else:
        print("Desculpe, não temos nada para você")

