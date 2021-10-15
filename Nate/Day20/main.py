from turtle import Screen, Turtle
from random import randint

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

stamp_ids = []


def init_snake():
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    stamp_ids.append(t.stamp())
    t.forward(20)
    stamp_ids.append(t.stamp())
    t.forward(20)
    stamp_ids.append(t.stamp())
    return t


def add_snake():
    snake.forward(20)
    stamp_ids.append(snake.stamp())


def move_forward():
    snake.forward(20)
    stamp_ids.append(snake.stamp())
    snake.clearstamp(stamp_ids[0])
    stamp_ids.pop(0)


def turn_up():
    if snake.heading() == 270:
        return
    else:
        snake.setheading(90)


def turn_right():
    if snake.heading() == 180:
        return
    else:
        snake.setheading(0)


def turn_down():
    if snake.heading() == 90:
        return
    else:
        snake.setheading(270)


def turn_left():
    if snake.heading() == 0:
        return
    else:
        snake.setheading(180)


def check_collision():
    if snake.xcor() > 280 or snake.xcor() < -280:
        return True
    if snake.ycor() > 300 or snake.ycor() < -300:
        return True
    else:
        return False


def init_bait():
    b = Turtle(shape="circle")
    b.hideturtle()
    b.color("blue")
    b.penup()
    bait_x = randint(-250, 250)
    bait_y = randint(-250, 250)
    b.setpos(x=bait_x, y=bait_y)
    b.stamp()
    return b


def move_bait(b):
    bait_x = randint(-250, 250)
    bait_y = randint(-250, 250)
    b.setpos(x=bait_x, y=bait_y)
    b.stamp()


def hit_bait():
    if snake.ycor() == bait.ycor() and snake.xcor() == bait.xcor():
        bait.clearstamps()
        return True
    else:
        return False


snake = init_snake()
bait = init_bait()
screen.listen()

screen.onkey(turn_up, "Up")
screen.onkey(turn_right, "Right")
screen.onkey(turn_down, "Down")
screen.onkey(turn_left, "Left")

collision = False
score = 0
while not collision:
    print(stamp_ids)
    move_forward()

    # check if we've hit the bait

    # check if we've hit anything
    if check_collision():
        collision = True
    elif hit_bait():
        add_snake()
        score += 1
        move_bait(bait)




screen.exitonclick()
