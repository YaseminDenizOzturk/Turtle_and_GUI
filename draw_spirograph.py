import turtle as t
import random

x = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


x.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        x.color(random_color())
        x.circle(100)
        x.setheading(x.heading() + size_of_gap)

# içine girdiğim değer yarıçap değeridir.


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
# exitonclick ile biz ekrana tıklayana kadar ekranı kapatmaz.
