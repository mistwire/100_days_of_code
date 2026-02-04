# PATTERN: Generative art that extracts colors from an image and uses them for painting.
import turtle
import random

# KEY CONCEPT: Colorgram library extracts dominant colors from images.
# Commented code shows the process:
# 1. import colorgram
# 2. Extract 30 most dominant colors from 'image.jpg'
# 3. Convert colorgram.Color objects to RGB tuples
# 4. Use in painting loop
# For this project, colors are pre-extracted to avoid external dependencies.
# import colorgram
# Extract 30 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#     make_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#     color_list.append(make_tuple)
# print(color_list)

# Pre-extracted color palette (from a Hirst painting photograph)
# These are RGB tuples (0-255 values for each channel)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

tim = turtle.Turtle()
# KEY CONCEPT: RGB color mode required to use (R, G, B) tuples instead of color names.
turtle.colormode(255)
# PATTERN: Performance optimization. Drawing many dots is slow; fastest mode skips animation.
tim.speed("fastest")
tim.hideturtle()  # Don't show the turtle itself, only the dots
tim.penup()  # Don't draw lines, only dots
# Initial positioning: start at upper-left corner of grid
tim.setheading(225)  # Face southwest to move to starting position
tim.forward(250)  # Move away from origin
tim.setheading(0)  # Face east (right) for painting rows

# PATTERN: Nested loops for 2D grid (10x10 dots)
for x in range(10):  # 10 rows
    for i in range(10):  # 10 dots per row
        # PATTERN: Draw colored dot using extracted palette
        tim.dot(20, random.choice(color_list))
        tim.forward(50)  # Space dots 50 units apart horizontally
    # After completing a row, reposition to start next row
    # KEY CONCEPT: Get current position, then jump to next row's starting position
    x = tim.pos()[0]  # Current X coordinate
    y = tim.pos()[1]  # Current Y coordinate
    # Move left (x - 500) and up (y + 50) to next row's start
    tim.setpos(x - 500, y + 50)

screen = turtle.Screen()
screen.exitonclick()