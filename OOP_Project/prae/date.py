from tkinter import *
#from api import Item
import ttkbootstrap as ttk
from ttkbootstrap import Style, PRIMARY
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime, date
from tkcalendar import Calendar 
import requests
import json

def hello():
    print("hello")
def hello2():
    print("hello2")
root = ttk.Window()

button2 = ttk.Button(root, text = f"-", command = lambda: hello())
button2.configure(command=lambda: hello2())
button2.pack()
root.mainloop()