# Python typing: Type hints and arrows ->

# You can pre-set a data type:
age: int
name: str
height: float
is_human: bool


# Can also type hint w/int a function
# use -> to indicate expected return data type:
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "this isn't a bool :-)"

print(police_check(12))

# now if you input a non-int value - you'll get warned in the IDE (but you'll still be able to run & crash):
print(police_check("twelve"))



