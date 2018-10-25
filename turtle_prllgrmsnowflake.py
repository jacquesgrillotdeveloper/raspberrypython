#!/bin/python3

import turtle
import random
autumn = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colors = ["cyan","purple","white","blue"]
autumn.color("magenta")
for i in range(10):
  for i in range(2):
    autumn.forward(100)
    autumn.right(60)
    autumn.forward(100)
    autumn.right(120)
  autumn.right(36)
  autumn.color(random.choice(colors))
  