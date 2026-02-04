# KEY CONCEPT: Dictionary basics (commented reference)
# programming_dictionary = {
#     "Bug": "An error...",
#     "Function": "A piece of code...",
#     }
# Access by key: programming_dictionary["Bug"]
# Add new key: programming_dictionary["Loop"] = "value"
# Loop through: for key in programming_dictionary: print(key, programming_dictionary[key])

# PROBLEM: Transform raw scores into letter grades
# Input: Dictionary mapping names to numeric scores
# Output: Dictionary mapping names to letter grades
# Algorithm: Loop through scores, apply grading scale, build new dict

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# STEP 1: Create empty dictionary to hold results
student_grades = {}

# STEP 2: PATTERN - Transform one dictionary into another
# KEY CONCEPT: Iterate through source dict's keys to access values
# For each score, apply grading criteria and store result with same key
for key in student_scores:
    # ACCESS: Use key to get the score value
    score = student_scores[key]
    # CONDITIONAL: Apply grading scale (note: ranges are exclusive on upper end)
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)