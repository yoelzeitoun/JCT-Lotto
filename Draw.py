from tkinter import *


class Draw:

    def __init__(self, master):
        global canvas
        canvas = Canvas(master, width=650, height=500, background='white')
        canvas.pack()
        canvas.bind('<ButtonPress>', self.mouse_press)
        canvas.bind('<B1-Motion>', self.draw)

    def mouse_press(self, event):
        global var1
        var1 = event

    def draw(self, event):
        global var1
        canvas.create_line(var1.x, var1.y, event.x, event.y)
        var1 = event
