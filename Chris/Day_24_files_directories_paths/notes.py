
# How to access a file in python
file = open("my_file.txt")
# read the file and save in contents variable:
contents = file.read()
print(contents)
# Then need to close file:
file.close()

# This is the better way to open/close files. The with operator auto-closes after use:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# How to write to file:
with open("my_file.txt", mode="w") as f:
    f.write("My new text here")

# How to append to a file:
with open("my_file.txt", mode="a") as f:
    f.write("\nAppended text here")

with open("new_file.txt", mode="w") as f:
    f.write("Text for newly created file")
