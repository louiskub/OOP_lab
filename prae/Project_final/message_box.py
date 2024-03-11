from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

root = ttk.Window(themename='superhero')
root.title("Message Box")
root.geometry('1920x1080')

def clicker():
    mb = Messagebox.ok("Display message", "Title")
    my_label.config(text=f'You Clicked {mb}')

my_button = ttk.Button(root, text="Click Me!", bootstyle="danger", command=clicker)
my_button.pack(pady=20)

my_label = ttk.Label(root, text="", bootstyle="light", font=("Helvetica",14))
my_label.pack(pady=20)

root.mainloop()
