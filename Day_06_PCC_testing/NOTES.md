# Day 6: Testing with pytest

## What You Learned

This day introduces **automated testing** using `pytest` -- writing code that verifies your other code works correctly. You test both standalone functions and class methods, and learn how **fixtures** eliminate repetitive setup.

---

## Key Concepts

### 1. Why Test?
Manual testing (running `names.py` and typing inputs) is slow and error-prone. Automated tests run in seconds and catch regressions -- bugs introduced when you change existing code. The `test_name_function.py` and `test_survey.py` files are your safety net.

### 2. Test Functions with `assert`
A test is just a function whose name starts with `test_`. Inside, you call the code under test and use `assert` to check the result:

```python
from name_function import get_formatted_name

def test_first_last_name():
    """Does 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

- `assert` does nothing if the expression is `True` -- the test passes silently
- `assert` raises `AssertionError` if `False` -- pytest catches this and reports a failure
- Each test should verify **one behavior** (single responsibility)

### 3. Testing Functions with Optional Parameters
`get_formatted_name` has an optional `middle` parameter with a default of `''`. Two tests cover both paths:

```python
def test_first_last_name():          # Tests the default path (no middle name)
def test_first_last_middle_name():   # Tests the optional parameter path
```

This pattern -- testing both the default and non-default paths -- applies whenever a function has optional parameters.

### 4. Testing Classes
`AnonymousSurvey` (in `survey.py`) is a class with state (`self.responses`). Testing classes means:
1. Creating an instance
2. Calling methods on it
3. Asserting the instance's state changed correctly

```python
def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```

### 5. Fixtures (`@pytest.fixture`)
When multiple tests need the same setup (creating an `AnonymousSurvey`), a **fixture** avoids repeating that code:

```python
@pytest.fixture
def language_survey():
    """A survey that is available for all tests"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey
```

- The fixture function name becomes a parameter in each test function
- pytest automatically calls the fixture and passes the result to the test
- Each test gets a **fresh** instance -- tests don't contaminate each other

### 6. Separation of Concerns in File Layout
The project separates code into clear roles:

| File | Role |
|------|------|
| `name_function.py` | The function being tested |
| `names.py` | Interactive script that uses the function |
| `test_name_function.py` | Automated tests for the function |
| `survey.py` | The class being tested |
| `language_survey.py` | Interactive script that uses the class |
| `test_survey.py` | Automated tests for the class |

This pattern -- keeping testable logic separate from I/O (input/print) -- is fundamental to writing testable code.

---

## Common Pitfalls

- **Forgetting the `test_` prefix**: pytest only discovers functions that start with `test_`. Name it `check_first_last()` and pytest will silently ignore it.
- **Testing too many things in one test**: If a test checks three different behaviors and fails, you won't know which one broke. Keep tests focused.
- **Not testing edge cases**: `get_formatted_name` is tested with and without a middle name. What about empty strings? Single characters? Always think about boundary conditions.
- **Fixture confusion**: The fixture function name must match the parameter name in the test exactly. `def language_survey()` fixture feeds `def test_store_single_response(language_survey)`.
- **Mutating shared state**: Without fixtures, if one test modifies a shared object, the next test sees those changes. Fixtures prevent this by creating fresh instances.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 1** | `AnonymousSurvey` uses the same OOP patterns (classes, `__init__`, `self`) you learned there |
| **Day 2** | `try/except` from Day 2 handles runtime errors; tests catch logic errors *before* runtime |
| **Day 10** | Functions with return values (like `get_formatted_name`) are the easiest to test -- you call them and check the output |
| **Day 15-16** | The Coffee Machine project could benefit from tests -- especially when refactoring from procedural (Day 15) to OOP (Day 16) |
| **Day 34** | The Quiz Brain app combines OOP with APIs -- tests would verify the data model works independently of the GUI |

---

## Before You Move On

Make sure you can:

- [ ] Write a test function that uses `assert` to verify a return value
- [ ] Explain why test functions must start with `test_`
- [ ] Create a `@pytest.fixture` and use it as a parameter in multiple tests
- [ ] Explain why each test gets a fresh fixture instance (test isolation)
- [ ] Run `pytest` from the command line and interpret its output (dots for passes, F for failures)

---

## Practice Prompt

Write tests for a `ShoppingCart` class:
- The class should have `add_item(name, price)`, `remove_item(name)`, and `get_total()` methods
- Write a fixture that creates a cart with 3 items pre-loaded
- Test adding an item, removing an item, and calculating the total
- Test edge cases: removing an item that doesn't exist, getting the total of an empty cart
