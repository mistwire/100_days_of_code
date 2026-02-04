# Day 16: OOP Coffee Machine (Refactor)

## What You Learned
This is an Object-Oriented refactor of Day 15's procedural coffee machine. You'll learn **separation of concerns** through multiple classes, each responsible for a specific domain. This is your first major multi-class project demonstrating how OOP eliminates global state problems.

---

## Key Concepts
### 1. Separation of Concerns (Single Responsibility Principle)
Each class handles one responsibility:
- **`MenuItem`**: Models a single drink (name, ingredients, cost)
- **`Menu`**: Manages the collection of available drinks
- **`CoffeeMaker`**: Handles resource management and drink preparation
- **`MoneyMachine`**: Handles payment processing and profit tracking

Compare Day 15's procedural approach (all logic in `main.py`) with this modular design.

### 2. Encapsulation & Instance Variables
Instead of global `resources` and `money`, each class encapsulates its own state:

```python
# CoffeeMaker
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

# MoneyMachine
class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.money_received = 0
```

Each object instance is independent—you could create multiple machines if needed. Day 15's globals prevent this.

### 3. Class Constants (Class Variables)
`MoneyMachine` uses class variables for configuration shared across instances:

```python
class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
```

This centralizes configuration. If you change `CURRENCY`, all instances benefit. Compare with Day 15's hardcoded values.

### 4. Data Model Class (MenuItem)
`MenuItem` is a simple data container:

```python
class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
```

This is a **data class**—it holds data without business logic. (Python 3.7+ has `@dataclass` decorator for this, but not used here.)

### 5. Collection Management (Menu Class)
`Menu` demonstrates managing a collection of objects:

```python
class Menu:
    def __init__(self):
        self.menu = [MenuItem(...), MenuItem(...), ...]

    def get_items(self):
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
```

Encapsulates the drink list and provides query methods. Day 15 used a simple dict; this is more scalable.

### 6. Stateful Methods with Side Effects
`MoneyMachine.make_payment()` updates internal state:

```python
def make_payment(self, cost):
    self.process_coins()
    if self.money_received >= cost:
        change = round(self.money_received - cost, 2)
        print(f"Here is ${change} in change.")
        self.profit += cost  # Update instance state
        self.money_received = 0  # Reset for next transaction
        return True
    else:
        self.money_received = 0
        return False
```

The key improvement: `self.money_received` automatically resets after each transaction, preventing bugs in Day 15.

### 7. Comparison: Procedural vs. OOP Architecture

| Aspect | Day 15 (Procedural) | Day 16 (OOP) |
|--------|-------------------|------------|
| State Storage | Global variables | Instance variables in classes |
| Resource Validation | `is_resources_sufficient()` function | `CoffeeMaker.is_resource_sufficient()` method |
| Payment Logic | `is_transaction_successful()` function | `MoneyMachine.make_payment()` method |
| Menu Structure | Nested dictionary | `Menu` class with `MenuItem` objects |
| Testability | Hard (global state affects tests) | Easy (create independent instances) |
| Extensibility | Add parameters to functions | Add methods to classes or subclasses |
| Money Tracking | Manual `global money` update | `self.profit` automatically managed |

---

## Common Pitfalls
- **Forgetting to reset transaction state**: `MoneyMachine.money_received = 0` must happen after each transaction, otherwise coins from failed attempts carry over (fixed compared to Day 15).
- **Accessing private attributes**: In `main.py`, we call `coffee_maker.resources` directly. Better practice would be `coffee_maker.report()` methods.
- **None return from `find_drink()`**: If a drink isn't found, `Menu.find_drink()` returns `None`, which would crash if accessed without checking. Day 15 would crash with KeyError; this is slightly better.
- **Class vs. Instance variables confusion**: `COIN_VALUES` is a class variable (shared by all instances), `money_received` is instance variable (unique per object).

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | OOP fundamentals applied here: classes, methods, constructors |
| **Day 15** | Direct predecessor—same functionality, different architecture |
| **Day 5** | `random` module (implicit if coin selection were randomized) |
| **Day 9** | Dictionary iteration within class methods |
| **Day 14** | Data structures now encapsulated in classes |
| **Day 17** | Quiz game uses similar multi-class architecture (QuizBrain, Question, Menu) |
| **Day 20-21** | Snake game builds on this OOP pattern |
| **Day 27** | Tkinter project uses GUI objects (similar encapsulation concept) |

---

## Before You Move On
Make sure you can:
- [ ] Explain why Day 16's `MenuItem` objects are better than Day 15's nested dict
- [ ] Trace how instances are created: `coffee_maker = CoffeeMaker()` vs. global state
- [ ] Identify what `self` refers to in each class method
- [ ] Explain the difference between class variables (`COIN_VALUES`) and instance variables (`self.profit`)
- [ ] Understand why `MoneyMachine.money_received = 0` prevents bugs compared to Day 15
- [ ] Compare `CoffeeMaker.report()` vs. Day 15's print statement in the main loop

---

## Practice Prompt
**Mini-Project: Bookstore Inventory System**
Refactor the Day 15 vending machine as an OOP design:

1. Create a `Book` class (title, author, price, quantity)
2. Create an `Inventory` class:
   - Manages collection of books
   - Provides `find_book(title)` and `get_available_books()` methods
   - `check_stock(title, quantity)` returns True/False
   - `sell_book(title, quantity)` deducts from inventory
3. Create a `CashRegister` class:
   - Tracks revenue (similar to `MoneyMachine.profit`)
   - `process_sale(amount)` accepts payment
   - `report()` shows total sales
4. Create `main.py` that uses these classes

Key requirements:
- No global variables
- Each class owns its data (encapsulation)
- `main.py` should be short and coordinate objects (like Day 16's main.py)
- Handle edge cases (book not found, insufficient stock, insufficient payment)

**Bonus Challenge**: Add a `Customer` class that tracks purchase history. Use composition: `customer = Customer(name)` then `customer.purchase_book(book)`.
