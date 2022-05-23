import turtle
import time
turtle.bgcolor('black')
seven = turtle.Turtle()
seven.pensize(3)
seven.speed(0)
seven.goto(200,200)
def drawnsquare():
    seven.rt(180)
    seven.fd(200)
    seven.rt(360)
    seven.fd(180)

for i in range(23):
    for colors in ['white','yellow','purple','orange']:
        seven.color(colors)
        drawnsquare()
        seven.rt(91)


time.sleep(50)


