# Day 1: Object-Oriented Programming (OOP) Basics

## What You Learned

This day introduces the core building blocks of OOP in Python: **classes**, **attributes**, **methods**, **inheritance**, and **composition**. These patterns are the foundation for nearly every Python project beyond simple scripts.

---

## Key Concepts

### 1. Classes and Instances
A **class** is a blueprint. An **instance** is a specific object built from that blueprint.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

my_dog = Dog("Mephistopheles", 6)  # instance
```

- `__init__` runs automatically when you create an instance
- `self` refers to the specific instance being created -- it's how each object keeps track of its own data
- Every method in a class must have `self` as its first parameter

### 2. Attributes: Passed vs Default
- **Passed attributes** come from arguments: `self.make = make`
- **Default attributes** are set inside `__init__` without arguments: `self.odometer_reading = 0`

### 3. Modifying Attributes
Three ways to change an attribute:
1. **Directly**: `my_car.odometer_reading = 23` (simple but no validation)
2. **Through a method**: `my_car.update_odometer(24)` (can add logic like preventing rollback)
3. **Incrementally**: `my_car.increment_odometer(100)` (adds to current value)

Using methods to modify attributes is preferred because you can add validation logic (like the odometer rollback check).

### 4. Inheritance
A child class inherits all attributes and methods from its parent:

```python
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # call parent's __init__
        self.battery = Battery()             # add new attribute
```

- `super()` gives access to the parent class
- Child classes can **override** parent methods (like `fill_gas_tank`)
- Child classes can **add** new attributes and methods

### 5. Composition (Instances as Attributes)
Instead of cramming everything into one class, you can use another class as an attribute:

```python
self.battery = Battery()  # Battery is its own class, stored as an attribute
```

Access it with chained dot notation: `my_id4.battery.describe_battery()`

### 6. Importing Classes
Two styles, each with trade-offs:

```python
from car import Car          # import specific class -- use as Car()
import car                   # import whole module -- use as car.Car()
```

The `from X import Y` style is cleaner when you only need one or two classes. The `import X` style avoids name collisions and makes it clear where each class comes from.

---

## Common Pitfalls

- **Forgetting `self`**: Every method needs `self` as its first parameter. Without it, Python won't know which instance to operate on.
- **Forgetting `super().__init__()`**: If your child class has `__init__`, you must call the parent's `__init__` or the parent's attributes won't be set.
- **Modifying attributes directly when validation matters**: Direct modification (`obj.attr = value`) skips any logic you've built into setter methods.
- **Circular imports**: In `electric_car.py`, `Battery` is defined after `ElectricCar` uses it. In Python, the class must be defined before it's referenced. Order matters within a file.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 2** | `pathlib.Path` is a class from Python's standard library -- you're already using OOP when you call `path.read_text()` |
| **Day 6** | You'll write `pytest` tests for classes like these |
| **Day 16** | The OOP Coffee Machine rebuilds Day 15's procedural code using classes -- a direct comparison of procedural vs OOP |
| **Days 20-23** | Games (Snake, Pong, Turtle Crossing) are built with multiple classes that interact, just like `Car` and `Battery` |
| **Day 34** | The Quiz Brain app combines OOP with a GUI -- classes managing data while Tkinter handles display |

---

## Before You Move On

Make sure you can:

- [ ] Create a class with `__init__`, attributes, and methods from scratch (without looking at examples)
- [ ] Explain what `self` is and why it's needed
- [ ] Create a child class that inherits from a parent and adds new functionality
- [ ] Explain the difference between modifying an attribute directly vs through a method
- [ ] Import a class from another file using both import styles

---

## Practice Prompt

Try building a `Library` system:
- A `Book` class with title, author, and `is_checked_out` (default `False`)
- A `Library` class that holds a list of `Book` instances
- Methods to `add_book()`, `check_out(title)`, and `return_book(title)`
- A `DigitalLibrary` child class that overrides `check_out` to allow unlimited copies
