# Note: ElectricCar is defined in electric_car.py, not car.py.
# This import would actually fail -- it should be: from electric_car import ElectricCar
from electric_car import ElectricCar

my_id4 = ElectricCar('volkswagen', 'id.4', 2021)
print(my_id4.get_descriptive_name())  # Inherited from Car -- ElectricCar didn't need to define this
my_id4.battery.describe_battery()     # COMPOSITION in action: chaining through the Battery attribute
my_id4.battery.get_range()            # my_id4 -> battery (Battery instance) -> get_range() method