from car import Car

# INHERITANCE: ElectricCar(Car) means ElectricCar gets everything Car has.
# It can then add new things or change (override) existing behavior.
class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        """Initializes attributes of the parent class"""
        # super().__init__() calls Car's __init__ to set make, model, year, odometer_reading.
        # Without this line, ElectricCar wouldn't have any of the parent's attributes.
        super().__init__(make, model, year)
        # COMPOSITION: Battery is its own class, stored as an attribute.
        # Access it via chaining: my_car.battery.describe_battery()
        self.battery = Battery()

    # OVERRIDING: This method replaces Car's version (if Car had one).
    # When you call fill_gas_tank() on an ElectricCar, this runs instead.
    def fill_gas_tank(self):
        print("This car doesn't need gas!")

# COMPOSITION PATTERN: Instead of putting all battery logic inside ElectricCar,
# we create a separate class. This keeps each class focused on one responsibility.
class Battery:
    # Default parameter: battery_size=82 is used when no value is passed
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

