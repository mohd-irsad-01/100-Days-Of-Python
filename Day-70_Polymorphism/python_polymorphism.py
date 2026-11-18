class car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a button")

class Scooter:
    def start(self):
        print("Scooter starts with a self start button")

vehicles = [car(), Bike(), Scooter()]
for vehicle in vehicles:
    vehicle.start()
