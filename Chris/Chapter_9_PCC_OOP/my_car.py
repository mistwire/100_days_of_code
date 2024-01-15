from car import Car 

my_new_car = Car('jeep', "wrangler", 2023)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

