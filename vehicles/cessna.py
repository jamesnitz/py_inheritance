from vehicles import Vehicle
class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        print("glug. Time for take-off")

    def drive(self):
        print("nyeeea!")


