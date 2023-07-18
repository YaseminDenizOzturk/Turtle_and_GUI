from turtle import Turtle,Screen
x = Turtle()
screen = Screen()


def move_forwards():
    x.forward(20)

def move_backwards():
    x.backward(20)

def turn_left():
    new_heading = x.heading() + 20
    x.setheading(new_heading)

def turn_right():
    new_heading = x.heading() - 20
    x.setheading(new_heading)

def clear():
    x.clear()
    x.penup()
    x.home()
    x.pendown()


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()
