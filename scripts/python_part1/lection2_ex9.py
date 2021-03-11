import turtle
import math
x = 0
y = 0
Vx = 10
Vy = 40
dt = 0.1
ay = -10
for i in range(100):    
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if abs(y) <=0.05:
        Vy = abs(Vy)
    turtle.goto(x, y)