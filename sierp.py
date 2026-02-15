import turtle
import math

#inner_border method should be in this file

def sierpy(t, radius, depth, n, x, y, flip=False):
    if depth == 0:
        t.penup()
        anglestep = 360 / n

        start_x = x + (radius * math.cos(0)) *  (-1 if flip else 1)
        t.goto(start_x, y + radius * math.sin(0))
        t.pendown()
        for i in range(1, n + 1):
            angle = math.radians(i * anglestep)
            vx = x + radius * math.cos(angle)* (-1 if flip else 1)
            vy = y + radius * math.sin(angle)
            t.goto(vx, vy)
    else:
        anglestep = 360 / n
        for i in range(n):
            angle = math.radians(i * anglestep)
            vx = x + radius * math.cos(angle)* (-1 if flip else 1)
            vy = y + radius * math.sin(angle)
            sierpy(t, radius / 2, depth - 1, n, vx, vy, flip=flip)

def border(t, depth, n):
    t.penup()
    t.goto(-250, -350)
    t.setheading(0)
    t.pendown()
    a= -250-30
    b=-350
    while b < 350:
        sierpy(t, 20, depth, n, a, b)
        b+=50
    t.right(90)
    while a < 250:
        sierpy(t, 20, depth, n, a, b)
        a+=50
    t.right(90)
    while b > -350:   
        sierpy(t, 20, depth, n, a, b, flip=True)
        b-=50
    t.right(90)
    while a > -275:   
        sierpy(t, 20, depth, n, a, b, flip=False)
        a-=50
