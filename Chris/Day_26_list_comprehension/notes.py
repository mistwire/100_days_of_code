# For Loop version:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List comprehension version:
new_list2 = [n + 1 for n in numbers]
print(new_list2)

name = "Angela"
new_list3 = [letter for letter in name]
print(new_list3)

# works on any iterable

new_list4 = [x*2 for x in range(1, 5)]
print(new_list4)

# Conditional List Comprehension:
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# get list of names with 4 or fewer letters
short_names = [name for name in names if len(name) < 5]
print(short_names)

# uppercase all names with 5 or more letters
long_names_upper = [x.upper() for x in names if len(x) > 5]
print(long_names_upper)

# 233 coding exercise
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [i**2 for i in numbers]
print(squared_numbers)

# 234 coding exercise
result = [x for x in numbers if x % 2 == 0]
print(result)

# 235 coding exercise







