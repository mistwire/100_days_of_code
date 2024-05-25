class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

bobs_burgers = Restaurant("Bob's Burgers", "pub food")
print(f"{bobs_burgers.restaurant_name} is a {bobs_burgers.cuisine_type} type of joint")

bobs_burgers.open_restaurant()
bobs_burgers.describe_restaurant()
