class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set odometer reading to a given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        "Add the given amount to the odometer reading"
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"{self.model}'s tank is full!")

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



my_id4 = ElectricCar('volkswagen', 'id.4', 2021)
print(my_id4.get_descriptive_name())
# my_id4.describe_battery()
my_id4.fill_gas_tank()
my_id4.battery.describe_battery()
my_id4.battery.get_range() 