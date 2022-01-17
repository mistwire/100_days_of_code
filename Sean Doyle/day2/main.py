#!/usr/bin/env python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import logging


def main():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    cash_register = MoneyMachine()

    def prompt():
        while True:
            choice = input("What type of coffee would you like? ")
            choice = choice.lower().strip()
            if choice == "off":
                print("Switching off! *Beep Boop Beep*")
                exit(1)
            elif choice == "report":
                print(coffee_maker.report())
            elif menu.find_drink(choice):
                break
            else:
                print(f"Please select from the following items {menu.get_items()}")
        return menu.find_drink(choice)

    while True:
        choice = prompt()
        logger.debug(choice.name)
        choice_details = menu.find_drink(choice.name)
        logger.debug(choice_details)
        if not coffee_maker.is_resource_sufficient(choice_details):
            continue
        else:
            choice_cost_formatted = "${:,.2f}".format(choice_details.cost)
            print(f"Getting beverage {choice}.  Total cost is: {choice_cost_formatted}")
            if cash_register.make_payment(choice_details.cost):
                coffee_maker.make_coffee(choice_details)


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        level=logging.DEBUG, format="%(levelname)s_%(asctime)s - %(message)s"
    )
    main()
