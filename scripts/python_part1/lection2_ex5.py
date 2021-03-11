def stick():
	turtle.forward(50)
	turtle.stamp()
	turtle.backward(50)


n = int(input())

import turtle

turtle.shape('turtle')
for i in range(n):
	stick()
	turtle.left(360/n)
