# turtle example
# https://pythonbasics.org
import turtle
import random

def drawshape(sides, length):
    angle = 360.0 / sides
    for sides in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def drawsquare(length):
    drawshape(4,length)

def drawtriangle(length):
    drawshape(3,length)

def drawcircle(length):
    drawshape(360, length)

drawcircle(1)
drawsquare(100)
drawtriangle(250)

turtle.done()
