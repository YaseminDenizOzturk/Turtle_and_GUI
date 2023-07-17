from turtle import Turtle

x = Turtle()

kenar_sayisi = 3

for _ in range(kenar_sayisi):
    aci = 360 / kenar_sayisi
    x.forward(100)
    # 100 adım ilerleyecek.
    x.right(aci)
    # yani right(aci) yaptığım zaman o açı kadar sağa dönecek.
    
