from car import ElectricCar

my_id4 = ElectricCar('volkswagen', 'id.4', 2021)
print(my_id4.get_descriptive_name())
my_id4.battery.describe_battery()
my_id4.battery.get_range() 