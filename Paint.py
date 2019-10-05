from tkinter import *
from PIL import ImageTk

canvas_width = 1000
canvas_height = 600
brush_size = 3
color = "black"


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def brish_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


root = Tk()
root.title('Simple Tkinter Paint')

w = Canvas(root, width=canvas_width, height=canvas_height, bg="white")

w.bind("<B1-Motion>", paint)

white_btn = Button(background="white", width=5, height=2, command=lambda: color_change("white"))
pink_btn = Button(background="hot pink", width=5, height=2, command=lambda: color_change("hot pink"))
red_btn = Button(background="Red", width=5, height=2, command=lambda: color_change("red"))
or_btn = Button(background="Orange", width=5, height=2, command=lambda: color_change("orange"))
yel_btn = Button(background="Yellow", width=5, height=2, command=lambda: color_change("yellow"))
green_btn = Button(background="Green", width=5, height=2, command=lambda: color_change("green"))
aqua_btn = Button(background="aquamarine", width=5, height=2, command=lambda: color_change("aquamarine"))
l_blue_btn = Button(background="light sky blue", width=5, height=2, command=lambda: color_change("light sky blue"))
blue_btn = Button(background="Blue", width=5, height=2, command=lambda: color_change("blue"))
cora_btn = Button(background="coral", width=5, height=2, command=lambda: color_change("coral"))
purple_btn = Button(background="Purple", width=5, height=2, command=lambda: color_change("purple"))
grey_btn = Button(background="Grey", width=5, height=2, command=lambda: color_change("grey"))
black_btn = Button(background="Black", width=5, height=2, command=lambda: color_change("black"))
brown_btn = Button(background="brown", width=5, height=2, command=lambda: color_change("brown"))

clear_btn = Button(text="Clear all", width=7, height=3, command=lambda: w.delete("all"))

image3 = ImageTk.PhotoImage(file="3.png")
image5 = ImageTk.PhotoImage(file="5.png")
image7 = ImageTk.PhotoImage(file="7.png")
image9 = ImageTk.PhotoImage(file="9.png")
image11 = ImageTk.PhotoImage(file="11.png")

orig_btn = Button(image=image3, command=lambda: brish_size_change(3))
five_btn = Button(image=image5, command=lambda: brish_size_change(5))
seven_btn = Button(image=image7, command=lambda: brish_size_change(7))
nine_btn = Button(image=image9, command=lambda: brish_size_change(9))
eleven_btn = Button(image=image11, command=lambda: brish_size_change(11))

w.grid(row=2,
       column=0,
       columnspan=7,
       padx=5,
       pady=5,
       sticky=E+W+S+N)

w.columnconfigure(10, weight=1)
w.rowconfigure(2, weight=1)


white_btn.place(x=10, y=10)
pink_btn.place(x=80, y=10)
red_btn.place(x=150, y=10)
or_btn.place(x=220, y=10)
yel_btn.place(x=290, y=10)
green_btn.place(x=360, y=10)
aqua_btn.place(x=430, y=10)
l_blue_btn.place(x=500, y=10)
blue_btn.place(x=570, y=10)
cora_btn.place(x=640, y=10)
purple_btn.place(x=710, y=10)
brown_btn.place(x=780, y=10)
grey_btn.place(x=850, y=10)
black_btn.place(x=920, y=10)


clear_btn.grid(row=0, column = 12)
orig_btn.place(x=1030, y=100)
five_btn.place(x=1030, y=150)
seven_btn.place(x=1030, y=200)
nine_btn.place(x=1030, y=250)
eleven_btn.place(x=1030, y=300)

root.mainloop()
