import tkinter as tk 
from tkinter import * 
import os 

root= tk.Tk()

canvas =  tk.canvas(root, height=900, width=500, bg="#000000")
canvas.pack()

frame= tk.Frame(root, bg="#3e646c")
frame.place(relwidth=1, relheight=2, rely = 1, relx= 1)
root.mainloop()
