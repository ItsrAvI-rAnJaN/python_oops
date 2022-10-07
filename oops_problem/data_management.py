class Inventory:
    def __init__(self, name, weight, price_per_kg):
        self.name = name
        self.weight = weight
        self.price_per_kg = price_per_kg

    def details(self):
        print(self.name)
        print(self.weight)
        print(self.price_per_kg)


if __name__ == "__main__":
    obj_rice = Inventory("Rice", 1000, 100)
    obj_pulse = Inventory("Pulse", 500, 150)
    obj_wheat = Inventory("Wheat", 5000, 50)
    obj_rice.details()
    obj_pulse.details()
    obj_wheat.details()
