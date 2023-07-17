from turtle import Turtle

x = Turtle()

for _ in range(15):
    x.forward(10)
    # 10 adım ileri gidecek 
    x.penup()
    # kalem penup olunca yukarı kaldırılır ve hareket halindeyken çizim yapılmaz.
    x.forward(10)
    # 10 adım ileri gider.
    x.pendown()
    # kalem tekrar aşağı doğru bakar ve çizim yapar.
