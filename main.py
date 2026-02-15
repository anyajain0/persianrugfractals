import turtle
import math

from koch2 import middleart
import tkinter as tk
from sierp import border
from sierp import inner_border
from koch2 import arounder
from turtle import RawTurtle, ScrolledCanvas

root = tk.Tk()
root.title("Persian Rug Fractal Graphics")
canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas = ScrolledCanvas(canvas_frame, width=600, height=800)
canvas.pack(fill=tk.BOTH, expand=True)
t = RawTurtle(canvas)
t.hideturtle()

def frame1():
    canvas.create_rectangle(-200, -300, 200, 300)
    canvas.create_rectangle(-225, -325, 225, 325)

def draw():
    t.clear()
    t.getscreen().tracer(0)
    frame1()
    border(t, int(slider2.get()), int(slider4.get()))
    inner_border(t, int(slider1.get()), int(slider3.get()))
    middleart(t, int(slider1.get()), int(slider3.get()))
    t.pendown()
    arounder(t, int(slider1.get()), int(slider3.get()), 0, 100, 170, 10, 10)
    arounder(t, int(slider1.get()), int(slider3.get()), 0, -80, 170, 10, 10, vflip=True, hflip=True)
    
    arounder(t, int(slider2.get()), int(slider4.get()), 0, 60, 150, 15, 5, vflip=False, hflip=False)
    arounder(t, int(slider2.get()), int(slider4.get()), 0, -50, 150, 15, 5, vflip=True, hflip=True)

    arounder(t, int(slider2.get()), int(slider4.get()), 0, 150, 200, 20, 4, vflip=False, hflip=False)
    arounder(t, int(slider2.get()), int(slider4.get()), 0, -150, 200, 20, 4, vflip=True, hflip=True)
     
    t.getscreen().update()
    
controls = tk.Frame(root)
controls.pack(side=tk.RIGHT, fill=tk.Y)

slider1 = tk.Scale(controls, from_=1, to=5, orient=tk.HORIZONTAL, label=" Int. Complexity")
slider1.pack(pady=10)

slider2 = tk.Scale(controls, from_=1, to=5, orient=tk.HORIZONTAL, label="Ext. Complexity")
slider2.pack(pady=10)

slider3 = tk.Scale(controls, from_=2, to=7, orient=tk.HORIZONTAL, label="Int. Roundness")
slider3.pack(pady=10)

slider4 = tk.Scale(controls, from_=2, to=7, orient=tk.HORIZONTAL, label="Ext. Roundness")
slider4.pack(pady=10)

button = tk.Button(controls, text="Draw Rug", command=draw)
button.pack(pady=10)


root.mainloop()

