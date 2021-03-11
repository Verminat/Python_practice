import turtle

turtle.shape('turtle')

def square(x):
	for i in range(4):
		turtle.forward(x)
		turtle.left(90)

for i in range(10):
	turtle.penup()
	turtle.goto(-5*i, -5*i)
	turtle.pendown()
	square(10*(i+1))
