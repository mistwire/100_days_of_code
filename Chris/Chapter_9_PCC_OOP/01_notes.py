class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age) -> None:
        """Init name and age attribs"""
        self.name = name 
        self.age = age 

    def sit(self):
        """Simulate dog sitting command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# create an instance from the class
my_dog = Dog("Mephistopheles", 6)

# access attributes
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

# call methods
my_dog.sit()
my_dog.roll_over()

class Car:
    def __init__(self, make, model, year) -> None:
        # class attributes 
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # modifying an attributes value through a method:
    def update_odometer(self, mileage):
        """Set odometer reading to a given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!")

    # increment a attribute's value through a method:
    def increment_odometer(self, miles):
        "Add the given amount to the odometer reading"
        self.odometer_reading += miles

# create an instance from the class
my_new_car = Car('Volkswagen', 'ID.4', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying an attribute's value directly:
my_new_car.odometer_reading = 23 
my_new_car.read_odometer() 

# modifying an attributes value through a method:
my_new_car.update_odometer(24)
my_new_car.read_odometer()
# add logic to prevent malformed input ;-) 
my_new_car.update_odometer(14)

my_used_car = Car('subaru', 'WRX', 2012)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(12_000)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


