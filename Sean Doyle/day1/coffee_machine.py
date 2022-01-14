#!/usr/bin/env python3
import logging

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# DONE Prompt User for coffee selection
# DONE Turn off coffee machine by entering off
# DONE Print Report
# DONE Check if enough resources
# DONE Process money
# TODO Check if Transaction successful
# TODO Make Coffee


def prompt():
    """
    Prompts user for choice.  Can select from three coffee choices and exit if necessary

    :return: choice (string)
    """
    choices = ["espresso", "latte", "cappuccino", "off", "report"]
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino) ")
        if choice.lower() not in choices:
            logger.warning(f"{choice} is not a valid choice, please try again")
        else:
            return choice


def check_resources(drink):
    resources_needed = MENU.get(
        drink,
    ).get("ingredients")
    cost = MENU.get(
        drink,
    ).get("cost")
    return resources_needed, cost


def validate_resources(resources_needed):
    for k in resources_needed.keys():
        if resources_needed[k] > resources[k]:
            return k
    return None


def process_money(cost):
    cost_f = "${:,.2f}".format(cost)
    total = 0.0
    coin_values = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def switch(coin_type):
        return coin_values.get(coin_type, 0)

    print(f"Total cost is {cost_f}")
    quarters = input(f"Please enter amount of quarters: ")
    dimes = input("Please enter amount of dimes: ")
    nickles = input("Please enter amount of nickels: ")
    pennies = input("Please enter amount of pennies: ")
    if not quarters:
        quarters = 0
    if not dimes:
        dimes = 0
    if not nickles:
        nickles = 0
    if not pennies:
        pennies = 0

    total = (
        float(quarters) * switch("quarters")
        + float(dimes) * switch("dimes")
        + float(nickles) * switch("nickles")
        + float(pennies) * switch("pennies")
    )
    if cost - total > 0:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        if total - cost != 0:
            refund = "${:,.2f}".format(total - cost)
            print(f"Here is {refund} in change")

        resources["money"] = resources.get("money", 0) + cost
        return True


def get_beverage(drink):
    drink_resources, _ = check_resources(drink)
    for k in drink_resources.keys():
        resources[k] = resources[k] - drink_resources[k]
    print(f"Here is your {drink}!")


def main():
    while True:
        choice = prompt()
        logger.debug(choice)
        if choice == "off":
            print("Switching off! *Beep Boop Beep*")
            exit(1)
        elif choice == "report":
            [print(key, ":", value) for key, value in resources.items()]
        else:
            resources_required, cost = check_resources(choice)
            resource_out = validate_resources(resources_required)
            if resource_out:
                print(f"Sorry there is not enough {resource_out}")
            else:
                logger.debug(f"Getting beverage {choice}")
                if process_money(cost):
                    get_beverage(choice)


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        level=logging.DEBUG, format="%(levelname)s_%(asctime)s - %(message)s"
    )
    main()
