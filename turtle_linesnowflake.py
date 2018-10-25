#!/bin/python3

import turtle
import random
alina = turtle.Turtle()

turtle.Screen().bgcolor("grey")
colors = ["cyan","purple","white","blue"]

alina.penup()
alina.forward(90)
alina.left(45)
alina.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            alina.forward(30)
            alina.backward(30)
            alina.right(45)
        alina.left(90)
        alina.backward(30)
        alina.left(45)
    alina.right(90)
    alina.forward(90)
    
for i in range(8):
    branch()
    alina.left(45)
    
 # alina.color(random.choice(colors))
  