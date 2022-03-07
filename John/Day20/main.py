from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

segments = []

starting_positions = [(0,0),(-20,0),(-40,0)]

def move_up():
    new_coord_x = int(segments[0].xcor())
    new_coord_y = int(segments[0].ycor()) + 20
    new_coord = (new_coord_x, new_coord_y)
    print(f"New Coord is {new_coord}")
    move_segments(new_coord)
    return

def move_left():
    new_coord_x = int(segments[0].xcor()) - 20
    new_coord_y = int(segments[0].ycor())
    new_coord = (new_coord_x, new_coord_y)
    print(f"New Coord is {new_coord}")
    move_segments(new_coord)
    return

def move_right():
    new_coord_x = int(segments[0].xcor()) + 20
    new_coord_y = int(segments[0].ycor())
    new_coord = (new_coord_x, new_coord_y)
    print(f"New Coord is {new_coord}")
    move_segments(new_coord)
    return

def move_down():
    new_coord_x = int(segments[0].xcor())
    new_coord_y = int(segments[0].ycor()) - 20
    new_coord = (new_coord_x, new_coord_y)
    print(f"New Coord is {new_coord}")
    move_segments(new_coord)
    return

def move_segments(first_segment_coord):
    prev_coord = first_segment_coord
    next_coord = ()
    for segment in segments:
        next_coord = segment.position()
        segment.goto(prev_coord)
        prev_coord = next_coord
    pass

# def clear_screen():
#     coord = 0
#     for segment in segments:
#         segment.goto(starting_positions[coord])
#         coord += 1






for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# playing = True
#
# while playing:

screen.listen()
screen.onkeyrelease(fun=move_up, key="w")
screen.onkeyrelease(fun=move_left, key="a")
screen.onkeyrelease(fun=move_right, key="d")
screen.onkeyrelease(fun=move_down, key="s")
screen.onkeyrelease(fun=clear_screen, key="c")


screen.exitonclick()