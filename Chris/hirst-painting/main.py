# import colorgram
# colors = colorgram.extract('image.jpg', 13)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     color_list.append(rgb_color)
#
# print(color_list)
import random
import turtle

color_list = [(237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29)]

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(0)
tim.penup()
turtle.colormode(255)
tim.hideturtle()

for i in range(10):
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)
        x, y = tim.position()
    tim.setpos(0.00, y + 50)
    print(f"x is {x}, y is {y}")

screen = turtle.Screen()
screen.exitonclick()
