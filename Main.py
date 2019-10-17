import Window_File as win
import math
import tkinter as tk
import triangle_solve
import time
import sys
import sys
from threading import Thread

#right triangle calculator
# angle_a = angle_c
# angle_b = angle_a
# angle_c = angle_b

def update():
    if win.side_a_box.get() == "0":
        win.side_a_box.delete(0, tk.END)
        win.side_a_box.insert(0, side_a)
    if win.side_b_box.get() == "0":
        win.side_b_box.delete(0, tk.END)
        win.side_b_box.insert(0, side_b)
    if win.side_c_box.get() == "0":
        win.side_c_box.delete(0, tk.END)
        win.side_c_box.insert(0, side_c)

    if win.angle_a_box.get() == "0":
        win.angle_a_box.delete(0, tk.END)
        win.angle_a_box.insert(0, angle_a)
    if win.angle_b_box.get() == "0":
        win.angle_b_box.delete(0, tk.END)
        win.angle_b_box.insert(0, angle_b)
    if win.direction_box.get() == "":
        win.direction_box.delete(0, tk.END)
        win.direction_box.insert(0, "n")

def calculate():
    win.alert_label.config(fg="grey25")

    global side_a, side_b, side_c, angle_a, angle_b, angle_c

    try:
        side_a = float(win.side_a_box.get())
        side_b = float(win.side_b_box.get())
        side_c = float(win.side_c_box.get())
        angle_a = float(win.angle_a_box.get())
        angle_b = float(win.angle_b_box.get())


    except ValueError:
        win.alert_label.config(text="ERROR: INT WAS NOT FOUND IN ONE OR MORE BOXES", fg="white")

    dimensions = triangle_solve.solve_triangle(side_a, side_b, side_c, angle_a, angle_b)
    side_a = dimensions[0]
    side_b = dimensions[1]
    side_c = dimensions[2]
    angle_a = dimensions[3]
    angle_b = dimensions[4]
    
    update()
    win.draw_triangle(win.triangle, 2, side_a, side_b, side_c, angle_a, angle_b, angle_c, win.direction_box.get())
    win.screen.update()

def tick():
    win.move_title()
    try:
        win.screen.update()
        time.sleep(0.01)
    except:
        pass

    tick()

sys.setrecursionlimit(10000000)

side_a = 3
side_b = 4
side_c = (math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2)))
#(side_a ** 2 + side_b ** 2) ** 0.5
a = side_a
b = side_b
c = side_c

# 207:	224	:305

angle_a =  math.degrees(math.asin(side_a/side_c))
angle_b = math.degrees(math.atan(side_b/side_a))
angle_c = 90

win.initialize(1000)

win.side_a_box.insert(0, side_a)
win.side_b_box.insert(0, side_b)
win.side_c_box.insert(0, side_c)
win.angle_a_box.insert(0, angle_a)
win.angle_b_box.insert(0, angle_b)

win.draw_triangle(win.triangle, 2, side_a, side_b, side_c, angle_a, angle_b, angle_c)

button = tk.Button(win.controls, text="Draw Triangle", command=calculate)
button.grid(row=3, column=0)

dimensions = []

tick()

win.screen.update()

win.root.mainloop()
