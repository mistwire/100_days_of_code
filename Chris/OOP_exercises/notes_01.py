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
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('Volkswagen', 'ID.4', 2021)
print(my_new_car.get_descriptive_name())
