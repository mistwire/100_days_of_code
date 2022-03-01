import turtle
import turtle as t
import random

turtle.screensize(250, 250)
turtle.setworldcoordinates(-10, -10, 500, 500)
turtle.speed('fastest')
turtle.colormode(255)

timmy = t.Turtle()
timmy_position = list(timmy.position())

spot_cols = 10
spot_rows = 10
spot_distance = 50
spot_size = 20

colors = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12)]

print(timmy.position())


for _ in range(spot_rows):
    for _ in range(spot_cols):
        # timmy.color(random.choice(colors))
        timmy.pendown()
        timmy.dot(spot_size, random.choice(colors))
        timmy.penup()
        timmy.forward(spot_distance)
    timmy_position[0] = 0
    timmy_position[1] += spot_distance
    timmy.setposition(timmy_position[0],timmy_position[1])


new_screen = t.Screen()
new_screen.exitonclick()