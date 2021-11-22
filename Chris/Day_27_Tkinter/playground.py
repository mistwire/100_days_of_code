# Create a function that can take unlimited positional arguments:

def add(*args):
    print(args[0])
    total = 0
    for i in args:
        total += i
    return total


blorp = add(1, 2, 3, 4, 5)
print(blorp)


# Create a function that can take unlimited keyword arguments with **kwargs:
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # use .get() to return None if keyword isn't specified
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Volkswagen", model="ID.4")

print(f"My car is a {my_car.color} {my_car.make} {my_car.model} with {my_car.seats} seats")

