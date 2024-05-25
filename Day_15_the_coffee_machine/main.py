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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
coffee_is_on = True

def is_resources_sufficient(order_ingredients):
    """Determines if there are enough resources to make the drink order"""
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
        global money
        money += cost_of_drink

        return True
    else: 
        print("You have not put in enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Remove the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")



while coffee_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if order == 'off':
        coffee_is_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: $ {money}")
    else:
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(order, drink["ingredients"])
