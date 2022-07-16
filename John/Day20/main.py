from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# screen.tracer(0)

segments = []

starting_positions = [(0,0),(-20,0),(-40,0)]


def move_up():
    ##TODO: 1: set new heading
    segments[0].setheading(90)
    move_segments()
    return

def move_down():
    ##TODO: 1: set new heading
    segments[0].setheading(270)
    move_segments()
    return

def move_left():
    ##TODO: 1: set new heading
    segments[0].setheading(180)
    move_segments()
    return

def move_right():
    ##TODO: 1: set new heading
    segments[0].setheading(0)
    move_segments()
    return


# def move_up():
#
#     new_coord_x = int(segments[0].xcor())
#     new_coord_y = int(segments[0].ycor()) + 20
#     new_coord = (new_coord_x, new_coord_y)
#     print(f"New Coord is {new_coord}")
#     move_segments(new_coord)
#     return
#
# def move_left():
#     new_coord_x = int(segments[0].xcor()) - 20
#     new_coord_y = int(segments[0].ycor())
#     new_coord = (new_coord_x, new_coord_y)
#     print(f"New Coord is {new_coord}")
#     move_segments(new_coord)
#     return
#
# def move_right():
#     new_coord_x = int(segments[0].xcor()) + 20
#     new_coord_y = int(segments[0].ycor())
#     new_coord = (new_coord_x, new_coord_y)
#     print(f"New Coord is {new_coord}")
#     move_segments(new_coord)
#     return
#
# def move_down():
#     new_coord_x = int(segments[0].xcor())
#     new_coord_y = int(segments[0].ycor()) - 20
#     new_coord = (new_coord_x, new_coord_y)
#     print(f"New Coord is {new_coord}")
#     move_segments(new_coord)
#     return

def move_segments():

    #print(f'LEader coord is: {leader_coord[0]}')
    #segments[0].forward(20)
    #first_segment_coord = segments[0].position()
    #prev_coord = first_segment_coord
    loopcount = 0
    for segment in segments:
        if loopcount == 0:
            leader_coord = segment.position()
            segment.forward(20)
        elif loopcount > 0:
            next_coord = segment.position()
            segment.goto(leader_coord)
            leader_coord = next_coord

        loopcount += 1

    #screen.update()





        # next_coord = segment.position()
        # prev_coord = next_coord
        # if next_coord==
        # segment.goto(prev_coord)

    return

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

screen.update()


# playing = True
#
# while playing:

screen.listen()
screen.onkeyrelease(fun=move_up, key="w")
screen.onkeyrelease(fun=move_left, key="a")
screen.onkeyrelease(fun=move_right, key="d")
screen.onkeyrelease(fun=move_down, key="s")
#screen.onkeyrelease(fun=clear_screen, key="c")


screen.exitonclick()