# Day 9: Silent Auction - Dictionaries & Nested Data Structures

## What You Learned
Today you learned to use dictionaries as the primary data structure for storing and querying related data. Unlike lists (index-based), dictionaries use meaningful keys to organize information. You also discovered how dictionaries can contain lists, and lists can contain dictionaries—creating flexible nested structures.

---

## Key Concepts

### 1. Dictionaries vs Lists
Dictionaries store key-value pairs; lists store by index:

```python
# LIST: Access by position (0, 1, 2...)
names = ["Alice", "Bob", "Charlie"]
print(names[0])  # "Alice" - but what does index 0 mean?

# DICTIONARY: Access by meaningful key
bids = {"Alice": 100, "Bob": 150, "Charlie": 120}
print(bids["Alice"])  # 100 - clear what "Alice" refers to
```

### 2. Dictionary Creation and Modification
```python
# Create empty dict
bids = {}

# Add entries (creating or updating)
bids["Alice"] = 100
bids["Bob"] = 150

# Update existing
bids["Alice"] = 110  # overwrites 100

# Access
print(bids["Alice"])  # 110

# Check if key exists
if "Charlie" in bids:
    print(bids["Charlie"])
```

### 3. Iterating Through Dictionaries
Three ways to loop:
```python
bids = {"Alice": 100, "Bob": 150}

# Method 1: Loop through keys (most common)
for bidder in bids:
    print(bidder, bids[bidder])  # "Alice 100", "Bob 150"

# Method 2: Loop through values only
for amount in bids.values():
    print(amount)  # 100, 150

# Method 3: Loop through key-value pairs
for bidder, amount in bids.items():
    print(bidder, amount)  # "Alice 100", "Bob 150"
```

### 4. Finding Maximum Values
Common task: find the highest bid and who made it.

```python
bids = {"Alice": 100, "Bob": 150, "Charlie": 120}

# Find highest value
highest = max(bids.values())  # 150

# Find who bid it: must loop and match
for bidder in bids:
    if bids[bidder] == highest:
        winner = bidder

# OR use a helper function (from the code)
def get_key(val):
    for key, value in bids.items():
        if value == val:
            return key
```

### 5. Nested Data Structures: Lists in Dictionaries
```python
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]  # LIST inside DICT
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg"]
    }
]

# Access nested data
print(travel_log[0]["cities"][1])  # "Lille"
#      ↑ list index  ↑ dict key   ↑ list index
```

**Order of operations for nested access:**
1. `travel_log[0]` → get first dict: `{"country": "France", ...}`
2. `["cities"]` → get the cities key: `["Paris", "Lille", "Dijon"]`
3. `[1]` → get second city: `"Lille"`

### 6. Transforming Data with Dictionaries
Convert one dict to another with conditional logic:
```python
# Input: scores -> Output: grades
student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99}
student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    else:
        student_grades[name] = "Fail"

print(student_grades)
# {"Harry": "Exceeds Expectations", "Ron": "Fail", "Hermione": "Outstanding"}
```

---

## Common Pitfalls

- **KeyError on access:** Accessing a key that doesn't exist crashes the program. Use `if key in dict:` first or use `.get()` method.
- **Confusing list/dict iteration:** `for x in dict` gives keys, not values. Use `for x in dict.values()` for values.
- **Nested access order:** `travel_log[0]["cities"][1]` is correct; `travel_log["cities"][0][1]` will crash.
- **Forgetting to build the result dict:** When transforming, create new dict first: `result = {}`
- **Using lists when dicts are better:** If you have meaningful keys, don't use numeric indices.
- **Duplicate keys overwriting:** Last assignment to a key wins. `{"a": 1, "a": 2}` has only `"a": 2`.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 5** | Iteration over sequences (now with dict keys/values) |
| **Day 7** | Finding max/min in data structures (similar to finding highest bid) |
| **Day 8** | String operations (keys are often strings) |
| **Day 15-16** | Coffee Machine project heavily uses nested dictionaries |
| **Day 20+** | OOP uses dictionaries to store object attributes |

---

## Before You Move On
Make sure you can:
- [ ] Create a dictionary and add/update entries
- [ ] Loop through a dictionary and access both keys and values
- [ ] Explain the difference between `for k in dict` vs `for k in dict.values()`
- [ ] Access nested data: `list_of_dicts[0]["key"][1]`
- [ ] Find the maximum value in a dictionary (and the key associated with it)
- [ ] Transform one dictionary into another using a loop

---

## Practice Prompt
**Enhancement Challenge:**
1. Create a `students` dictionary that tracks both scores AND grades:
   ```python
   students = {
       "Harry": {"score": 81, "grade": "Exceeds Expectations"},
       "Hermione": {"score": 99, "grade": "Outstanding"}
   }
   ```
2. Add function to calculate average score across all students
3. Add function to find all students with a specific grade
4. Bid tracking: if the same person bids twice, overwrite their bid (already happens!)
5. Prevent the same person from bidding multiple times in the auction

**Bonus:** Create a `grade_book` system that stores students, their assignments, and scores:
```python
grade_book = {
    "Harry": {
        "Math": [81, 85, 79],
        "English": [88, 92]
    },
    "Hermione": {
        "Math": [99, 100],
        "English": [97, 96]
    }
}
```
Then calculate average per subject per student.

**Bonus 2:** Implement the silent auction in reverse: instead of dict_name -> bid, use dict_bid -> list_of_names (multiple people can bid the same amount). How would winner selection change?
