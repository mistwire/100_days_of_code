import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed(10)
timmy.pendown()

walk_distance = 20
walk_turns = 100
walk_headings = [0, 90, 180, 270]
colors = ["red","orange","yellow","green","blue","violet"]

walk_count = 0

while walk_count < walk_turns:
    
    
    timmy.setheading(random.choice(walk_headings))
    timmy.color(random.choice(colors))
    timmy.forward(walk_distance)

    walk_count += 1



new_screen = t.Screen()
new_screen.exitonclick()