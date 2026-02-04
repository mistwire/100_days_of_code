# PATTERN: OOP Separation of Concerns. Each import represents a distinct responsibility domain.
# Compare with Day 15 where all logic was in this single file.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# KEY CONCEPT: Instance creation instead of global state.
# Each object encapsulates its own state (inventory, profit, menu data).
# Compare: Day 15 used global resources, money; here we have independent instances.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# PATTERN: Main loop is now clean and minimal—orchestrates objects without direct state manipulation.
# This is the benefit of OOP: complexity hidden in classes, coordinator code is simple.
is_on = True

while is_on:
    # Delegation: ask the Menu object for available items (encapsulation - we don't access menu.menu directly)
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        # Each object reports its own state through dedicated methods.
        # Day 15 had one print statement; here each class manages its output.
        coffee_maker.report()
        money_machine.report()
    else:
        # KEY CONCEPT: Data flow. Objects communicate via method return values and parameters.
        # drink is now a MenuItem object (Day 15: nested dict), passed between subsystems.
        drink = menu.find_drink(choice)
        # Validation chain: resources → payment → execution (same as Day 15, but now encapsulated)
        if coffee_maker.is_resource_sufficient(drink):
            # MoneyMachine handles its own state (profit += cost, money_received = 0)
            # Day 15 required global keyword; here self does it naturally.
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
