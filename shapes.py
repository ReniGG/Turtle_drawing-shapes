import turtle
import random

def random_color():
    return random.random(), random.random(), random.random() 


ws = turtle.Screen()
ws.bgcolor(random_color())
lee = turtle.Turtle()
lee.pensize(10)
lee.shape("turtle")
lee.speed(0)


for _ in range(4):
    lee.color(random_color())
    lee.forward(100)
    lee.left(90)

lee.left(180)

for _ in range(3):
    lee.color(random_color())
    lee.forward(100)
    lee.right(90)

lee.up()
lee.forward(100)
lee.down()

for _ in range(3):
    lee.color(random_color())
    lee.forward(100)
    lee.left(90)

lee.up()
lee.forward(200)
lee.down()

for _ in range(2):
    lee.color(random_color())
    lee.left(90)
    lee.forward(100)

lee.up()
lee.left(90)
lee.forward(100)
lee.right(90)
lee.forward(300)
lee.down()

for _ in range (24):
    lee.color(random_color())
    lee.circle(80)
    lee.up()
    lee.left(90)
    lee.forward(80)
    lee.right(75)
    lee.down()

lee.up()
lee.forward(300)
lee.down()



for i in range(50):
    lee.color(random_color())
    lee.forward(i * 2)
    lee.left(30)
    


turtle.exitonclick()