from car import Car

# Inheritance! 
class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        """Initializes attributes of the parent class"""
        super().__init__(make, model, year)
        # add new attributes! 
        self.battery = Battery()
        

    # overriding methods from parent class
    def fill_gas_tank(self):
        print("This car doesn't need gas!")

# Instances as attributes
class Battery:
    def __init__(self, battery_size = 82) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 62:
            range = 209
        elif self.battery_size == 82:
            range = 245
        print(f"This car can go about {range} miles on a full charge")

