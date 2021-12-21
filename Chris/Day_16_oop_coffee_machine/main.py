from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}:")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(user_choice)
        # print(drink.cost)
        # print(drink.ingredients)
        # print(drink.name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print(f"Sorry, that wasn't enough money for your {user_choice}")


