# PATTERN: Resource manager. Encapsulates inventory state and operations on it.
# Compare with Day 15: global resources dict vs. here: self.resources instance variable.
# Benefit: Each CoffeeMaker instance is independent (could create multiple machines).
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        # KEY CONCEPT: Instance state. self.resources is private to this object (conceptually).
        # Day 15: global resources affected all functions; here it's scoped to this instance.
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        # PATTERN: State inquiry method. Object reports its own state (Encapsulation).
        # Day 15 printed in main loop; here it's the object's responsibility.
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # KEY CONCEPT: Fixed bug from Day 15! Condition is ">" not ">="
        # This correctly allows ordering when exact amount is available.
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        # PATTERN: State mutation. This method modifies self.resources.
        # Only called after validation passes (is_resource_sufficient() + payment OK).
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

