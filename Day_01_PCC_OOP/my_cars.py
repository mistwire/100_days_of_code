# IMPORT STYLE 2: Importing an entire module
# When you use `import car`, you must prefix with the module name: car.Car()
# This makes it explicit where each class comes from -- helpful when multiple
# modules define classes with similar names.
import car
import electric_car

my_wrangler = car.Car("jeep", 'wrangler', 2023)  # note: car.Car() not just Car()
print(my_wrangler.get_descriptive_name())
my_id4 = electric_car.ElectricCar('volkswagen', 'id.4', 2021)
print(my_id4.get_descriptive_name())

