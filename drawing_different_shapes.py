from turtle import Turtle
import random

x = Turtle()

colours = ["lime","gold", "medium orchid"]

def sekil_cizme(kenar_sayisi):
    aci = 360 / kenar_sayisi
    for _ in range(kenar_sayisi):
        x.forward(100)
        x.right(aci)

for cizilecek_kenar in range (3,11):
    x.color(random.choice(colours))
    sekil_cizme(cizilecek_kenar)
