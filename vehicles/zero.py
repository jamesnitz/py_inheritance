from vehicle import Vehicle
class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0
        self.main_color = 0
        self.maximum_occupancy = 0

    def charge_battery(self):
        print("zip zip! Fully Charged")

    def drive(self):
        print("ZHOOM!")