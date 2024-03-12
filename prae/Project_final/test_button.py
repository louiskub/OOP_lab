import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

def increment_value():
    current_value = value_var.get()
    value_var.set(current_value + 1)

def decrement_value():
    current_value = value_var.get()
    value_var.set(current_value - 1)

if __name__ == "__main__":
    root = ttk.Window(themename='flatly')
    root.title("Increment/Decrement Example")
    root.geometry('400x200')

    # Create an IntVar to hold the numeric value
    value_var = IntVar()
    value_var.set(0)

    # Create a label displaying the value
    label = ttk.Label(root, textvariable=value_var, font=("Helvetica", 15))
    label.pack(pady=20)

    # Create buttons to increment and decrement the value
    plus_button = tk.Button(root, text="+", command=increment_value)
    plus_button.pack(side=LEFT, padx=10)

    minus_button = tk.Button(root, text="-", command=decrement_value)
    minus_button.pack(side=LEFT, padx=10)

    root.mainloop()

