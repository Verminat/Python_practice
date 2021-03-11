import turtle

turtle.shape('turtle')
turtle.speed(10)
n = 1000
for i in range(n):
	turtle.forward(1)
	turtle.left(360/n)
