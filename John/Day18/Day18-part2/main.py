import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")


for _ in range(15):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)

screen = t.Screen()
screen.exitonclick()