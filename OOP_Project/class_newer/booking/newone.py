import ttkbootstrap as ttk
import tkinter as tk
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import filedialog
import ttkbootstrap as ttk
import requests


root = ttk.Window(themename="superhero")
root.title("Scroll Frame")
root.geometry('1920x1080')
frame2 = ttk.Frame(root)
# def create_frame():
#     frame1 = ttk.Frame(root)
#     frame1.pack()
#     background_image = PhotoImage(file="background.png")
#     label = ttk.Label(frame1, image=background_image)
#     label.pack()
def create_frame():
    pass
b = ttk.Button(frame2, text="Download", bootstyle="success outline",padding="10 5",
                command=lambda : create_frame())
b.place(x=20, y=30)

root.mainloop()