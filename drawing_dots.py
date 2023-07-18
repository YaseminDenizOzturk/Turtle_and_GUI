import turtle as turtle_module
import random

turtle_module.colormode(255)
x = turtle_module.Turtle()
x.speed("fastest")
x.penup()
x.hideturtle()

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

x.setheading(255)
x.forward(300)
x.setheading(0)

number_of_dots = 100


for _ in range(10):
    x.dot(20, random.choice(color_list))
    x.forward(30)
    # color_listten gelen rastgele bir renkten nokta koyup 30 adım ilerleyecek ve bu durum for döngüsü içerisinde devam edecek.

    if dot_count in range(1, number_of_dots + 1):
        x.setheading(90)
        x.forward(50)
        x.setheading(180)
        x.forward(500)
        x.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
# exitonclick ile biz ekrana tıklamadan ekranı kapatmaz.
