import turtle

n = 100
turtle.shape('turtle')
for i in range(5*n):
	turtle.forward(0.01*i)
	turtle.left(360/n)
