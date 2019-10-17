import tkinter as tk
import turtle

max_space = 170
space = " "
operator = "add"
numberofspaces = 0

def move_title():

    global numberofspaces
    global operator
    global space

    if numberofspaces == 0:
        operator = "add"
    elif numberofspaces == max_space:
        operator = "subtract"
    if operator == "add":
        numberofspaces += 1
    elif operator == "subtract":
        numberofspaces -= 1
    try:
        root.title("{}Ethan's Triangle Drawing Program".format(space * numberofspaces))
    except:
        pass

def draw_triangle(pen, multiple, side_a, side_b, side_c, angle_a, angle_b, angle_c, direction="e"):
    #resize sides to fit window
    global a, b, c
    a = side_a
    b = side_b
    c = side_c
    if a > 0 and b > 0 and c > 0:
        if a < 50 or b < 50 or c < 50:
            while a < 50 or b < 50 or c < 50:
                a = a * 2
                b = b * 2
                c = c * 2
        elif a > 50 or b > 50 or c > 50:
            while a > 50 or b > 50 or c > 50:
                a = a / 2
                b = b / 2
                c = c / 2

    #setup for pen
    pen.reset()
    pen.hideturtle()
    pen.up()
    pen.goto(-(b/2), a/2)

    if direction == 'n':
        pen.setheading(90)
    elif direction == 'e':
        pen.setheading(0)
    elif direction == 's':
        pen.setheading(270)
    elif direction == 'w':
        pen.setheading(180)



    pen.color("white")

    #write Angle B
    pen.left(180)
    pen.fd(20)
    pen.left(90)
    pen.fd(20)
    pen.write(u"{}\u00B0".format(round(angle_b, 2)))
    pen.left(180)
    pen.fd(20)
    pen.right(90)
    pen.fd(20)

    #Side A
    pen.pendown()
    pen.fd((a * multiple)/2)
    pen.right(90)
    pen.up()
    pen.fd(20)
    pen.write(round(side_a, 2))
    pen.left(180)
    pen.fd(20)
    pen.right(90)
    pen.pendown()
    pen.fd((a * multiple)/2)

    #write Angle C
    pen.up()
    pen.fd(20)
    pen.right(90)
    pen.fd(20)
    pen.write(u"{}\u00B0".format(round(angle_c, 2)))
    pen.left(180)
    pen.fd(20)
    pen.left(90)
    pen.fd(20)
    pen.left(180)
    pen.left(angle_c)
    pen.pendown()

    #Side B
    pen.fd((b * multiple)/2)

    #Write Side B
    pen.right(90)
    pen.up()
    pen.fd(20)
    pen.write(round(side_b, 2))
    pen.left(180)
    pen.fd(20)
    pen.right(90)

    pen.pendown()
    pen.fd((b * multiple)/2)

    #Write Angle A
    pen.up()
    pen.fd(20)
    pen.right(90)
    pen.fd(20)
    pen.write(u"{}\u00B0".format(round(angle_a, 2)))
    pen.right(90)
    pen.fd(20)
    pen.right(90)
    pen.fd(20)

    pen.left(90)
    pen.right(angle_a)

    #Side C
    pen.pendown()
    pen.fd((c * multiple)/2)
    pen.right(90)

    #write Side C
    pen.up()
    pen.fd(20)
    pen.write(round(side_c, 2))
    pen.left(180)
    pen.fd(20)
    pen.right(90)
    pen.pendown()
    pen.fd((c * multiple)/2)
    #pen.goto(-(side_b/2), side_a/2)

    #remove this later
    #pen.left(180)
    #pen.right(angle_c)
    #pen.fd(side_a)

def initialize(size=600):
    global root
    root = tk.Tk()
    root.geometry('{}x{}'.format(size, size))
    root.title("Ethan Posner's Triangle Program")
    root.configure(background='grey25')


    canvas = tk.Canvas(root, width=str(900), height=str(800), highlightbackground="green", highlightcolor="green", highlightthickness=0)
    canvas.place(relx=.5, rely=.85, anchor="s")
    global screen
    screen = turtle.TurtleScreen(canvas)

    global triangle
    triangle = turtle.RawTurtle(screen)
    # triangle.ht()
    screen.tracer(0)
    screen.bgcolor('grey25')

    ### end of standard turtle process ###

    # frame for user input
    global controls
    controls = tk.Frame(root)
    controls.configure(background='grey25')
    controls.place(relx=0.1, rely=0.85)

    # labels and input boxes to change side and angle variables of triangle
    global side_a_label, side_a_box, side_b_label, side_b_box, side_c_label, side_c_box, angle_a_label, angle_a_box, angle_b_label, angle_b_box, angle_c_label, angle_c_box, alert_label, direction_box
    side_a_label = tk.Label(controls, text="side A: ", bg="grey25", fg="white")
    side_a_label.grid(row=0, column=0)
    side_a_box = tk.Entry(controls)
    side_a_box.grid(row=0, column=1)

    side_b_label = tk.Label(controls, text="side B: ", bg="grey25", fg="white")
    side_b_label.grid(row=1, column=0)
    side_b_box = tk.Entry(controls)
    side_b_box.grid(row=1, column=1)
    side_c_label = tk.Label(controls, text="side C: ", bg="grey25", fg="white")
    side_c_label.grid(row=2, column=0)
    side_c_box = tk.Entry(controls)
    side_c_box.grid(row=2, column=1)

    angle_a_label = tk.Label(controls, text="Angle A: ", bg="grey25", fg="white")
    angle_a_label.grid(row=0, column=2)
    angle_a_box = tk.Entry(controls)
    angle_a_box.grid(row=0, column=3)

    direction_label = tk.Label(controls, text="Direction: ", bg="grey25", fg="white")
    direction_label.grid(row=0, column=4)
    direction_box = tk.Entry(controls)
    direction_box.grid(row=0, column=5)

    angle_b_label = tk.Label(controls, text="Angle B: ", bg="grey25", fg="white")
    angle_b_label.grid(row=1, column=2)
    angle_b_box = tk.Entry(controls)
    angle_b_box.grid(row=1, column=3)
    angle_c_label = tk.Label(controls, text="Angle C: ", bg="grey25", fg="white")
    angle_c_label.grid(row=2, column=2)
    angle_c_box_label = tk.Label(controls, text="90", bg="grey25", fg="white")
    angle_c_box_label.grid(row=2, column=3)

    alert_label = tk.Label(controls, bg="grey25", fg="white")
    alert_label.grid(row=3, column=1, columnspan="3")
