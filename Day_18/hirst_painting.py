import turtle
import random
# import colorgram 
# Extract 30 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#     make_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#     color_list.append(make_tuple)
# print(color_list)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for x in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    x = tim.pos()[0]
    y = tim.pos()[1]
    tim.setpos(x - 500, y + 50)

screen = turtle.Screen()
screen.exitonclick()