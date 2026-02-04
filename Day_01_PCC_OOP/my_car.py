# IMPORT STYLE 1: `from car import Car` lets you use Car() directly
# without the module prefix. Cleaner when you only need one class.
from car import Car

my_new_car = Car('jeep', "wrangler", 2023)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  # Direct attribute access (no validation)
my_new_car.read_odometer()

