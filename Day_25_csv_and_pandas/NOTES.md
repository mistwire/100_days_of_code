# Day 25: CSV and Pandas - Data Analysis

## What You Learned
Data manipulation with pandas DataFrames: reading CSV files, selecting data with conditional filtering, computing statistics, and converting data between formats. This day transforms file I/O (Day 2/24) from text-based to data-structure-based thinking.

---

## Key Concepts

### 1. Pandas DataFrame as Data Container
A DataFrame is like an in-memory spreadsheet with powerful querying:

```python
import pandas

# Read CSV file into DataFrame
data = pandas.read_csv("weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>

# Access single column (returns Series - 1D array)
print(data["temp"])       # Series: [20, 15, 18, ...]
print(type(data["temp"])) # <class 'pandas.core.series.Series'>

# Access alternate syntax (column name becomes attribute)
print(data.condition)     # Same as data["condition"]
print(data.condition[3])  # Get specific row from column
```

**Why DataFrames?** Automatic parsing, column indexing, statistical methods all built-in.

### 2. Filtering Data with Boolean Conditions
Select rows matching criteria using boolean conditions:

```python
# Get row where day == "Monday"
monday_data = data[data["day"] == "Monday"]
print(monday_data)  # Returns DataFrame with matching rows

# Get row with highest temperature
hottest = data[data.temp == data.temp.max()]
print(hottest)

# Extract single value from filtered result
monday_temp = monday_data.temp.item()  # Single scalar value
```

**Key pattern:** `data[data.column == value]` returns a filtered DataFrame.

### 3. Statistical Methods on Series
One-line statistics replacing manual sum/len/max logic:

```python
temperatures = data["temp"]

# Manual way (Day 2/10 style)
avg_temp = sum(temperatures) / len(temperatures)

# Pandas way (one method call)
avg_temp = data["temp"].mean()
max_temp = data["temp"].max()
min_temp = data["temp"].min()
count = data["temp"].count()
```

### 4. Data Type Conversions
Transform between formats for different purposes:

```python
# DataFrame → Dictionary (for file I/O)
data_dict = data.to_dict()

# Series → List (for iteration)
temp_list = data["temp"].to_list()

# Dictionary/List → DataFrame (create from scratch)
new_data = pandas.DataFrame({
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
})

# DataFrame → CSV file (save output)
new_data.to_csv("output.csv")
```

### 5. Value Counting and Aggregation
Analyze categorical data with built-in counting:

```python
# US Squirrel Census example: count fur colors
fur_colors = data["Primary Fur Color"].value_counts()
print(fur_colors)
# Output:
# Gray      3427
# Black     2337
# Cinnamon  392

# Convert to DataFrame and save
df = pandas.DataFrame({
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [fur_colors["Gray"], fur_colors["Black"], fur_colors["Cinnamon"]]
})
df.to_csv("squirrel_count.csv")

# One-liner shortcut
data["Primary Fur Color"].value_counts().to_csv("squirrel_count.csv")
```

### 6. Pandas Iteration: iterrows()
Loop through DataFrame rows, accessing both index and row data:

```python
for (index, row) in data.iterrows():
    print(index)        # Row index (0, 1, 2, ...)
    print(row.column)   # Access column like attribute
    print(row["column"]) # Also works with bracket notation
```

Used in Day 26 for converting CSV to dictionary comprehensions.

---

## Common Pitfalls
- **Forgetting to import pandas**: `import pandas` required
- **File not found**: Check working directory; use absolute paths if needed
- **Confusing DataFrame and Series**: DataFrame has multiple rows/columns; Series is 1D
- **Modifying read-only Series**: Create new Series/DataFrame instead of modifying in-place
- **Not filtering before statistics**: `data.temp.max()` works, but `data[data.temp > 20].mean()` filters first
- **CSV structure assumption**: `read_csv()` assumes first row is header; use `header=None` for data without headers

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 2** | File I/O basics; pandas handles CSV format automatically |
| **Day 4** | String operations; column names often need cleaning (`.str.strip()`) |
| **Day 5** | Random sampling with `.sample(n=10)` on DataFrames |
| **Day 24** | File paths and structured data storage |
| **Day 26** | Convert CSV to dict using `iterrows()` |
| **Day 27** | Display DataFrame data in Tkinter tables |
| **Day 33+** | APIs return JSON (similar to DataFrame structure) |

---

## Before You Move On
Make sure you can:
- [ ] Explain the difference between DataFrame and Series
- [ ] Write filtering conditions: `data[data.column > value]`
- [ ] Use at least 3 statistical methods: mean(), max(), min()
- [ ] Convert DataFrame to CSV and back
- [ ] Extract single values from filtered DataFrames using `.item()`
- [ ] Iterate through rows using `iterrows()`

---

## Practice Prompt
**Challenge: Temperature Analysis**
1. Read a CSV file with date/temperature/condition columns
2. Find the average temperature for each month
3. Create new DataFrame with months and their averages
4. Save to `monthly_averages.csv`
5. Filter and print: "Days above 25 degrees" (use boolean condition)
6. Find the day with the biggest temperature drop from previous day
7. Optional: Create visualization (matplotlib) showing temperature trend

This chains data filtering, aggregation, and file I/O into realistic data analysis workflow.
