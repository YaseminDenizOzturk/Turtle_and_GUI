from turtle import Turtle 
import random

x = Turtle()
colours = ["lime","red","pink","dark slate blue"]
directions = [0,90,180,270]
x.pensize(15)
x.speed("fastest")

for _ in range(200):
    x.color(random.choice(colours))
    x.forward(30)
    x.setheading(random.choice(directions))
    # kaplumbağayı istenilen yöne döndürür.
    