# PATTERN: Financial manager. Handles payment collection and profit tracking.
# Compare with Day 15: global money + global in is_transaction_successful() vs. here: self.profit
class MoneyMachine:
    # KEY CONCEPT: Class variables (shared by all instances). Configuration constants.
    # Change CURRENCY here, and all instances use the new value (vs. Day 15's hardcoded "$")
    CURRENCY = "$"

    # PATTERN: Class variable for configuration. COIN_VALUES is shared; methods access it.
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # KEY CONCEPT: Instance variables (unique per object).
        # self.profit tracks revenue for THIS machine (independent if multiple machines exist)
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        # Uses self.CURRENCY (class variable) and self.profit (instance variable)
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        # PATTERN: Helper method. Used internally by make_payment().
        # Iterates COIN_VALUES (class variable) to ask for each coin type.
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        # PATTERN: Core transaction logic. Updates instance state based on payment outcome.
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            # KEY CONCEPT: State update on successful transaction. Compare with Day 15's global keyword.
            # Here: self.profit += cost (clean). Day 15: global money; money += cost_of_drink (awkward)
            self.profit += cost
            # CRITICAL FIX from Day 15: self.money_received is reset ONLY on success.
            # Day 15 had no automatic reset, leading to coins carrying over between transactions.
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            # Reset on failure too, ensuring clean state for next transaction.
            self.money_received = 0
            return False

