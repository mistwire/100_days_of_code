# with open("./my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="a") as file:
    file.write("\nNew text goes here.")


with open("new_file.txt", mode="w") as file:
    file.write("Makes a new file if the file doesn't exist")