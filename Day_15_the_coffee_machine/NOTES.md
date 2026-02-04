# Day 15: Coffee Machine (Procedural Approach)

## What You Learned
This project teaches procedural programming and transaction logic using nested dictionaries to model a coffee machine. You'll understand how global state, resource management, and multi-step workflows can be built without OOP.

---

## Key Concepts
### 1. Nested Dictionaries for Data Structure
Nested dictionaries organize complex data hierarchically. The MENU structure stores recipes and prices, while each drink has its own ingredient requirements:

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    # ... more drinks
}
```
This structure mirrors real-world relationships: each drink has associated metadata (cost and ingredients) organized together.

### 2. Resource Management & State
The `resources` dictionary tracks inventory, and functions modify this shared state:
```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```
Checking resource sufficiency requires comparing requested amounts against available inventory—a validation pattern seen throughout the project.

### 3. Transaction Logic (Multi-Step Process)
A successful transaction requires multiple sequential checks:
1. Check if resources are sufficient (`is_resources_sufficient()`)
2. Collect payment (`process_coins()`)
3. Validate payment is sufficient (`is_transaction_successful()`)
4. Deduct resources and confirm order (`make_coffee()`)

This sequential validation prevents invalid states (e.g., giving free coffee if payment fails).

### 4. Global State with `global` Keyword
The function modifies global `money` using the `global` keyword:
```python
global money
money += cost_of_drink
```
This allows functions to modify outer scope variables. Day 16 eliminates this complexity by encapsulating state within objects.

### 5. User Interface Loop & State Machine
The main loop (`while coffee_is_on`) is a state machine handling three types of inputs:
- `'off'`: Stop the machine
- `'report'`: Display current state
- Drink name: Initiate transaction

This pattern appears in many interactive programs.

---

## Common Pitfalls
- **Off-by-one in resource comparison**: The condition `order_ingredients[item] >= resources[item]` prevents making coffee when an exact amount is available (should be `>`). Day 16 fixes this.
- **Global state mutations**: Using `global money` makes code harder to test and reason about. Encapsulation in Day 16 is cleaner.
- **Incomplete input validation**: Doesn't handle invalid drink names (will crash with KeyError if user enters undefined drink).
- **Money doesn't reset**: `process_coins()` doesn't reset `money_received` after a transaction, causing potential issues across multiple transactions.

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Uses OOP concepts Day 1 introduces, but applies procedural approach instead |
| **Day 5** | Uses `random` module (implicit in color choices if extended) |
| **Day 9** | Dictionary iteration and nested structure access patterns |
| **Day 14** | Game data structures similar to this MENU/resources approach |
| **Day 16** | OOP refactor of this exact project—compare the architecture differences |
| **Day 27-28** | Tkinter GUIs will build similar state management patterns |

---

## Before You Move On
Make sure you can:
- [ ] Understand nested dictionary structure and access patterns (`dict[key1][key2]`)
- [ ] Explain why multiple sequential checks prevent invalid states
- [ ] Identify limitations of global variables and procedural state management
- [ ] Trace through a full transaction: resource check → payment → completion
- [ ] Predict what would happen if you removed the `is_resources_sufficient()` check

---

## Practice Prompt
**Mini-Project: Vending Machine for Snacks**
Create a snack vending machine using the same procedural approach:
- Define a MENU with snacks (chips, candy, soda) including prices and inventory
- Track inventory and money separately
- Allow users to:
  - View available snacks (with prices)
  - Purchase snacks (with change calculation)
  - Restock inventory (admin function)
  - Exit
- Add a report function that shows current inventory and total revenue

Constraints: Keep everything procedural (no classes). Use nested dictionaries for menu data.

**Challenge Extension**: What problems appear when you run low on inventory? How would you handle preventing overselling? (Hint: This is why Day 16's refactor exists.)
