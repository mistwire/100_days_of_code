# PATTERN: Nested dictionary for hierarchical data. Each drink is a key with a dict value
# containing "ingredients" (itself a dict) and "cost". This mirrors real-world structure.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# KEY CONCEPT: Shared global state. These variables track machine inventory and revenue.
# Problem: Global variables make testing difficult (Day 16 solves this with classes).
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
coffee_is_on = True

def is_resources_sufficient(order_ingredients):
    """Determines if there are enough resources to make the drink order"""
    # PATTERN: Validation check. Iterate through required ingredients and verify availability.
    # BUG: Condition should be ">" not ">=" - this prevents ordering when exact amount is available.
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True 

def process_coins():
    """Returns total cash amount from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, cost_of_drink):
    """returns True if payment is accepted, False if not enough money"""
    if money_recieved >= cost_of_drink:
        change = round(money_recieved - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        # KEY CONCEPT: The 'global' keyword allows this function to modify the outer scope variable.
        # This is needed because we're using procedural programming without encapsulation.
        # Day 16 moves this to a MoneyMachine class (self.profit += cost) - much cleaner!
        global money
        money += cost_of_drink

        return True
    else:
        print("You have not put in enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Remove the required ingredients from the resources"""
    # PATTERN: Resource deduction. Iterates through ordered ingredients and updates global resources.
    # This is the final step only after passing all prior checks (validation → payment → execution).
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")



# PATTERN: State machine loop. Three types of inputs are handled:
# 1. 'off' - Exit the program
# 2. 'report' - Display current inventory and revenue
# 3. Drink name - Initiate a transaction with sequential validation
while coffee_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if order == 'off':
        coffee_is_on = False
    elif order == 'report':
        # Display current state (resources and money). Compare with Day 16's CoffeeMaker.report()
        print(f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: $ {money}")
    else:
        # KEY CONCEPT: Transaction workflow - multiple validation steps BEFORE execution.
        # Step 1: Extract drink recipe from nested dict
        drink = MENU[order]
        # Step 2: Validate resources available
        if is_resources_sufficient(drink["ingredients"]):
            # Step 3: Collect payment
            payment = process_coins()
            # Step 4: Validate payment sufficient AND update global money
            if is_transaction_successful(payment, drink['cost']):
                # Step 5: Execute only if all prior steps passed
                make_coffee(order, drink["ingredients"])
