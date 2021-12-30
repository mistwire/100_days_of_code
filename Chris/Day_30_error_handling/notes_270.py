# # FileNotFoundError:
# with open("a_file.txt") as file:
#     file.read()

# # KeyError:
# a_dict = {'key': 'value'}
# value = a_dict["non_existent_key"]

# # IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# # TypeError:
# text = 'abc'
# print(text + 5)

try:
    file = open("a_file.txt")
    a_dict = {'key': 'value'}
    print(a_dict["key"])

except FileNotFoundError:
    # Do this if the try fails:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"they key {error_message} does not exist")

else:
    # Do this when the try succeeds
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")

