import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.pendown()

side_length = 100


for num_sides in range(3, 11):
    timmy.home()
    for shape in range(num_sides):
        timmy.forward(side_length)
        timmy.right(
            360/num_sides
        )
        # ref: timmy.right(180 - (900/7))


new_screen = t.Screen()
new_screen.exitonclick()
