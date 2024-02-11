# How to create a class
# Python classes are done in PascalCase 
# Attributes - what a class HAS (values)
# Methods - what a class DOES (functions)
# Constructor - what should happen when an object is being constructed: starting values 

class User:
    # it's convention that the name of the parameter == the name of the attribute (but they don't have to be the same)
    def __init__(self, user_id, username) -> None:
        print("new user being created") 
        self.id = user_id
        self.username = username
        # can set default values as well:
        self.followers = 0
        self.following = 0

    # a method always start with a self parameter:
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "chris")
print(user_1.username)
print(user_1.id)

# you can 'make' new attributes on the fly
user_1.fizz = "buzz"
print(user_1.fizz)



