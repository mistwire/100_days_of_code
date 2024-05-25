import pandas

student_dict = {
    "student": ["Angela", "James", "Lily", "Chris"],
    "score": [45, 65, 94, 100]
}

for k, v in student_dict.items():
    print(f"the key is {k}")
    print(f"the value is {v}")

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through the df (not valuable)
for (k, v) in student_df.items():
    print(f"the key is {k}")
    print(f"the value is {v}")


# Use iterrows to get data out of df:
for (k, v) in student_df.iterrows():
    print(f"the key is {k}")
    print(f"the value is {v.student}")
    print(f"the value is {v.score}")

