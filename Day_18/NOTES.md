# Day 18: Turtle Graphics & Generative Art

## What You Learned
This day focuses on **Turtle graphics fundamentals**: drawing with loops, coordinate systems, color manipulation, and procedural generation. You'll create visual patterns using simple turtle commands, introducing algorithmic art and image data extraction (colorgram).

---

## Key Concepts
### 1. Turtle Graphics Basics
Turtle is a Python library for drawing using a virtual "turtle" that moves and draws lines:

```python
from turtle import Turtle, Screen

tim = Turtle()
tim.forward(100)  # Move forward 100 units, drawing a line
tim.right(90)     # Turn right 90 degrees
tim.penup()       # Stop drawing
tim.pendown()     # Resume drawing
```

The turtle has **state**: position, heading (direction), pen up/down, color, speed.

### 2. Drawing Shapes with Loops
Challenge 01: Draw a square
```python
for _ in range(4):
    tim.forward(100)
    tim.right(90)
```

Challenge 03: Draw polygons (3-10 sides)
```python
def draw_shape(number_of_sides):
    angle = 360 / number_of_sides  # Interior angle
    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)  # Triangle, square, pentagon, ... decagon
```

Key insight: **External angle = 360 / number_of_sides**. This is derived from geometry.

### 3. Pen State Management (Pen Up / Pen Down)
Challenge 02: Draw dashed line
```python
for _ in range(15):
    tim.forward(10)
    tim.penup()     # Lift pen
    tim.forward(10)  # Move without drawing
    tim.pendown()    # Lower pen
```

This creates a dotted pattern by toggling drawing on/off.

### 4. Random Number Generation
Challenge 04: Random walk with colors and directions
```python
import random

tim.speed("fastest")  # Increase speed for performance

for i in range(200):
    tim.forward(25)
    tim.color(random_color())
    tim.setheading(random.choice(turn_options))  # Random absolute heading
```

Key difference: `setheading()` sets absolute direction (0°=East, 90°=North, 180°=West, 270°=South), while `right()` rotates relative to current heading.

### 5. RGB Color Mode
```python
turtle.colormode(255)  # Use RGB 0-255 instead of 0-1

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim.color(random_color())  # Random color tuple
```

By default, Turtle uses color names ("red", "blue"); RGB mode allows numeric color specification.

### 6. Circular Drawings & Trigonometry
Challenge 05: Spirograph (overlapping circles)
```python
def draw_spiro(size_of_gap):
    for i in range(int(360 / size_of_gap)):  # Number of circles
        tim.color(random_color())
        tim.circle(100)  # Draw a circle of radius 100
        tim.setheading(tim.heading() + size_of_gap)  # Rotate turtle heading
```

This demonstrates how rotating the turtle before drawing circles creates spiral patterns.

### 7. Image Color Extraction (Colorgram)
The commented code in `hirst_painting.py` shows image processing:

```python
# import colorgram
# colors = colorgram.extract('image.jpg', 30)  # Extract 30 dominant colors
# color_list = []
# for color in colors:
#     make_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#     color_list.append(make_tuple)
```

This extracts dominant colors from an image and uses them for painting. It bridges visual design and code.

### 8. Grid Drawing (Hirst Painting)
`hirst_painting.py` draws a 10x10 grid of dots with colors from an image:

```python
for x in range(10):
    for y in range(10):  # Nested loops for grid
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    # After inner loop, reposition for next row
    x = tim.pos()[0]
    y = tim.pos()[1]
    tim.setpos(x - 500, y + 50)  # Move up, reset to left
```

This demonstrates **nested loops** for creating 2D patterns and **position tracking** (`tim.pos()`, `tim.setpos()`).

---

## Common Pitfalls
- **Confusing `right(angle)` vs. `setheading(angle)`**: `right()` rotates relative to current heading; `setheading()` sets absolute heading (0-360°).
- **Forgetting `turtle.colormode(255)`**: Without this, RGB tuples fail; Turtle expects color names.
- **Speed issues**: `tim.speed("fastest")` is necessary for loops with many iterations (avoids 1-minute execution times).
- **Grid repositioning logic**: In `hirst_painting.py`, the nested loop repositioning is non-obvious. Easy to off-by-one error in coordinates.
- **Integer division in loop count**: `int(360 / size_of_gap)` must convert float to int, otherwise `range()` fails.
- **Forgetting `screen.exitonclick()`**: Without it, the window closes immediately after drawing completes.

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1-5** | Variables, loops, functions, random module used here |
| **Day 9** | Tuples for RGB colors |
| **Day 15-16** | State management (turtle has position, heading, pen state) |
| **Day 17** | Event loops; here: drawing loop replaces question loop |
| **Day 19** | Turtle event listeners (keyboard input) build on Day 18 drawing |
| **Day 20-21** | Snake and Pong games use Turtle extensively |
| **Day 23** | Screen borders and collision detection build on turtle coordinates |

---

## Before You Move On
Make sure you can:
- [ ] Explain why `angle = 360 / number_of_sides` for drawing regular polygons
- [ ] Understand the difference between `tim.right(90)` and `tim.setheading(90)`
- [ ] Predict the output of Challenge 03 (polygons from 3-10 sides)
- [ ] Draw a square using only `forward()` and `right()` without a loop
- [ ] Explain what `penup()` and `pendown()` do and when to use them
- [ ] Understand nested loops in the grid drawing and coordinate tracking
- [ ] Understand RGB color tuples and `colormode(255)`

---

## Practice Prompt
**Mini-Project: Customizable Geometric Pattern Generator**
Create a drawing program that generates patterns based on user input:

1. **Spirograph Variations**:
   - Ask user for gap size (5, 10, 15, 20)
   - Ask user for circle radius (50, 75, 100, 150)
   - Draw the spirograph with these parameters
   - Example: `gap=10, radius=100` creates a 36-circle spiral

2. **Star Generator**:
   - Draw a star with N points (5, 6, 7, 8 points)
   - Each point is a triangle extending outward
   - Use random colors for each point
   - Formula: Angle between points = 360 / number_of_points

3. **Fractal-like Tree** (challenge):
   - Draw a trunk
   - At the top, split into two branches at angles
   - Recursively draw branches on those branches (smaller each time)
   - Create a tree-like structure

4. **Color Palette UI**:
   - Extract colors from an image using colorgram
   - Display all colors as a 10x10 grid of squares
   - User clicks to see the hex value of each color
   - (Requires turtle.textinput() for interaction)

**Bonus Challenge**:
- Create a "Mandala Generator" that uses nested loops and rotations to create symmetric patterns
- Add user input: `enter spiral gap size (1-30)` and draw multiple spirographs at once
- Experiment with transparency if possible (turtle has limited support)

**Reflection**:
- What patterns emerge? Why do certain angles create pleasing designs?
- How does changing the loop count or step size affect the pattern?
- Can you recreate a famous artwork pattern (Mondrian, Islamic tiles, etc.)?
