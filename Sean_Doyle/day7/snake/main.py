#!/usr/bin/env python3
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for pos in starting_pos:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()
