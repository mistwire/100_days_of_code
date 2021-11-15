# import another_module
# print(another_module.another_variable)
# from turtle import *
# terry = Turtle()
# print(terry)
# terry.shape("turtle")
# terry.color("CornflowerBlue")
# terry.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

print(table)

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

table.align = "l"

print(table)