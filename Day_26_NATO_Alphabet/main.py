import pandas

# =================================================================
# 1. DICTIONARY ITERATION (Traditional Loop)
# =================================================================
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# PATTERN: Loop through dict using .items() to get key AND value
for (key, value) in student_dict.items():
    # Access both key and value in each iteration
    pass


# =================================================================
# 2. DATAFRAME ITERATION WITH iterrows()
# =================================================================
student_data_frame = pandas.DataFrame(student_dict)

# PATTERN: iterrows() yields (index, row) tuples
# row is a Series with column names as attributes
for (index, row) in student_data_frame.iterrows():
    # Access row data: row.student, row.score
    # index is the row number (0, 1, 2, ...)
    pass

# =================================================================
# 3. DICTIONARY COMPREHENSION WITH iterrows()
# =================================================================
# This is the key pattern for converting CSV/DataFrame to dictionary!
# {new_key: new_value for (index, row) in df.iterrows()}

# Read NATO alphabet mapping (letter → code word)
df = pandas.read_csv("nato_alphabet.csv")
# CSV format: letter,code
#             A,Alfa
#             B,Bravo
#             ...

# KEY CONCEPT: Dictionary comprehension - create dict from DataFrame
# Pattern: {row.column1: row.column2 for index, row in df.iterrows()}
# This replaces manual loop that appends to dict
nato_dict = {r.letter: r.code for i, r in df.iterrows()}
# Result: {"A": "Alfa", "B": "Bravo", "C": "Charlie", ...}

# =================================================================
# 4. LIST COMPREHENSION - TRANSFORM USER INPUT
# =================================================================
user_input = input("Enter word to nato-ify: ").upper()

# PATTERN: List comprehension - iterate over string characters
# For each letter in user input, look up phonetic code in nato_dict
response = [nato_dict[i] for i in user_input]
# Example: input "cat" → ["Charlie", "Alfa", "Tango"]

print(response)