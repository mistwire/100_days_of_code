# PATTERN: Data class. MenuItem encapsulates a single drink's attributes.
# Compared to Day 15's nested dict MENU["espresso"]["ingredients"]["water"],
# this is cleaner: drink.ingredients["water"] where drink is a MenuItem object.
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        # KEY CONCEPT: Ingredients bundled with the item. Each MenuItem is self-contained.
        # Day 15: separate MENU and resources; here they're logically grouped.
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


# PATTERN: Collection manager. Menu encapsulates the drink list and provides query methods.
# Day 15 used a dict; this is more scalable (easy to add methods, sort, filter, etc.).
class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        # PATTERN: Composition. Menu is composed of MenuItem objects (has-a relationship).
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        # KEY CONCEPT: Encapsulation. Caller doesn't know self.menu is a list—just gets options string.
        # Day 15: main.py directly accessed MENU dict; here Menu controls the representation.
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        # PATTERN: Linear search through collection. Returns MenuItem object (not a dict).
        # Improvement over Day 15: find_drink(order_name) is safer than MENU[order_name] (no KeyError).
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
