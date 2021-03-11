print("Введите какое число многоугольников вы хотите: ")
x = int(input())

import turtle
import math

def right_figure(R, n):
	for i in range(n):
		turtle.left(360/n)
		turtle.forward(2*R*math.sin(360/4/n/math.pi))

for i in range(3, x+3):
	right_figure(10*i, i)
	turtle.penup()
	turtle.goto(0, 0)
	turtle.pendown()