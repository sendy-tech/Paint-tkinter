from tkinter import *

canvas_width = 700
canvas_height = 500
brush_size = 3
color = "black"


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)


def brish_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


root = Tk()
root.title('Simple Tkinter Paint')

w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg="white")
w.bind("<B1-Motion>", paint)

red_btn = Button(text="Red", width=8, command=lambda: color_change("red"))
or_btn = Button(text="Orange", width=8, command=lambda: color_change("orange"))
yel_btn = Button(text="Yellow", width=8, command=lambda: color_change("yellow"))
green_btn = Button(text="Green", width=8, command=lambda: color_change("green"))
l_blue_btn = Button(text="lBlue", width=8, command=lambda: color_change("light sky blue"))
blue_btn = Button(text="Blue", width=8, command=lambda: color_change("blue"))
purple_btn = Button(text="Purple", width=8, command=lambda: color_change("purple"))
grey_btn = Button(text="Grey", width=8, command=lambda: color_change("grey"))
black_btn = Button(text="Black", width=8, command=lambda: color_change("black"))
white_btn = Button(text="Eraser", width=8, command=lambda: color_change("white"))

clear_btn = Button(text="Clear all", width=10, command=lambda: w.delete("all"))

w.grid(row=2,
       column=0,
       columnspan=7,
       padx=5,
       pady=5,
       sticky=E+W+S+N)

w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

red_btn.grid(row=0, column=2)
or_btn.grid(row=0, column=3)
yel_btn.grid(row=0, column=4)
green_btn.grid(row=0, column=5)
l_blue_btn.grid(row=0, column=6)
blue_btn.grid(row=0, column=7)
purple_btn.grid(row=0, column=8)
grey_btn.grid(row=0, column=9)
black_btn.grid(row=0, column=10)
white_btn.grid(row=0, column=11)

root.mainloop()
