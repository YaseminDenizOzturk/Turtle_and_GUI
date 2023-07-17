from turtle import Turtle

x = Turtle()

kenar_sayisi = 5

for _ in range(kenar_sayisi):
    aci = 360 / kenar_sayisi
    x.forward(100)
    x.right(aci)
    
