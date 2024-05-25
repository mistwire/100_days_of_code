# try:
#     file = open("a_file.txt")
#     a_dict = {'key': 'value'}
#     print(a_dict["key"])
#
# except FileNotFoundError:
#     # Do this if the try fails:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print(f"they key {error_message} does not exist")
#
# else:
#     # Do this when the try succeeds
#     content = file.read()
#     print(content)
#
# finally:
#     raise KeyError("This is an error I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / (height * height)
print(bmi)


