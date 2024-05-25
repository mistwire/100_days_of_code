# Importing an entire module 
import car
import electric_car

my_wrangler = car.Car("jeep", 'wrangler', 2023)
print(my_wrangler.get_descriptive_name())
my_id4 = electric_car.ElectricCar('volkswagen', 'id.4', 2021)
print(my_id4.get_descriptive_name())

