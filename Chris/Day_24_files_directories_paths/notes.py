
# How to access a file in python
file_path = 'C:/Users/chris/Desktop/my_file.txt'

file = open(file_path)
# read the file and save in contents variable:
contents = file.read()
print(contents)
# Then need to close file:
file.close()

# This is the better way to open/close files. The with operator auto-closes after use:
with open(file_path) as file:
    contents = file.read()
    print(contents)

# How to write to file:
with open(file_path, mode="w") as f:
    f.write("My new text here")

# How to append to a file:
with open(file_path, mode="a") as f:
    f.write("\nAppended text here")

with open(file_path, mode="w") as f:
    f.write("Text for newly created file")
