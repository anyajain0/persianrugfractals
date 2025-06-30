import turtle
import math
from sierp import sierpy

def koch(t, length, depth):
    if depth==0:
        t.forward(length)
    else:
        koch(t,length/3, depth-1)
        t.left(60)
        koch(t,length/3, depth-1)
        t.right(120)
        koch(t,length/3, depth-1)
        t.left(60)
        koch(t,length/3, depth-1)
   
def kochsnow(t,l, d, x,y):
    t.penup()
    t.goto(x-(l/2),(y+l*math.sqrt(3)/2))
    t.pendown()
    for i in range(3):   
        koch(t, l,d)
        t.right(120)
        
def pent(t,radius,depth, n,x,y):
    angle = 360 / n
    sint = math.sin(math.pi / n)
    #most annoying part ever to figure out
    denom = 1 + sint * (math.sqrt(3)) / (3 ** depth)
    sidelength = 2 * radius * sint / denom
    max_bump = (3**depth) * (math.sqrt(3)/2)
    t.penup()
    t.goto(x , y + radius)
    t.setheading(0)
    t.right(180 / n)
    t.pendown()

    for i in range(n):
        koch(t, sidelength, depth)
        t.right(angle)
        
def middleart(t, depth, n):
    pent(t, 100, depth, n ,0,0)
    b=80

    while b > 5:
        pent(t, b, depth, n, 0,0)
        b -= 10
        t=t
        
    for i in range(depth*4):
        angle = 2 * math.pi * i / (depth*4)
        x = 130 * math.cos(angle)
        y = 130 * math.sin(angle)
        pent(t, 30, depth, n, x, y)
        
    for i in range(depth*8):
        angle = 2 * math.pi * i / (depth*8)
        x = 150 * math.cos(angle)
        y = 150 * math.sin(angle)
        pent(t, 20, depth, n, x, y)


def arounder(t, depth, n, cx, cy, semirad,count, rad, vflip = False, hflip=False):
    import math
    if count is None:
        count = depth * 6  
    for i in range(count):
        angle = math.pi * i / (count - 1)  
        x = cx + semirad * math.cos(angle) * (-1 if hflip else 1) + 1
        y = cy + semirad * math.sin(angle) * (-1 if vflip else 1)
        if i % 2 == 0:
            pent(t, rad, depth, n, x, y)
        else:
            sierpy(t, rad, depth, n, x, y)
