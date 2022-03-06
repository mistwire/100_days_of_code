import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.pendown()

side_length = 100
colors = ["purple","lime green","red","yellow","pink"]

for num_sides in range(3, 11):
    timmy.home()
    timmy.color(random.choice(colors))
    for shape in range(num_sides):
        
        timmy.forward(side_length)
        timmy.right(
            360/num_sides
        )
        # ref: timmy.right(180 - (900/7))


new_screen = t.Screen()
new_screen.exitonclick()
