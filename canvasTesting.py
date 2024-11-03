#from tkinter import *

#class MainWindow(Frame):
#    def __init__(self):
#        super().__init__()
#        self.pack(expand=Y,fill=BOTH)

#        outercanvas = Canvas(self, width=200, height=100, bg='#00ffff')
#        outercanvas.pack(expand=Y,fill=BOTH)

#        innercanvas = Canvas(outercanvas, width=100, height=50)
#        outercanvas.create_window(50, 25, anchor=NW, window=innercanvas)

#        innercanvas.create_text(10, 10, anchor=NW, text="Hello")

#root = MainWindow()
#root.mainloop()

import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line')

root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()